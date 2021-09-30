from django.urls import include
from django.urls import path

from rest_framework import routers

from . import views
from . import viewsets

router = routers.DefaultRouter()
router.register('', viewsets.CustomUserModelViewSet)

urlpatterns = [
    path('data/', views.UserRetrieveUpdateDestroyAPIView.as_view(),
         name='user-data'),
    path('users/', include(router.urls)),
]