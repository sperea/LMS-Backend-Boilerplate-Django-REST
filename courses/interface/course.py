from courses.drivers.database.course import CourseDatabaseRepoFactory

class CourseRepo(object):

    def __init__(self, db_repo, cache_repo):
        self.db_repo = db_repo
        self.cache_repo = cache_repo

    def get_product(self, reference):
        product = self.db_repo.get_course(reference)
        return product


class CourseRepoFactory(object):

    @staticmethod
    def get():
        db_repo = CourseDatabaseRepoFactory.get()
        return CourseRepo(db_repo)