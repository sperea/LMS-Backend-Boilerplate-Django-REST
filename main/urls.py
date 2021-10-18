# backend/urls.py
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView


urlpatterns = [
    path('', include('djoser.urls.authtoken')),
    path('swagger-ui/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='swagger-ui'),
    path('accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls),
    path('courses/', include('framework.routers.courses')),

]