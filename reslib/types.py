class Classifiable:

    BOUNDARIES = {
        '3': 40,
        '2:2': 50,
        '2:1': 60,
        '1': 70,
    }

    @property
    def score(self):
        return 0

    @property
    def classification(self):
        score = self.score
        current = "Fail"
        for key, value in Classifiable.BOUNDARIES.items():
            if score >= value:
                current = key
        return current
