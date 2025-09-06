from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import User
# Create your views here.
def is_admin(u):return u.role == u.Role.ADMIN
def is_student(u): return u.role == u.Role.STUDENT



@login_required
def welcome(request):
    if request.user.role == User.Role.ADMIN:
        return render(request,'welcomest.html')
    else:
        return render(request,'welcome.html')
    

