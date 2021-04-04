from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import Group
from django.db import transaction
from .models import User, Student,Teacher


class StudentSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    Branch = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)
    location = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.email = self.cleaned_data.get('email')
        user.save()
        group = Group.objects.get(name = 'Student')
        user.groups.add(group)
        student = Student.objects.create(user=user)
        student.phone_number = self.cleaned_data.get('phone_number')
        student.location = self.cleaned_data.get('location')
        student.Branch = self.cleaned_data.get('Branch')
        student.email = self.cleaned_data.get('email')
        student.save()
        return user


class TeacherSignUpForm(UserCreationForm):
    phone_number = forms.CharField(required=True)
    Department = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_teacher = True
        user.is_active = True
        user.is_staff = True
        user.email = self.cleaned_data.get('email')
        group = Group.objects.get(name = 'Teacher')
        print(group)
        user.save()
        user.groups.add(group)
        teacher = Teacher.objects.create(user=user)
        teacher.phone_number = self.cleaned_data.get('phone_number')
        teacher.Department = self.cleaned_data.get('Department')
        teacher.email = self.cleaned_data.get('email')
        teacher.save()
        return user