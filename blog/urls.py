from django.conf.urls import url
from django.urls import path
from .views import *

app_name = 'posts'

urlpatterns = [
  url(r'^$', public, name='overview'),
  path('post/<int:pk>', single, name='single'),
]
