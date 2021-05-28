class Student:
    school="Akirachix"
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def speak(self):
        return f"Hello my name is {self.name} and I am {self.age} years old and I school at {self.school}."
    #tocreate a class,use class keyword
    #start the class name with a capital letter if the class has more than one word,capitalize each word
    # no spaces in the class name
    #when you save your module in your .py file,it's called a module
    #to import a class from a module,use dot notation=>from module import class name
    # modules in a directory from a package
    # car.py(4 attributes,3behaviours)
    # dog.py()
    # bank  