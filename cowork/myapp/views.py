from django.shortcuts import render
from myapp import models
# Create your views here.
def detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    
    return render(request, 'detail.html', {'post':post})
