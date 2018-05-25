import os

from .io import loadfile


class Course:

    def __init__(self, folder):
        self.data = loadfile(os.path.join(folder, "course.yml"))

    @property
    def name(self):
        return self.data["name"]

    @property
    def parts(self):
        parts = []
        for part in self.data["parts"]:
            parts.append(Part(part))
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
        return "Fail"


class Part:

    def __init__(self, data):
        self.data = data

    @property
    def name(self):
        return self.data["name"]

    @property
    def weight(self):
        return self.data["weight"]

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
            semesters.append(Semester(sem))
        return semesters


class Semester:

    def __init__(self, data):
        self.data = data

    @property
    def name(self):
        return self.data["name"]

    @property
    def score(self):
        return 100

    @property
    def modules(self):
        return self.data["modules"]
