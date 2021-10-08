from django.urls import path
from framework.views import ViewWrapper
from courses.views.course import GetCourseViewFactory
from courses.views.course import GetAllCoursesViewFactory

app_name = 'courses'

urlpatterns = [
    path('course-info/<code>/',
         ViewWrapper.as_view(view_factory=GetCourseViewFactory),
         name='course-info'),
    path('all-courses/',
         ViewWrapper.as_view(view_factory=GetAllCoursesViewFactory),
         name='course-info'),
]