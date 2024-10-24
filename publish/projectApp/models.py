from django.db import models

# Create your models here.
class User(models.Model):
    id= models.AutoField(primary_key=True)
    name= models.CharField(max_length=250)
    email= models.CharField(max_length=250)
    username= models.CharField(max_length=250)
    image= models.CharField(max_length=250,null=True, blank=True)
    is_admin = models.BooleanField(default=False)
    def __str__(self):
        return self.username
    class Meta:
        db_table = 'User'  
class UserItemList(models.Model):
    list_id= models.AutoField(primary_key=True)
    user= models.ForeignKey('User', on_delete=models.CASCADE)
    list_name = models.CharField(max_length=250)
    is_public = models.BooleanField(default=False)
    def __str__(self):
        return self.list_name
    class Meta:
        db_table = 'user_list'  


class Item(models.Model):
    item_id= models.AutoField(primary_key=True)
    price= models.FloatField()
    name = models.CharField(max_length=250)
    url = models.CharField(max_length=250)
    image = models.CharField(max_length=250, null=True, blank=True)
    description = models.CharField(max_length=250, null=True, blank=True)
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'Item'  

class Entry(models.Model):
    entry= models.AutoField(primary_key=True)
    list=models.ForeignKey('UserItemList', on_delete=models.CASCADE)
    item =models.ForeignKey('Item', on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.list.list_name} - {self.item.name}"
    class Meta:
        db_table = 'entries'