from django.urls import path
from . import views

app_name = 'conshare-api-discussions'


urlpatterns = [
    path('',views.discussions,name='discussions'),
    path('create/',views.create_discussion,name='create_discussion'),
    path('vote/',views.update_vote,name='discussion_vote'),
    path('<str:pk>/', views.get_discussion, name="get_discussion"),
    path('edit/<str:pk>/', views.edit_discussion, name="edit_discussion"),
    path('delete/<str:pk>/', views.delete_discussion, name="delete_discussion"),
    path('edit-comment/<str:pk>/', views.edit_discussion_comment, name="edit_discussion_comment"),
    path('delete-comment/<str:pk>/', views.delete_discussion_comment, name="delete_discussion_comment"),
]
