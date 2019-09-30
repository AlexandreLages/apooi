from django.contrib import admin
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url('', include('front.urls')),
    url('', include('back.urls')),
    url('', include('usuario.urls')),
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG == False:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)