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
        all_courses = CourseORM.objects.all()
        if not all_courses.exists():
            raise ObjectDoesNotExist()
        courses = Courses()
        for course in all_courses:
            courses.append(self._decode_orm_course(course))

        return courses

    def get_all_filter_by_user(self, username):
        orm_course = CourseORM.objects.all()
        if not orm_course.exists():
            raise ObjectDoesNotExist()
        courses = Courses()
        courses_list = orm_course.fetchall()
        for course in courses_list:
            courses.append(self._decode_orm_course(course))

        return courses

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
