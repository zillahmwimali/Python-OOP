class Student:
    school="Akirachix"
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def speak(self):
        return f"Hello my name is {self.name} and I am {self.age} years old."