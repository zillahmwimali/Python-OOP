x = [100,110,120,130,140,150]
y=[i*5 for i in x]
print(y)

def divisible_by_three(n):
    for p in range(1,n):
        if p%3==0:
            print(p)
divisible_by_three(30)

x= [[1,2],[3,4],[5,6]]
m=[]
for sublist in x:
    for item in sublist:
        m.append(item)
print(m)

def smallest(x):
    return(min(x))
smallest(x=[3,6,8,2,4,1,5,7])

def sort_list(x):
    y=set(x)
print(y)
x = ['a','b','a','e','d','b','c','e','f','g','h']
sort_list(x)

def divisible_by_seven():
    d=[]
    for k in range(100,200):
        if k%7==0:
            d.append(k)
    print(d)
divisible_by_seven()

def greet():
    current_year=2021
    students = [
        {"age": 19, "name": "Eunice"},
         {"age": 21, "name": "Agnes"}, 
         {"age": 18, "name": "Teresa"}, {"age": 22, "name": "Asha"}
         ]
    for student in students:
         print (f"Hello{student.name},you were born in the year{current_year-student.age}")                                                                                     
 
class Rectangle:
    def __init__(self,width,length):
        self.width=width
        self.length=length

    def area(self):
        area=self.width*self.length
        return area
    def perimeter(self):
        perimeter=2*(self.width+self.length)
        return perimeter





