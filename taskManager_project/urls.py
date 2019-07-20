from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('pages.urls')),
    path('admin/', admin.site.urls),
    path('notes/', include('notes.urls')),
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),
]
