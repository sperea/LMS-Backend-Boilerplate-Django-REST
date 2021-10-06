# backend/urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('djoser.urls.authtoken')),
    path('accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls),
    path('courses/', include('framework.routers.courses')),
]