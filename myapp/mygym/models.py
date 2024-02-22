from django.db import models
from django.contrib.auth.models import User
class Member(models.Model):
    user=models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    username=models.CharField(max_length=20)
    email=models.EmailField()
    phone=models.IntegerField()
    comment=models.TextField(max_length=200)
    classes=models.CharField(max_length=20)
    full_name=models.CharField(max_length=25)
    def __str__(self):
        return self.username
class queries(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    comment=models.TextField(max_length=200)
    def __str__(self):
        return self.name
    
