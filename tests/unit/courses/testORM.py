from django.test import TestCase
from accounts.models import *
from framework.models.courses import *


class CourseORMTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        CustomUser(email = "prueba@prueba.com").save()
        users = CustomUser.objects.all()
        user_from_db = users[0]
        Teacher.objects.create(user=user_from_db)
        pass


    def test_Topic_ORM_creation(self):
        new_teacher = Teacher.objects.all()[0]
        CourseORM(name = "prueba",
            slug = "prueba",
            description = "prueba",
            teacher = new_teacher).save()
        ModuleORM(
            title = "prueba",
            description = "prueba",
            course = CourseORM.objects.all()[0]
        ).save()
        SectionORM(
            title = "prueba",
            description = "prueba",
            module = ModuleORM.objects.all()[0]
        ).save()
        TopicORM(
            title = "prueba",
            description = "prueba",
            type = 1,
            section = SectionORM.objects.all()[0]
        ).save()
        courses = CourseORM.objects.all()
        self.assertEquals(courses.count(), 1)
        modules = ModuleORM.objects.all()
        self.assertEquals(modules.count(), 1)
        sections = SectionORM.objects.all()
        self.assertEquals(sections.count(), 1)
        topics = TopicORM.objects.all()
        self.assertEquals(topics.count(), 1)


