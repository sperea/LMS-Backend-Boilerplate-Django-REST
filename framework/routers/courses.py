from django.urls import path
from framework.views import ViewWrapper
from courses.views.course import GetCourseViewFactory

app_name = 'courses'

urlpatterns = [
    path('course-info/<int:code>/',
         ViewWrapper.as_view(view_factory=GetCourseViewFactory),
         name='course'),
]