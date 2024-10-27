from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets,status
from .models import User, UserItemList, Item, Entry
from .serializers import UserSerializer, UserItemListSerializer, ItemSerializer, EntrySerializer


# Create your views here.
def homepage(request):
    return render(request, 'homepage.html')

# Create your views here.
@api_view(['GET'])
def get_users(request):
    if not request.user.is_admin:
        return Response({"error": "Permission denied. Admins only."}, status=status.HTTP_403_FORBIDDEN)
    users=User.objects.all()
    serializer =UserSerializer(users, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

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


@api_view(['GET','PUT','PATCH','DELETE'])
def user_detail(request,pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    logged_in_user_id= request.headers.get("User-Id")
    if request.method in ['PUT','PATCH','DELETE'] and logged_in_user_id and int(logged_in_user_id) != int(user.id):
        return Response({"error": "You can only update your own profile"}, status=status.HTTP_403_FORBIDDEN)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method in ['PUT','PATCH']:
        if 'username' in request.data or 'image' in request.data:
            partial = True if request.method == 'PATCH' else False
            serializer = UserSerializer(user, data=request.data,partial=partial, fields=['username','image'])
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"Error":"Invalid fields for update"}, status=status.HTTP_400_BAD_REQUEST)
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
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def create_user_item_list(request):
    serializer= UserItemListSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','PATCH','DELETE'])
def user_item_list_detail(request,pk):
    try:
        user_item_list = UserItemList.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserItemListSerializer(user_item_list)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method in ['PUT','PATCH']:
        partial = True if request.method == 'PATCH' else False
        serializer = UserItemListSerializer(user_item_list, data=request.data,partial=partial)
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

# @api_view(['GET'])
# def get_items(request):
#     items=Item.objects.all()
#     serializer =ItemSerializer(items, many=True)
#     return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def create_item(request):
    serializer= ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','PATCH','DELETE'])
def item_detail(request,pk):
    try:
        item = Item.objects.get(pk=pk)
    except Item.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ItemSerializer(item)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method in ['PUT','PATCH']:
        partial = True if request.method == 'PATCH' else False
        serializer = ItemSerializer(item, data=request.data,partial=partial)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)  

@api_view(['GET'])
def get_items_by_list_id(request, list_id):
    try:
        list_obj = UserItemList.objects.get(pk=list_id)
    except UserItemList.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    user_id= request.headers.get('User-Id')
    is_admin = request.headers.get('is_admin') == 'true'
    try:
        if( not list_obj.is_public and not is_admin and int(user_id) != int(list_obj.user.id)):
            return Response({"detail":f"Access Denied, {list_id} or {is_admin} or {type(user_id)} / {int(list_obj.user.id)}"}, status=status.HTTP_404_NOT_FOUND)
    except:
        return Response({"detail":"Access Failed "}, status=status.HTTP_409_CONFLICT)
    entries=Entry.objects.filter(list_id=list_id)
    if not entries.exists():
        return Response('Error : No items found in this list', status=status.HTTP_404_NOT_FOUND)
    items_id= entries.values_list('item_id',flat=True)
    items = Item.objects.filter(item_id__in=items_id)
    serializer =ItemSerializer(items, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def create_entry(request, list_id):
    try:
        list_obj = UserItemList.objects.get(pk=list_id)
    except UserItemList.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    item_id= request.data.get('item')
    try:
        item_obj = Item.objects.get(pk=item_id)
    except Item.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    info={'list':list_obj.list_id, "item":item_obj.item_id}
    serializer= EntrySerializer(data=info)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','PATCH','DELETE'])
def entry_detail(request, pk):
    try:
        entry = Entry.objects.get(pk=pk)
    except Entry.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = EntrySerializer(entry)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method in ['PUT','PATCH']:
        partial = True if request.method == 'PATCH' else False
        serializer = EntrySerializer(entry, data=request.data,partial=partial)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        entry.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET'])
def get_lists_by_user_id(request, user_id):
    lists=UserItemList.objects.filter(user_id=user_id)
    if not lists.exists():
        return Response('Error : No lists found for this user', status=status.HTTP_404_NOT_FOUND)
    serializer =UserItemListSerializer(lists, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_items(request):
    name = request.query_params.get('name',None)
    if name:
        items = Item.objects.filter(name__icontains=name)
    else:
        items = Item.objects.all()
    serializer =ItemSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def admin_create_user(request):
    if not request.user.is_admin:
        return Response({"error": "Permission denied. Admins only."}, status=status.HTTP_403_FORBIDDEN)    
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def admin_delete_user(request, pk):
    if not request.user.is_admin:
        return Response({"error": "Permission denied. Admins only."}, status=status.HTTP_403_FORBIDDEN)
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['PATCH'])
def admin_update_user(request, pk):
    if not request.user.is_admin:
        return Response({"error": "Permission denied. Admins only."}, status=status.HTTP_403_FORBIDDEN)
    try:
        user = User.objects.get(pk=pk)
    except:
        return Response ({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
    serializer = UserSerializer(user, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status= status.HTTP_404_BAD_REQUEST)


@api_view(['POST'])
def user_login(request):
    email = request.data.get('email')
    try:
        # Check if user exists by email
        user = User.objects.get(email=email)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except User.DoesNotExist:
        # Create user if not found
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def is_admin(request):
    if request.user.is_admin:
        return Response({"is_admin": request.user.is_admin}, status= status.HTTP_200_OK)
    else:
        return Response({"error": "User not authenticated"}, status= status.HTTP_401_UNAUTHORIZED)