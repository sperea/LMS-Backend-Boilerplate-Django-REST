from django.test import TestCase
from accounts.models import *


class UserModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        CustomUser(email = "prueba@prueba.com").save()
        pass

    def test_user_creation(self):
        users = CustomUser.objects.all()
        self.assertEquals(users.count(), 1)
        user_from_db = users[0]
        self.assertEquals(user_from_db.email, "prueba@prueba.com")

    def test_student_creation(self):
        users = CustomUser.objects.all()
        self.assertEquals(users.count(), 1)
        user_from_db = users[0]
        Student.objects.create(user=user_from_db)
        students = Student.objects.all()
        self.assertEquals(students.count(), 1)

    def test_teacher_creation(self):
        users = CustomUser.objects.all()
        self.assertEquals(users.count(), 1)
        user_from_db = users[0]
        Teacher.objects.create(user=user_from_db)
        teachers = Teacher.objects.all()
        self.assertEquals(teachers.count(), 1)