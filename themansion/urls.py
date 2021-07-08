# "THE BLOG MANSION" A.K.A. "THE MANSION"
# BY THE BLACK UNICORN. LICENSED UNDER THE MIT
# LICENSE.

from django.contrib import admin
from django.urls import include
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
