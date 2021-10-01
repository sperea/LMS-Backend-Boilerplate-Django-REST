from django.shortcuts import render
from django.contrib.auth import get_user_model

from rest_framework import generics
from rest_framework import permissions

from . import serializers

CustomUser = get_user_model()

class UserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = serializers.CustomUserRetrieveSerializer
    permission_classes = (permissions.IsAuthenticated,)


    def get_object(self):
        return self.request.user

