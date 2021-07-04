from django.shortcuts import render

from .models import Post


def index(request):
    posts = Post.objects.all()

    context = {
        'posts': posts
    }

    return render(request, 'blog/blog_list.html', context)


def detail(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, 'blog/blog_detail.html', {'post': post})
