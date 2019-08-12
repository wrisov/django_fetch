from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

posts = [
    {
        'author' : 'AB CDEF',
        'title' : 'Blog post 1',
        'content' : 'Content',
        'date_posted':'August 27, 2019'
    },
    {
        'author' : 'JK LMON',
        'title' : 'Blog post 2',
        'content' : 'Content 2',
        'date_posted':'July 27, 2019'
    },
    

]

def home(request) :
   context = {
       'posts':Post.objects.all()
   }
   return render(request,'blog/home.html',context)


def about(request) :
    return render(request,'blog/about.html')  

# Create your views here.s
