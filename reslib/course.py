import os

from .io import loadfile
from .module import Module


class Course:

    def __init__(self, folder):
        self.folder = folder
        self.data = loadfile(os.path.join(folder, "course.yml"))

    @property
    def name(self):
        return self.data["name"]

    @property
    def parts(self):
        parts = []
        for part in self.data["parts"]:
            parts.append(Part(self.folder, part))
        return parts

    @property
    def score(self):

        if len(self.parts) <= 0:
            return 0

        score = 0

        for part in self.parts:
            score += part.score * part.weight
        return score

    @property
    def classification(self):
        return "???"


class Part:

    def __init__(self, folder, data):
        self.folder = folder
        self.data = data

    @property
    def name(self):
        return self.data["name"]

    @property
    def weight(self):
        return self.data["weight"]

    @property
    def classification(self):
        return "???"

    @property
    def score(self):

        if len(self.semesters) <= 0:
            return 0

        score = 0

        for sem in self.semesters:
            score += sem.score
        score /= len(self.semesters)
        return score

    @property
    def semesters(self):
        semesters = []
        for sem in self.data["semesters"]:
            semesters.append(Semester(self.folder, sem))
        return semesters


class Semester:

    def __init__(self, folder, data):
        self.folder = folder
        self.data = data

    @property
    def name(self):
        return self.data["name"]

    @property
    def classification(self):
        return "???"

    @property
    def score(self):

        if len(self.modules) <= 0:
            return 0

        score = 0

        for mod in self.modules:
            score += mod.score
        score /= len(self.modules)
        return score

    @property
    def modules(self):
        modules = []
        if self.data["modules"] is None:
            return []
        for mod in self.data["modules"]:
            modules.append(Module(self.folder, mod))
        return modules
