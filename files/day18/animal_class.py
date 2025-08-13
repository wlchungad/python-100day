class Animal():
    def __init__(self, name=""):
        self.name = name

    def make_sound(self):
        print("Generic method called")

class Dog(Animal):
    def __init__(self, name="", favourite="Bone"):
        super().__init__(name)
        self.favourite = favourite
    
    def make_sound(self):
        # This overwrites the same method from parent class
        print(f"{self.name}: Woof~~")
        print(f"It's asking for {self.favourite}!")

class Cat(Animal):
    def __init__(self, name=""):
        super().__init__(name)
    
    def make_sound(self):
        print(f"{self.name}: Meow~~")