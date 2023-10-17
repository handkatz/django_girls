from django.contrib.auth.models import User
from django.shortcuts import render
from django.utils import timezone
from . models import Post

def post_list(request):
    posts = Post.objects.all()
    # user = request.user.id
    # posts = Post.objects.filter(author=user)
    return render(request, 'blog/post_list.html', {'posts': posts})

