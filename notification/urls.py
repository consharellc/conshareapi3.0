from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_notifications, name="get-notifications"),
    path('<str:pk>/read/',views.read_notification,name='read-notification'),
]
