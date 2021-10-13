from courses.interface.course import CourseRepoFactory

class GetCourseInteractor(object):

    def __init__(self, course_repo):
        self.course_repo = course_repo

    def set_params(self, code):
        self.code = code
        return self

    def execute(self):
        return self.course_repo.get_course(self.code)


class GetCourseInteractorFactory(object):

    @staticmethod
    def get():
        course_repo = CourseRepoFactory.get()
        return GetCourseInteractor(course_repo)


class GetAllCoursesInteractor(object):

    def __init__(self, course_repo):
        self.course_repo = course_repo

    def execute(self):
        return self.course_repo.get_all()


class GetAllCoursesInteractorFactory(object):

    @staticmethod
    def get():
        course_repo = CourseRepoFactory.get()
        return GetAllCoursesInteractor(course_repo)



class GetAllEnrolledCoursesInteractor(object):

    def __init__(self, course_repo):
        self.course_repo = course_repo

    def set_params(self, code):
        self.code = code
        return self

    def execute(self):
        return self.course_repo.get_all_by_student(self.code)


class GetAllEnrolledCoursesInteractorFactory(object):

    @staticmethod
    def get():
        course_repo = CourseRepoFactory.get()
        return GetAllEnrolledCoursesInteractor(course_repo)