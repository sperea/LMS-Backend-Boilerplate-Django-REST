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
            description = "prueba",
            teacher = new_teacher).save()
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
        response = client.get('/course-info/1/', {}, format='json')
        assert response.status_code == 200
