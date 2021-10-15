
class CourseSerializer:

    @staticmethod
    def serialize(course):
        return {
            'code': course.code,
            'slug': course.slug,
            'code': course.code,
            'description': course.description,
            'image': str(course.image.url)
        }

    @staticmethod
    def serialize_list(course_list):
        serialized_list = []
        for course in course_list:
            serialized_list.append(CourseSerializer.serialize(course))
        return serialized_list

