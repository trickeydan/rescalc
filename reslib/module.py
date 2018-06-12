import os

from .io import loadfile


class Module:

    def __init__(self, folder, module):
        self.folder = folder
        self.data = loadfile(os.path.join(folder, "modules", module + ".yml"))

    @property
    def name(self):
        return self.data["name"]

    @property
    def weight(self):
        return self.data["weight"]

    @property
    def score(self):
        if len(self.assessments) <= 0:
            return 0

        score = 0
        div_factor = 1

        for assess in self.assessments:
            score += assess.score * assess.weight
        return score

    @property
    def classification(self):
        return "???"

    @property
    def assessments(self):
        assignments = []
        if not self.data["assessments"] is None:
            for assign in self.data["assessments"]:
                assignments.append(Assessment(self.folder, assign))
        return assignments


class Assessment:

    def __init__(self, folder, data):
        self.folder = folder
        self.data = data

    @property
    def name(self):
        return self.data["name"]

    @property
    def score(self):
        return self.data["result"] * 100 / self.data["max-result"]

    @property
    def weight(self):
        return self.data["weight"]

    @property
    def classification(self):
        return "???"
