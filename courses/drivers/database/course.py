from django.core.exceptions import ObjectDoesNotExist
from framework.models.courses import CourseORM
from courses.entities.course import Course
from courses.entities.course import Courses


class CourseDatabaseRepo(object):

    def get_course(self, code):
        try:
            orm_course = CourseORM.objects.get(code=code)
        except CourseORM.DoesNotExist:
            raise ObjectDoesNotExist()

        return self._decode_orm_course(orm_course)

    def get_all(self):
        courses = CourseORM.objects.all()
        if not courses.exists():
            raise ObjectDoesNotExist()
        courses_list = []
        for course in courses:
            courses_list.append(self._decode_orm_course(course))
        return courses_list


    def _decode_orm_course(self, orm_course):
        return Course(
            name=orm_course.name,
            slug=orm_course.slug,
            code=orm_course.code,
            description=orm_course.description)


class CourseDatabaseRepoFactory(object):

    @staticmethod
    def get():
        return CourseDatabaseRepo()
