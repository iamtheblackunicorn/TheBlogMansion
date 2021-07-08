# "THE BLOG MANSION" A.K.A. "THE MANSION"
# BY THE BLACK UNICORN. LICENSED UNDER THE MIT
# LICENSE.

from django.shortcuts import render
from .models import Post

def public(request):
    posts = Post.objects.all()
    return render(
      request,
      'blog/overview.html',
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
    duration = str(round(len(body.split(' '))/250, 0)).split('.')[0]
    if duration == '0':
        duration = '1'
    else:
        pass
    return render(
      request,
      'blog/post.html',
      {
        'title': title,
        'body': body,
        'banner': banner,
        'description': description,
        'date': date,
        'duration': duration
      }
    )
def api(request):
    posts = Post.objects.all()
    return render(
      request,
      'blog/api.html',
      {
        'posts':posts
      }
    )
