

class Course(object):

    def __init__(self, name, slug, code, description, image, hours):
        self._name = name
        self._hours = hours
        self._slug = slug
        self._code = code
        self._description = description
        self._image = image

    @property
    def name(self):
        return self._name

    @property
    def hours(self):
        return self._hours

    @property
    def slug(self):
        return self._slug

    @property
    def code(self):
        return self._code

    @property
    def description(self):
        return self._description

    @property
    def image(self):
        return self._image

