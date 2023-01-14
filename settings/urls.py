from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from apps.musics import views
from apps.auths import views as au_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main),
    path('create-music/', views.music),
    path('create-genre/', views.genre),
    path('create-author/', views.author),
    path('activate/<str:code>/', au_views.activate_user)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += [
        path('__debug__/', include('debug_toolbar.urls')),
    ]