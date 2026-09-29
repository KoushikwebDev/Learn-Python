from abc import ABC, abstractmethod

# we can not create object from a abstract class
class Mentor(ABC):
    @abstractmethod
    def teach(self):
        pass


# so can not use abstract class directly, but we can inherit all methods from the abstract class
class SuperMentor(Mentor):
    def teach(self):
        return "I am the best tutor"

mentor_a = SuperMentor() 
print(mentor_a.teach())


# multiple abstraction inheritance

class Course(ABC):

    @abstractmethod
    def content(self): pass

    @abstractmethod
    def duration(self): pass

    @abstractmethod
    def tutor(self): pass

    # concreate method
    def price(self):
        return 5000


class PythonCourse(Course):
    def content(self):
        return "This course contain the python info"

    def duration(self):
        return "this course duration is 1 week"

    def tutor(self):
        return "this course will be teach by Koushik"

my_course = PythonCourse()

print(my_course.content())
print(my_course.tutor())
print(my_course.price())
