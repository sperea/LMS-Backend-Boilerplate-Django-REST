from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from framework.models.courses import CourseORM
from accounts.models import Student
from courses.entities.course import Course


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

    def get_all_by_student(self, code):
        student = get_object_or_404(Student, code=code)
        courses = CourseORM.objects.filter(students__in=[student])
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
            description=orm_course.description,
            image=orm_course.image)


class CourseDatabaseRepoFactory(object):

    @staticmethod
    def get():
        return CourseDatabaseRepo()
