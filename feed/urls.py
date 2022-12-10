from django.urls import path
from . import views

app_name = 'feeds-api'

urlpatterns = [
     path('', views.feeds, name="feeds"),
     path('create/', views.create_feed, name="feed-create"),
     path('edit/<str:pk>/', views.edit_feed, name="feed-edit"),
     path('details/<str:pk>/', views.feed_details, name="feed-details"),
     path('share/', views.refeed, name="feed-share"),
     path('vote/', views.update_vote, name="posts-vote"),
     path('delete/<str:pk>/', views.delete_feed, name="delete-feed"),
     path('<str:pk>/comments/', views.feed_comments, name="feed-comments"),
]