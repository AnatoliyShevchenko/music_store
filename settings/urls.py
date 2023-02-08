from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from apps.auths import views as au_views
from apps.musics.views import (
    MainView, 
    MusicView,
    GenreView,
    AuthorView,
    TempView,
    RegView
)
from apps.auths.views import RegistrationView, LoginView, ProfileView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainView.as_view()),
    path('music/', MusicView.as_view()),
    path('genres/', GenreView.as_view()),
    path('authors/', AuthorView.as_view()),
    path('temp/', TempView.as_view()),
    path('reg/', RegistrationView.as_view()),
    path('login/', LoginView.as_view()),
    path('login/profile/', ProfileView.as_view()),
    path('activate/<str:code>/', au_views.activate_user)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(
    settings.MEDIA_URL, 
    document_root=settings.MEDIA_ROOT
)

if settings.DEBUG:
    urlpatterns += [
        path('__debug__/', include('debug_toolbar.urls')),
    ]