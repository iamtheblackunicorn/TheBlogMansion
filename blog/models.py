# "THE BLOG MANSION" A.K.A. "THE MANSION"
# BY THE BLACK UNICORN. LICENSED UNDER THE MIT
# LICENSE.

from django.db import models
class Post(models.Model):
    title = models.CharField(max_length=2000)
    body = models.TextField(max_length=5000000)
    description = models.CharField(max_length=2000)
    date = models.DateTimeField(auto_now=True)
    banner = models.ImageField(upload_to='blog')
    def __str__(self):
        return self.title
