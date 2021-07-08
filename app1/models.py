from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class customuser(models.Model):
    # userdata=models.OneToOneField(User,on_delete=models.CASCADE)
    mobile=models.CharField(max_length=16,default='none')
    otp=models.CharField(max_length=10,default='none')