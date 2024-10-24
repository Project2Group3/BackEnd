from django.db import models

# Create your models here.
class User(models.Model):
    name= models.CharField(max_length=250)
    email= models.CharField(max_length=250)
    username= models.CharField(max_length=250)
    image= models.CharField(max_length=250,null=True, blank=True)
    is_Admin = models.BooleanField(default=False)
    id= models.AutoField(primary_key=True)
    def __str__(self):
        return self.username


class UserItemList(models.Model):
    user= models.ForeignKey('User', on_delete=models.CASCADE)
    item= models.ForeignKey('Item', on_delete=models.CASCADE)
    list_name = models.CharField(max_length=250)
    listId= models.AutoField(primary_key=True)
    def __str__(self):
        return self.listName


class Item(models.Model):
    itemId= models.AutoField(primary_key=True)
    price= models.FloatField()
    name = models.CharField(max_length=250)
    url = models.CharField(max_length=250)
    image = models.CharField(max_length=250, null=True, blank=True)
    description = models.CharField(max_length=250, null=True, blank=True)
    def __str__(self):
        return self.name
