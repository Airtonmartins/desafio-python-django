from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from model_bakery import baker



class SigninTests(APITestCase):

    def setUp(self):
        self.url = '/api/signin'   
        self.user = baker.make('users.User')
        self.user.set_password('1234')
        self.user.save()
        self.body = {
            'email': self.user.email, 'password': '1234'
        }
    
    def test_signin_success(self):
        response = self.client.post(self.url, self.body, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('token' in response.data)

    def test_signin_password_wrong(self):
        self.body['password'] = "12345"
        response = self.client.post(self.url, self.body, format='json')
        self.assertEqual(
            response.data['message'], "Invalid e-mail or password"
        )
        self.assertEqual(
            response.data['error_code'], status.HTTP_400_BAD_REQUEST
        )
    
    def test_signin_password_wrong(self):
        self.body['password'] = "12345"
        response = self.client.post(self.url, self.body, format='json')
        self.assertEqual(
            response.data['message'], "Invalid e-mail or password"
        )
        self.assertEqual(
            response.data['error_code'], status.HTTP_400_BAD_REQUEST
        )
    
    def test_signin_invalid_email(self):
        self.body['email'] = "email@email.com"
        response = self.client.post(self.url, self.body, format='json')
        self.assertEqual(
            response.data['message'], "Invalid e-mail or password"
        )
        self.assertEqual(
            response.data['error_code'], status.HTTP_400_BAD_REQUEST
        )
    
    def test_signin_without_body(self):
        response = self.client.post(self.url, {}, format='json')
        self.assertEqual(
            response.data['message'], "Missing fields"
        )
        self.assertEqual(
            response.data['error_code'], status.HTTP_400_BAD_REQUEST
        )