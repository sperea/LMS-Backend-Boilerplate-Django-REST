from accounts.models import *
from PIL import Image
from io import BytesIO

from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.test import APITestCase
from framework.models.courses import *
from django.core.files.uploadedfile import SimpleUploadedFile
import tempfile


class GetCourseTests(APITestCase):

    def setUp(self):
        self.user = CustomUser.objects.create_user(email='js@js.com', password='js.sj')
        self.refresh = RefreshToken.for_user(self.user)
        client = APIClient()
        response = client.post('/token/login/', {'email': 'js@js.com', 'password': 'js.sj'}, format='json')
        self.token = response.data["auth_token"]
        self.small_gif = (
            b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x00\x00\x00\x21\xf9\x04'
            b'\x01\x0a\x00\x01\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02'
            b'\x02\x4c\x01\x00\x3b'
        )
    def test_get_course_by_code(self):
        Teacher.objects.create(user=self.user)
        new_teacher = Teacher.objects.all()[0]
        
        CourseORM(name = "prueba",
            slug = "prueba",
            code = "XXX",
            description = "prueba",
            teacher = new_teacher,
            image=SimpleUploadedFile('small.gif', self.small_gif, content_type='image/gif')).save()
        
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
            teacher = new_teacher,
            image=SimpleUploadedFile('small.gif', self.small_gif, content_type='image/gif')).save()
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'Token {self.token}')
        response = client.get('/courses/all-courses/', {}, format='json')
        assert response.status_code == 200

    def test_get_all_courses_filtered_by_student(self):
        Teacher.objects.create(user=self.user)
        new_teacher = Teacher.objects.all()[0]
        new_course = CourseORM(name="prueba",
            slug ="prueba",
            code="XXX",
            description="prueba",
            teacher=new_teacher,
            image=SimpleUploadedFile('small.gif', self.small_gif, content_type='image/gif'))
        new_student = Student.objects.create(user=self.user)
        new_student.save()
        new_course.students.add(new_student)
        new_course.save()
        
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'Token {self.token}')
        response = client.get('/courses/enrolled-courses/%s/' % (new_student.code), {}, format='json')
        assert response.status_code == 200