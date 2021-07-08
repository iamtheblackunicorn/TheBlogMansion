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
    return render(
      request,
      'posts/post.html',
      {
        'title': title,
        'body': body
      }
    )
