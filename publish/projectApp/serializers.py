from rest_framework import serializers
from .models import User, UserItemList, Item, Entry

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class UserItemListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserItemList
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class EntrySerializer(serializers.ModelSerializer):
    item = serializers.PrimaryKeyRelatedField(queryset=Item.objects.all()) 
    class Meta:
        model = Entry
        fields = '__all__'