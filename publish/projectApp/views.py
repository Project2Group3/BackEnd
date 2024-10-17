from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets,status
from .models import User, UserItemList, Item
from .serializers import UserSerializer, UserItemListSerializer, ItemSerializer


# Create your views here.
def homepage(request):
    return render(request, 'homepage.html')

# Create your views here.
@api_view(['GET'])
def get_users(request):
    users=User.objects.all()
    serializer =UserSerializer(users, many=True)
    return Response(serializer.data)

# @api_view(['GET'])
# def get_user(request):
#     return Response(UserSerializer({
#     "id": 1,
#     "name": "John Doe",
#     "email": "john.doe@example.com",
#     "username": "johndoe",
#     "image": "https://example.com/images/johndoe.jpg",
#     "is_admin": True
# }
# ).data)

@api_view(['POST'])
def create_user(request):
    serializer= UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def user_detail(request,pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

#USER Item List 

# @api_view(['GET'])
# def getUserItemList(request):
#     user = User(id=1, name="John Doe", username="johndoe")  # Creating a mock user object
#     item = Item(itemId=101, name="Wireless Headphones")  # Creating a mock item object
#     return Response(UserItemListSerializer({
#     "list_id": 11, 
#     "user": user,
#     "item": item,
#     "list_name": "John's Wishlist"
# }
# ).data)

@api_view(['GET'])
def get_user_item_list(request):
    user_item_lists=UserItemList.objects.all()
    serializer =UserItemListSerializer(user_item_lists, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_user_item_list(request):
    serializer= UserItemListSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def user_item_list_detail(request,pk):
    try:
        user_item_list = UserItemList.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserItemListSerializer(user_item_list)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = UserItemListSerializer(user_item_list, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        user_item_list.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#Items 

# @api_view(['GET'])
# def getItem(request):
#     return Response(ItemSerializer({
#     "item_id": 101,
#     "price": 1999,
#     "name": "Wireless Headphones",
#     "url": "https://example.com/products/wireless-headphones",
#     "image": "https://example.com/images/wireless-headphones.jpg",
#     "description": "High-quality wireless headphones with noise-cancelling features."
# }
# ).data)

@api_view(['GET'])
def get_items(request):
    items=Item.objects.all()
    serializer =ItemSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_item(request):
    serializer= ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def item_detail(request,pk):
    try:
        item = Item.objects.get(pk=pk)
    except Item.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ItemSerializer(item)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)