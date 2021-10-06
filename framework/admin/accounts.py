from django.contrib import admin
from accounts.models import *


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['email']
    list_filter = ['email']
    search_fields = ['email']


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['user', 'code']
    list_filter = ['user', 'code']
    search_fields = ['user', 'code']


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['user', 'code']
    list_filter = ['user', 'code']
    search_fields = ['user', 'code']