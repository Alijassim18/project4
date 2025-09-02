from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
# Create your views here.
def welcome(request):
    return render(request,'welcome.html')


