from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase , APIClient
import json

class FeedTestsViews(APITestCase):

    def setUp(self):
        url = reverse('users-api:register')
        data = {
            'username':'test',
            'email':'test@gmail.com', 
            'password':'test@123'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'test')
        self.test_user = User.objects.get(username='test')
        self.test_user_pwd = 'test@123'
        url = 'feeds-api:feed_create'
        reversed_url = reverse(url)
        data = {
            'content':"feed Test Post"
        }
        client = APIClient()
        client.force_authenticate(user=self.test_user)
        response = client.post(reversed_url, data)
        self.feed = json.loads(response.content.decode('utf-8'))
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_users_url(self):
        url = 'feeds-api:feeds'
        reversed_url = reverse(url)
        client = APIClient()
        client.force_authenticate(user=self.test_user)
        response = client.get(reversed_url)
        response_data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response_data.get('count'),1)

    def test_feeds_edit_view(self):
        url = 'feeds-api:feed-edit'
        reversed_url = reverse(url,args=[self.feed.get('id')])
        client = APIClient()
        client.force_authenticate(user=self.test_user)
        data = {
            'content':"feed Post edited"
        }
        response = client.patch(reversed_url,data, format='json')
        response_data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response_data.get('content'),data.get('content'))
        self.feed = response_data

    def test_feeds_details_view(self):
        client = APIClient()
        client.force_authenticate(user=self.test_user)
        url = 'feeds-api:feed-details'
        reversed_url = reverse(url,args=[self.feed.get('id')])
        response = client.get(reversed_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
