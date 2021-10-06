from django.core.exceptions import ObjectDoesNotExist
from framework.models.courses import CourseORM
from courses.entities.course import Course


class CourseDatabaseRepo(object):

    def get_course(self, code):
        try:
            orm_course = CourseORM.objects.get(code=code)
        except CourseORM.DoesNotExist:
            raise ObjectDoesNotExist()

        return self._decode_orm_product(orm_course)

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

