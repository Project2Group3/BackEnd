from django.urls import path,include
from . import views
from .views import get_users, create_user, user_detail,get_items, create_item, item_detail, get_user_item_list, create_user_item_list, user_item_list_detail 
urlpatterns = [
    path('', views.homepage),
    path('users/',get_users,name='get_user'),
    path('users/create/',create_user,name='create_user'),
    path('users/<int:pk>',user_detail,name='user_detail'),

    path('items/',get_items,name='get_items'),
    path('items/create/',create_item,name='create_item'),
    path('items/<int:pk>',item_detail,name='item_detail'),

    path('user_item_list/',get_user_item_list,name='get_user_item_list'),
    path('user_item_list/create/',create_user_item_list,name='create_user_item_list'),
    path('user_item_list/<int:pk>',user_item_list_detail,name='user_item_list_detail'),

]