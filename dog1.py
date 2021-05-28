class Dog:
    breed="German Shepherd"
    def __init__(self,color,age,sound):
        self.color=color
        self.age=age
        self.sound=sound
    
    def identity(self):
        return f"I am a {self.color} {self.breed} of {self.age} years old."
    def guard(self):
        return f"I {self.sound} once I sense an enemy."