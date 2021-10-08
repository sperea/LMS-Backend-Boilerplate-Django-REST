from courses.entities.course import CoursesIterator

class CourseSerializer:

    @staticmethod
    def serialize(course):
        return {
            'code': course.code,
            'slug': course.slug,
            'code': course.code,
            'description': course.description
        }

    @staticmethod
    def serialize_list(course_list):
        serialized_list = []
        for course in course_list:
            serialized_list.append(CourseSerializer.serialize(course))
        return serialized_list

    @staticmethod
    def serialize_iterator(course_list):
        serialized_list = []
        iterator = CoursesIterator(course_list)
        while True:
            try:
                course = next(iterator)
                serialized_list.append(CourseSerializer.serialize(course))
            except StopIteration:
                break