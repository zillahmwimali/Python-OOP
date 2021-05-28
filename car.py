class Car:
    origin="Germany"
    def __init__(self,make,model,color,capacity,speed):
        self.color=color
        self.make=make
        self.model=model
        self.capacity=capacity
        self.speed=speed

    def full_description(self):
        return f"This is a {self.color} {self.make} {self.model} with a {self.capacity} seater carriage. "
    def accelerate(self):
        return f"This {self.origin} machine can accelerate from zero to {self.speed}mph in four seconds. "
