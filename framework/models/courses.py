import os
import uuid

from django.db import models
from accounts.models import Student
from accounts.models import Teacher

import cloudinary


class CourseORM(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=150)
    slug = models.SlugField(db_index=True, max_length=150)
    code = models.CharField(max_length=6, default=uuid.uuid4().hex.upper()[0:6], blank=True, verbose_name="Code")
    image = cloudinary.models.CloudinaryField('image', null=True, blank=True)
    #image = models.ImageField(null=True, blank=True, upload_to='courses_images')
    description = models.TextField()
    teacher = models.ForeignKey(Teacher, on_delete=models.PROTECT)
    students = models.ManyToManyField(Student)
    


    def __str__(self):
        return self.name

    class Meta:
        app_label="courses"


class ModuleORM(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    order = models.PositiveIntegerField(default=1)
    course = models.ForeignKey(CourseORM, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        app_label="courses"


class SectionORM(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    order = models.PositiveIntegerField(default=1)
    module = models.ForeignKey(ModuleORM, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        app_label="courses"


class TopicORM(models.Model):
    TOPIC_TYPE_GENERAL = 1
    TOPIC_TYPE_HOMEWORK = 2
    TOPIC_TYPE_QUIZ = 2

    TOPIC_TYPE_CHOICES = (
        (TOPIC_TYPE_GENERAL, 'General'),
        (TOPIC_TYPE_HOMEWORK, 'Homework'),
        (TOPIC_TYPE_QUIZ, 'Quiz'),
    )

    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    order = models.PositiveIntegerField(default=1)
    type = models.SmallIntegerField(choices=TOPIC_TYPE_CHOICES, default=TOPIC_TYPE_GENERAL, verbose_name='Type')
    section = models.ForeignKey(SectionORM, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        app_label="courses"


def get_resource_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join("resources/", filename)

    class Meta:
        app_label="courses"


class ResourcesORM(models.Model):
    topic = models.ForeignKey(TopicORM, on_delete=models.CASCADE)
    resource = models.FileField(upload_to=get_resource_file_path, verbose_name="File")

    class Meta:
        app_label="courses"


class PackageORM(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=150)
    slug = models.SlugField(db_index=True, max_length=150)
    code = models.CharField(max_length=10)
    parent = models.ForeignKey('PackageORM', on_delete=models.CASCADE)
    courses = models.ManyToManyField(CourseORM)

    def __str__(self):
        return self.name

    class Meta:
        app_label="courses"