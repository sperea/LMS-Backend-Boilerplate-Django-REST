from django.contrib import admin
from ..models import *


class ModuleInline(admin.StackedInline):
    model = ModuleORM

class SectionInline(admin.StackedInline):
    model = SectionORM

class Topicline(admin.StackedInline):
    model = TopicORM

@admin.register(CourseORM)
class CourseORMAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'code']
    list_filter = ['name']
    search_fields = ['name', 'slug', 'code']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ModuleInline]


@admin.register(ModuleORM)
class ModuleORMAdmin(admin.ModelAdmin):
    list_display = ['title', 'order', 'course']
    list_filter = ['title']
    search_fields = ['title', 'order', 'course']
    inlines = [SectionInline]

@admin.register(SectionORM)
class SectionORMAdmin(admin.ModelAdmin):
    list_display = ['title', 'order', 'module']
    list_filter = ['title']
    search_fields = ['title', 'order', 'module']
    inlines = [Topicline]


@admin.register(TopicORM)
class TopicORMAdmin(admin.ModelAdmin):
    list_display = ['title', 'order', 'section']
    list_filter = ['title']
    search_fields = ['title', 'order', 'section']

@admin.register(ResourcesORM)
class ResourcesORMAdmin(admin.ModelAdmin):
    list_display = ['topic', 'resource']
    list_filter = ['topic']
    search_fields = ['topic', 'resource']