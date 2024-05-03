from django.urls import reverse , resolve
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from feed import views

class FeedTestsUrls(APITestCase):

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

    def test_feeds_url(self):
        url = 'feeds-api:feeds'
        reversed_url = reverse(url)
        self.assertEqual(resolve(reversed_url).func,views.feeds)
    
    def test_feeds_create_url(self):
        url = 'feeds-api:feed_create'
        reversed_url = reverse(url)
        self.assertEqual(resolve(reversed_url).func,views.create_feed)
    
    def test_feeds_edit_url(self):
        url = 'feeds-api:feed-edit'
        reversed_url = reverse(url,args=['9812-3ehj9-238d39-8hd23h'])
        self.assertEqual(resolve(reversed_url).func,views.edit_feed)
    
    def test_feeds_detail_url(self):
        url = 'feeds-api:feed-details'
        reversed_url = reverse(url,args=['9812-3ehj9-238d39-8hd23h'])
        self.assertEqual(resolve(reversed_url).func,views.feed_details)
    
    def test_feeds_refeed_url(self):
        url = 'feeds-api:feed-share'
        reversed_url = reverse(url)
        self.assertEqual(resolve(reversed_url).func,views.refeed)

    def test_feeds_vote_url(self):
        url = 'feeds-api:posts-vote'
        reversed_url = reverse(url)
        self.assertEqual(resolve(reversed_url).func,views.update_vote)

    def test_feeds_delete_url(self):
        url = 'feeds-api:delete-feed'
        reversed_url = reverse(url,args=['9812-3ehj9-238d39-8hd23h'])
        self.assertEqual(resolve(reversed_url).func,views.delete_feed)

    def test_feeds_comments_url(self):
        url = 'feeds-api:feed-comments'
        reversed_url = reverse(url,args=['9812-3ehj9-238d39-8hd23h'])
        self.assertEqual(resolve(reversed_url).func,views.feed_comments)
