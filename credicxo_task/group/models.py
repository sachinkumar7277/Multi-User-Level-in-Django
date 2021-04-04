from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    email = models.EmailField(default='your@email.com')


class Student(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    email = models.EmailField(default='your@email.com')
    location = models.CharField(max_length=20)
    Branch = models.CharField(max_length=100, default='Null')
    phone_number = models.CharField(max_length=20,default='hmko nhi pta')

    def __str__(self):
        return self.user.username

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    email = models.EmailField(default='your@email.com')
    Department = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20, default='humko nhi pta')
    def __str__(self):
        return self.user.username