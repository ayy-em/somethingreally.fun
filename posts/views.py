from django.shortcuts import render

from .models import Post


def index(request):
    posts = Post.objects.all()
    context = {
        'title': 'SR.f - Fresh Posts',
        'posts': posts
    }

    return render(request, 'blog/blog-related/blog-main.html', context)


def details(request, postnum):
    post = Post.objects.get(id=postnum)
    context = {
        'post': post
    }

    return render(request, 'blog/blog-related/blog-post-details.html', context)
