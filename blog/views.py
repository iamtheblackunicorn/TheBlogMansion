# "THE BLOG MANSION" A.K.A. "THE MANSION"
# BY THE BLACK UNICORN. LICENSED UNDER THE MIT
# LICENSE.

from django.shortcuts import render
from .models import Post

def public(request):
    posts = Post.objects.all()
    return render(
      request,
      'posts/overview.html',
      {
        'posts':posts
      }
    )
def single(request, pk):
    post = Post.objects.get(pk=pk)
    title = post.title
    body = post.body
    banner = post.banner
    description = post.description
    date = post.date
    author = post.author
    return render(
      request,
      'posts/post.html',
      {
        'title': title,
        'body': body,
        'banner': banner,
        'description': description,
        'date': date,
      }
    )
def api(request):
    posts = Post.objects.all()
    return render(
      request,
      'posts/api.html',
      {
        'posts':posts
      }
    )
