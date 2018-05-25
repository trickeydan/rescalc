import os

from .io import loadfile


class Course:

    def __init__(self, folder):

        self.data = loadfile(os.path.join(folder, "course.yml"))


