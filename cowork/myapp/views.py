from django.shortcuts import render
from .models import Post
from django.shortcuts import render, get_object_or_404
from myapp import models

def list(request):
    posts = Post.objects.all()
    return render(request, 'list.html', {'posts': posts})


# Create your views here.
def detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    
    return render(request, 'detail.html', {'post':post})
