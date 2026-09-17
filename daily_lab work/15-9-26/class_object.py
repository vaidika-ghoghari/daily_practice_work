#class intialization

class Car:
    #constructor
    def __init__(self,brand, name ,model,prize):
        self.brand = brand
        self.name = name
        self.model = model
        self.prize = prize


    #methods
    def start(self):
        print(f" {self.brand} and {self.model} is starting..... ")


    #method2
    def details(self):
        print(f"""
        Brand : {self.brand}
        Name : {self.name}
        Model : {self.model}
        Prize : {self.prize}
    """)

    #access the object

car1= Car('honda','city','white',120000)
car2= Car('audi','R8','red',1200000)

print(car1)    
car1.details()
car2.details()


########
#simple class

class student:
    pass

s1=student()

print(s1)
print(type(s1))

#class with attributes

class Students:

    name = "vaidika"
    age = 20
    course = "Python"

s1 = Students()

print("Name : ", s1.name)
print("Age : " , s1.age)
print("Course : ", s1.course)

#update object value

class Student:
    def __init__(self , name , salary):
        self.name = name
        self.salary = salary

s1 = Student("peter", 120000)

print(s1.name)
print(s1.salary)

s1.salary = 130000
print(s1.salary)

    










