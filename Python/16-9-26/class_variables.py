#class variables

class college:

    college_name = "red and white skill education"

    def __init__(self ,student):
        self.student = student


s1 = college("peter")
s2 = college("james")

print(f"{s1.student} == {s1.college_name} ")
print(f"{s2.student} == {s2.college_name} ")


#user unput object
class student:

    def __init__(self,name,age,course,marks ):
        self.name = name
        self.age = age
        self.course = course
        self.marks = marks

    def display(self):
        print("Name : ",self.name)
        print("Age : ",self.age)
        print("Course : ",self.course)
        print("Marks : ",self.marks)

name= input("Enter Name:")
age= input("Enter age:")
course= input("Enter course:")
marks= input("Enter marks:")

s1 = student( name, age , course ,marks)
s1.display()

s2=s1
s2.display()

#delete attribute (del)

class demo:

    def __init__(self):
        self.name = "python"
        self.duration = "6 month"


    def display(self):
        print("Name :" ,self.name)
        print("Duration : ",self.duration)

d1= demo()

print(d1.name)
print(d1.duration)

d1.display()

del d1.display
d1.display()


