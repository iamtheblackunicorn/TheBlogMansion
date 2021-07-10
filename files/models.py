# "THE BLOG MANSION" A.K.A. "THE MANSION"
# BY THE BLACK UNICORN. LICENSED UNDER THE MIT
# LICENSE.

from django.db import models

class UserFile(models.Model):
    userAsset = models.FileField(upload_to='files')
    alias = models.CharField(max_length=100)
    assetAuthCode = models.CharField(max_length=16)
