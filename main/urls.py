from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include

from main import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('menu.urls',namespace='menu')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
