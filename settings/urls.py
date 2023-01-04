from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from apps.musics import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main),
    path('create-music/', views.music),
    path('create-genre/', views.genre),
    path('create-author/', views.author)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
