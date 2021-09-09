from django.db import models

# Create your models here.
class Users(models.Model):
 name = models.CharField(max_length=70)
 workname = models.CharField(max_length=200 ,null='TRUE')
 remark = models.CharField(max_length=70 ,null='TRUE')
