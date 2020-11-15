from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from model_bakery import baker



class SignupTests(APITestCase):

    def setUp(self):
        self.url = '/api/signup'
        self.body = {
            "first_name": "First Name",
            "last_name": "Last name",
            "email": "email222@email.com",
            "password": "1234",
            "phones": [
                {
                    "number": 999999999,
                    "area_code": 81,
                    "country_code": "+55"
                },
                {
                    "number": 999999999,
                    "area_code": 81,
                    "country_code": "+55"
                },
                {
                    "number": 999999999,
                    "area_code": 81,
                    "country_code": "+55"
                }
            ]
        }
        self.user = baker.make('users.User')

    def test_signup_success(self):
        response = self.client.post(self.url, self.body, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue('token' in response.data)

    def test_signup_email_exist(self):
        self.body['email'] = self.user.email
        response = self.client.post(self.url, self.body, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['message'], "E-mail already exists")
        self.assertEqual(
            response.data['error_code'], status.HTTP_400_BAD_REQUEST
        )
    
    def test_signup_required_fields(self):
        self.body['first_name'] = ""
        self.body.pop('password')
        response = self.client.post(self.url, self.body, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['message'], "Missing fields")
        self.assertEqual(
            response.data['error_code'], status.HTTP_400_BAD_REQUEST
        )
    
    def test_signup_invalid_fields(self):
        self.body['email'] = 23234235
        response = self.client.post(self.url, self.body, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['message'], "Invalid fields")
        self.assertEqual(
            response.data['error_code'], status.HTTP_400_BAD_REQUEST
        )
    
    def test_signup_without_body(self):
        response = self.client.post(self.url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['message'], "Missing fields")
        self.assertEqual(
            response.data['error_code'], status.HTTP_400_BAD_REQUEST
        )
    
    def test_signup_required_phones_fields(self):
        self.body['phones'][0].pop('area_code')
        response = self.client.post(self.url, self.body, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['message'], "Missing fields")
        self.assertEqual(
            response.data['error_code'], status.HTTP_400_BAD_REQUEST
        )
