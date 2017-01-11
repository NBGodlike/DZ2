from django.db import models
from django.contrib.auth.models import User



class User(models.Model):
    first_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=False)
    username = models.CharField(max_length=255, null=False, default='login')
    password = models.CharField(max_length=255, null=False, default='12345')
    Phone_number = models.CharField(max_length=255, null=True)


class Luser(models.Model):
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    username = models.CharField(max_length=255, null=False, default='login')
    password = models.CharField(max_length=255, null=False, default='12345')
    Phone_number = models.CharField(max_length=255, null=True)


class Course(models.Model):
    name = models.TextField(max_length=255, null=True)
    duration = models.TextField(max_length=255, null=True)
    teacher = models.TextField(max_length=255, null=True)
    value = models.TextField(max_length=255, null=True)
    picture = models.ImageField(upload_to='css2/', null=True)
    lusers = models.ManyToManyField(Luser)



class Comment(models.Model):
    Course = models.TextField(max_length=255, null=False)
    Text = models.TextField(max_length=255, null=False)



