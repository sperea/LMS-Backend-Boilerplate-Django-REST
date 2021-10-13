from accounts.models import *

from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.test import APITestCase
from framework.models.courses import *


class GetCourseTests(APITestCase):

    def setUp(self):
        self.user = CustomUser.objects.create_user(email='js@js.com', password='js.sj')
        self.refresh = RefreshToken.for_user(self.user)
        client = APIClient()
        response = client.post('/token/login/', {'email': 'js@js.com', 'password': 'js.sj'}, format='json')
        self.token = response.data["auth_token"]

    def test_get_course_by_code(self):
        Teacher.objects.create(user=self.user)
        new_teacher = Teacher.objects.all()[0]
        CourseORM(name = "prueba",
            slug = "prueba",
            code = "XXX",
            description = "prueba",
            teacher = new_teacher).save()
        
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'Token {self.token}')
        response = client.get('/courses/course-info/%s/' % ("XXX"), {}, format='json')
        assert response.status_code == 200

    def test_get_all_courses(self):
        Teacher.objects.create(user=self.user)
        new_teacher = Teacher.objects.all()[0]
        CourseORM(name = "prueba",
            slug = "prueba",
            code = "XXX",
            description = "prueba",
            teacher = new_teacher).save()
        
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'Token {self.token}')
        response = client.get('/courses/all-courses/', {}, format='json')
        assert response.status_code == 200

    def test_get_all_courses_filtered_by_student(self):
        Teacher.objects.create(user=self.user)
        new_teacher = Teacher.objects.all()[0]
        new_course = CourseORM(name = "prueba",
            slug = "prueba",
            code = "XXX",
            description = "prueba",
            teacher = new_teacher)
        new_student = Student.objects.create(user=self.user)
        new_student.save()
        new_course.students.add(new_student)
        new_course.save()
        
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'Token {self.token}')
        response = client.get('/courses/enrolled-courses/%s/' % (new_student.code), {}, format='json')
        assert response.status_code == 200