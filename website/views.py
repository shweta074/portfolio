from django.shortcuts import render,  HttpResponse
from django.views import generic
from blog.models import Post
# import requests

def index(request):
    blog = Post.objects.all()
    return render(request,template_name='website/index.html', context={"blogs": blog})

def assests(request):
    return render(request,template_name='website/assests')




    

  
     
     
