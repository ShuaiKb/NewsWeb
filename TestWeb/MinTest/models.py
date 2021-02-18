from django.db import models

# Create your models here.
class User(models.Model):
    password = models.CharField(max_length=256, default="")
    username = models.CharField(max_length=64, default="")
    userinfo = models.CharField(max_length=128, default='')
    email= models.CharField(max_length=128, default='')
    mobile = models.CharField(max_length=128, default='')
    admin = models.BooleanField(default='False')

class Classes(models.Model):
    name =models.CharField(max_length=64, default="")

class News(models.Model):
    title = models.CharField(max_length=255, default="")
    time = models.CharField(max_length=64, default="")
    content = models.CharField(max_length=256, default="")
    img = models.CharField(max_length=256, default="")
    author = models.CharField(max_length=11, default="")
    classes = models.CharField(max_length=11, default="")
    shenhe = models.BooleanField(default='False')

class Message(models.Model):
    name = models.CharField(max_length=64, default="")
    img = models.CharField(max_length=256, default="")
    time = models.CharField(max_length=64, default="")
    content = models.CharField(max_length=256, default="")
    classes = models.CharField(max_length=64, default="")