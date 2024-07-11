import datetime


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def get_age_from_year(cls, name, year):
        age = datetime.datetime.now().year - year
        person_obj = cls(name, age)
        return person_obj


p1 = Person("Alex", 24)
print(p1.age)  # 24


p2 = Person.get_age_from_year("Jon", 1992)
print(p2.age)  # 32
print(p2.name)  # Jon

