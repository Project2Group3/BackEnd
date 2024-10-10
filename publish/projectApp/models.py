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


class userMadeList(models.Model):
    userId= models.ForeignKey('User', on_delete=models.CASCADE)
    itemId= models.ForeignKey('Item', on_delete=models.CASCADE)
    listName = models.CharField(max_length=250)
    listId= models.AutoField(primary_key=True)
    def __str__(self):
        return self.listName


class Item(models.Model):
    itemId= models.AutoField(primary_key=True)
    price= models.IntegerField(max_length=64)
    name = models.CharField(max_length=250)
    url = models.CharField(max_length=250)
    image = models.CharField(max_length=250, null=True, blank=True)
    description = models.CharField(max_length=250, null=True, blank=True)
    def __str__(self):
        return self.name
