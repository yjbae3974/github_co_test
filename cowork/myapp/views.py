from django.shortcuts import render
from .models import Post
from django.shortcuts import render, get_object_or_404


def list(request):
    posts = Post.objects.all()
    return render(request, 'list.html', {'posts': posts})

