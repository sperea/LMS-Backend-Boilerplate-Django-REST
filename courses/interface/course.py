from courses.drivers.database.course import CourseDatabaseRepoFactory

class CourseRepo(object):

    def __init__(self, db_repo):
        self.db_repo = db_repo

    def get_course(self, code):
        course = self.db_repo.get_course(code)
        return course

    def get_all(self):
        courses = self.db_repo.get_all()
        return courses

    def get_all_by_student(self, code):
        courses = self.db_repo.get_all_by_student(code)
        return courses

class CourseRepoFactory(object):

    @staticmethod
    def get():
        db_repo = CourseDatabaseRepoFactory.get()
        return CourseRepo(db_repo)