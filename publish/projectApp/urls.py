from django.urls import path,include
from . import views
from .views import  user_login,admin_create_user, admin_delete_user, admin_update_user,get_users, create_user, user_detail,get_items, create_item, item_detail, get_user_item_list, create_user_item_list, user_item_list_detail,create_entry, get_items_by_list_id, entry_detail, get_lists_by_user_id 
urlpatterns = [
    path('', views.homepage),
    path('users/',get_users,name='get_user'),
    path('users/create/',create_user,name='create_user'),
    path('users/<int:pk>',user_detail,name='user_detail'),
    path('users/<int:user_id>/lists',get_lists_by_user_id,name='get_lists_by_user'),

    path('items/',get_items,name='get_items'),
    path('items/create/',create_item,name='create_item'),
    path('items/<int:pk>',item_detail,name='item_detail'),

    path('user_item_list/',get_user_item_list,name='get_user_item_list'),
    path('user_item_list/create/',create_user_item_list,name='create_user_item_list'),
    path('user_item_list/<int:pk>',user_item_list_detail,name='user_item_list_detail'),

    path('user_item_list/<int:list_id>/add-item',create_entry,name='add_item_to_list'),
    path('user_item_list/<int:list_id>/list-items',get_items_by_list_id,name='get_items_by_list'),
    path('entries/<int:pk>',entry_detail,name='entry_detail'),

    path('users/login/', user_login, name='user_login'),
    path('admin/users/create/', admin_create_user, name='admin_create_user'),
    path('admin/users/<int:pk>/update/', admin_update_user, name='admin_update_user'),
    path('admin/users/<int:pk>/delete/', admin_delete_user, name='admin_delete_user')

]