from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from model_bakery import baker



class MeTests(APITestCase):

    def setUp(self):
        self.url_me = '/api/me'
        self.url_signin = '/api/signin'    
        self.user = baker.make('users.User')
        self.phone = baker.make('users.Phone', user=self.user)
        self.user.set_password('1234')
        self.user.save()
        self.body = {
            'email': self.user.email, 'password': '1234'
        }
    
    def test_signin_success(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.url_me)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['first_name'], self.user.first_name)
        self.assertEqual(response.data['last_name'], self.user.last_name)
        self.assertEqual(response.data['email'], self.user.email)
        phone_data = response.data['phones'][0]
        phone_user = self.user.phones.first()
        self.assertEqual(phone_data['number'], phone_user.number)
        self.assertEqual(phone_data['area_code'], phone_user.area_code)
        self.assertEqual(phone_data['country_code'], phone_user.country_code)
        
    def test_signin_unauthorized(self):
        response = self.client.get(self.url_me)
        self.assertEqual(
            response.data['message'], "Unauthorized"
        )
        self.assertEqual(
            response.data['error_code'], status.HTTP_401_UNAUTHORIZED
        )
