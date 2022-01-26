from django.urls import path
from . import views

app_name = 'mumbles-api'

urlpatterns = [
     path('', views.mumbles, name="feeds"),
     path('create/', views.create_mumble, name="feed-create"),
     path('edit/<str:pk>/', views.edit_mumble, name="feed-edit"),
     path('details/<str:pk>/', views.mumble_details, name="feed-details"),
     path('share/', views.remumble, name="feed-share"),
     path('vote/', views.update_vote, name="posts-vote"),
     path('delete/<str:pk>/', views.delete_mumble, name="delete-mumble"),
     path('<str:pk>/comments/', views.mumble_comments, name="feed-comments"),
]