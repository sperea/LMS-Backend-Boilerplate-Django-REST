from courses.use_cases.course_interactors import GetCourseInteractorFactory
from courses.serializers.course import CourseSerializer
from django.core.exceptions import ObjectDoesNotExist


class GetCourseView(object):

    def __init__(self, get_course_interactor):
        self.get_course_interactor = get_course_interactor

    def get(self, code):
        try:
            course = self.get_course_interactor.set_params(code=code).execute() 
        except ObjectDoesNotExist:
            body = {'error': 'Course does not exist!'}
            status = 404
        else:
            body = CourseSerializer.serialize(course)
            status = 200

        return body, status


class GetCourseViewFactory(object):

    @staticmethod
    def create(request):
        get_course_interactor = GetCourseInteractorFactory.get()
        return GetCourseView(get_course_interactor)