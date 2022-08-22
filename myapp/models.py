from django.db import models
import email

# Create your models here.

class User(models.Model):
    Username=models.CharField(max_length=50)
    Email=models.EmailField(max_length=50)
    Contact=models.CharField(max_length=10)
    Messages=models.CharField(max_length=50)
    # is_active=models.CharField(max_length=50,default=0)

class User11(models.Model):
    Username=models.CharField(max_length=50)
    Email=models.EmailField(max_length=50)
    Contact=models.CharField(max_length=10)
    Messages=models.CharField(max_length=50)
    # is_active=models.CharField(max_length=50,default=0)


class UploadFile(models.Model):
    Resume=models.FileField(max_length=100)


class resumefile(models.Model):
    id=models.AutoField(primary_key=True)
    file_name=models.CharField(max_length=255)
    file=models.FileField(max_length=100)
    



