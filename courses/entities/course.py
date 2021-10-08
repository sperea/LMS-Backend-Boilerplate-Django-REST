

class Course(object):

    def __init__(self, name, slug, code, description):
        self._name = name
        self._slug = slug
        self._code = code
        self._description = description

    @property
    def name(self):
        return self._name

    @property
    def slug(self):
        return self._slug

    @property
    def code(self):
        return self._code

    @property
    def description(self):
        return self._description



class Courses(object):

    def __init__(self):
        self._list = []

    def append(self, element):
        if isinstance(element, Course):
            self._list.append(element)
        else:
            raise TypeError
        return self

    def all(self):
        return self

    def len(self):
        return len(self._list)

    def filter_by_username(self, username):
        filtered_courses = Courses()
        for course in self._list:
            if (course.name == username):
                filtered_courses.append(element)
        return filtered_courses


class CoursesIterator:
    def __init__(self, courses):
        self._courses = courses
        self._index = 0

    def __next__(self):
       if self._index < self._courses.len():
           self._index = self._index + 1
           return self._courses.get(self._index)
       # End of Iteration
       raise StopIteration