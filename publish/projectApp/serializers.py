from rest_framework import serializers
from .models import User, userMadeList, Item

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class userMadeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = userMadeList
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'