from django.contrib.auth import login, logout,authenticate
from django.shortcuts import redirect, render
from django.contrib import messages
from .models import Student, Teacher, User
from django.views.generic import CreateView
from .forms import StudentSignUpForm, TeacherSignUpForm
from django.contrib.auth.forms import AuthenticationForm
from .models import User

def index(request):
    if request.user.is_authenticated :
        if request.user.is_student:
           """" if logged in user is a student then we fetch his data from student table """
           data = Student.objects.filter(user = request.user)
           return render(request, 'index.html', {'dataval': data})

        elif request.user.is_teacher:
            """ if logged in user is a teacher then we fetch his data from teacher table"""
            data = Teacher.objects.filter(user = request.user)
            return render(request, 'index.html', {'dataval': data})
        else:
            return render(request, 'index.html')
    return render(request, 'index.html')


def register(request):
    return render(request, 'register.html')



class customer_register(CreateView):
    model = User
    form_class = StudentSignUpForm
    template_name = 'student_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')



class employee_register(CreateView):
    model = User
    form_class = TeacherSignUpForm
    template_name = 'teacher_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')



def login_request(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None :
                login(request,user)
                return redirect('/')
            else:
                messages.error(request,"Invalid username or password")
        else:
                messages.error(request,"Invalid username or password")
    return render(request, 'login.html',
    context={'form':AuthenticationForm()})

def logout_view(request):
    logout(request)
    return redirect('/')

def logout_view(request):
    logout(request)
    return redirect('/')