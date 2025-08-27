class MultiBases(type):
    # overriding __new__ method
    def __new__(cls, clsname, bases, clsdict):
        # if no of base classes is greater than 1 raise error
        if len(bases)>1:
            raise TypeError("Multiple base classes inherited")
        
        # else execute __new__ method of super class, ie. call __init__ of type class
        else:
            return super().__new__(cls, clsname, bases, clsdict)

class Base(metaclass=MultiBases):
    pass

class Person(Base):
    def __init__(self, name):
        self.name = name
    
    def hello(self):
        print(f"Hello I am {self.name}")

class Student(Person):
    def __init__(self, name, school):
        super().__init__(name)
        self.school = school

    def hello(self):
        print(f"Hello I am {self.name} from {self.school}")

class UniversityStudent(Student):
    def __init__(self, name, school, studies):
        super().__init__(name, school)
        self.studies = studies
    
    def hello(self):
        print(f"Hello I am {self.name} from {self.school} studying {self.studies}")

alice = UniversityStudent('Alice', "ABC College", "Religious Studies")
alice.hello()

# the python should stop here:
class InvalidClass(Person, Student):
    def __init__(self, name):
        super().__init__(name)

