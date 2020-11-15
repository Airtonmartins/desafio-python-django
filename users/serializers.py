from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.models import update_last_login
from rest_framework import serializers
from rest_framework.exceptions import APIException
from rest_framework_jwt import serializers as jwt_serializers
from rest_framework_jwt.settings import api_settings
from .constants import ERRORS_MESSAGE_VALIDATION, INVALID_CREDENTIALS
from .models import Phone


jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
User = get_user_model()



class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = ('number', 'area_code', 'country_code')
        extra_kwargs = {
            'number': { 'error_messages': ERRORS_MESSAGE_VALIDATION },
            'area_code': { 'error_messages': ERRORS_MESSAGE_VALIDATION },
            'country_code': { 'error_messages': ERRORS_MESSAGE_VALIDATION }
        }

class UserSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(
        format='%d/%m/%Y - %H:%M', read_only=True
    )
    last_login = serializers.DateTimeField(
        format='%d/%m/%Y - %H:%M:%S', read_only=True
    )
    phones = PhoneSerializer(many=True)
    
    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email', 'password', 'phones', 
            'created_at', 'last_login'
        )
        extra_kwargs = {
            'first_name': { 'error_messages': ERRORS_MESSAGE_VALIDATION },
            'last_name': { 'error_messages': ERRORS_MESSAGE_VALIDATION },
            'email': {
                'error_messages': ERRORS_MESSAGE_VALIDATION
            },
            'password': {
                'write_only': True,
                'error_messages': ERRORS_MESSAGE_VALIDATION
            },
        }
    
    def __init__(self, *args, **kwargs):
        super(UserSerializer, self).__init__(*args, **kwargs)
        self.fields["phones"].error_messages["required"] = ERRORS_MESSAGE_VALIDATION['required']
    
    def create(self, validated_data):
        phones = validated_data.pop('phones')
        user = User.objects.create_user(**validated_data)
        for phone in phones:
            Phone.objects.create(user=user, **phone)
        return user


class JWTSerializerCustom(jwt_serializers.JSONWebTokenSerializer):

    def __init__(self, *args, **kwargs):
        super(JWTSerializerCustom, self).__init__(*args, **kwargs)
        self.fields["email"].error_messages["required"] = ERRORS_MESSAGE_VALIDATION['required']
        self.fields["password"].error_messages["required"] = ERRORS_MESSAGE_VALIDATION['required']
    

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(email=email, password=password)
            if user:
                payload = jwt_payload_handler(user)
                update_last_login(None, user)
                return {
                    'token': jwt_encode_handler(payload)
                }
            else:
                message = INVALID_CREDENTIALS
                raise serializers.ValidationError(message)
        else:
            message = ERRORS_MESSAGE_VALIDATION['required']
            raise serializers.ValidationError()


