class Student:
    def __init__(self, name, chinese, math, english):
        self.name = name
        self.chinese = chinese
        self.math = math
        self.english = english

    def total(self):
        return self.chinese + self.math + self.english

    def average(self):
        return self.total() / 3

    def to_dict(self):
        return {
            "name": self.name,
            "chinese": self.chinese,
            "math": self.math,
            "english": self.english,
        }

    @classmethod
    def from_dict(cls, d):
        return cls(d["name"], d["chinese"], d["math"], d["english"])

    def __str__(self):
        return (f"{self.name:<8}{self.chinese:>6}{self.math:>6}"
                f"{self.english:>6}{self.total():>8}{self.average():>8.1f}")