from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from .models import User, userMadeList, Item
from .serializers import UserSerializer, userMadeListSerializer, ItemSerializer


# Create your views here.
def homepage(request):
    return render(request, 'homepage.html')

# Create your views here.
@api_view(['GET'])
def getUser(request):
    return Response(UserSerializer({
    "id": 1,
    "name": "John Doe",
    "email": "john.doe@example.com",
    "username": "johndoe",
    "image": "https://example.com/images/johndoe.jpg",
    "is_admin": True
}
).data)

def getUserMadeList(request):
    return Response(UserSerializer({
    "list_id": 1001,
    "user": {
        "id": 1,
        "name": "John Doe",
        "username": "johndoe"
    },
    "item": {
        "item_id": 101,
        "name": "Wireless Headphones"
    },
    "list_name": "John's Wishlist"
}
).data)

def getItem(request):
    return Response(UserSerializer({
    "item_id": 101,
    "price": 1999,
    "name": "Wireless Headphones",
    "url": "https://example.com/products/wireless-headphones",
    "image": "https://example.com/images/wireless-headphones.jpg",
    "description": "High-quality wireless headphones with noise-cancelling features."
}
).data)