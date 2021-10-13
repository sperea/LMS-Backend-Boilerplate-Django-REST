from courses.use_cases.course_interactors import GetCourseInteractorFactory
from courses.use_cases.course_interactors import GetAllCoursesInteractorFactory
from courses.use_cases.course_interactors import GetAllEnrolledCoursesInteractorFactory
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


class GetAllCourseView(object):

    def __init__(self, get_course_interactor):
        self.get_all_courses_interactor = get_course_interactor

    def get(self):
        try:
            courses = self.get_all_courses_interactor.execute() 
        except ObjectDoesNotExist:
            body = {'error': 'Course does not exist!'}
            status = 404
        else:
            body = CourseSerializer.serialize_list(courses)
            status = 200

        return body, status



class GetAllCoursesViewFactory(object):

    @staticmethod
    def create(request):
        get_course_interactor = GetAllCoursesInteractorFactory.get()
        return GetAllCourseView(get_course_interactor)


class GetAllEnrolledCoursesView(object):

    def __init__(self, get_course_interactor):
        self.get_all_enrolled_courses_interactor = get_course_interactor

    def get(self, code):
        try:
            courses = self.get_all_enrolled_courses_interactor.set_params(code=code).execute() 
        except ObjectDoesNotExist:
            body = {'error': 'Course does not exist!'}
            status = 404
        else:
            body = CourseSerializer.serialize_list(courses)
            status = 200

        return body, status


class GetAllEnrolledCoursesViewFactory(object):

    @staticmethod
    def create(request):
        get_course_interactor = GetAllEnrolledCoursesInteractorFactory.get()
        return GetAllEnrolledCoursesView(get_course_interactor)