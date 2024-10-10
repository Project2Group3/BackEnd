from django.urls import path,include
from . import views
from .views import getUser, getItem, getUserMadeList
urlpatterns = [
    path('', views.homepage),
    path('users/',getUser,name='getUser'),
    path('items/',getItem,name='getItem'),
    path('userMadeList/',getUserMadeList,name='getUserMadeList')
]