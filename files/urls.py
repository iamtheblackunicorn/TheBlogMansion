# "THE BLOG MANSION" A.K.A. "THE MANSION"
# BY THE BLACK UNICORN. LICENSED UNDER THE MIT
# LICENSE.

from django.conf.urls import url
from django.urls import path
from .views import *

app_name = 'files'

urlpatterns = [
  path('assets', authorize, name='auth'),
  path('asset/<str:authCode>', download, name='download')
]
