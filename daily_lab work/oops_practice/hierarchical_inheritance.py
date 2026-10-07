#Hierarchical Inheritance
print(==== Hierarchical Inheritance ====)

class StaffMember:

  def __init__(self , name , employee_id):
    self.name = name
    self.employee_id = employee_id

  def check_in(self):
    print(f"{self.name} (ID : {self.employee_id}) checked in for the day>>>>>")

class Developer(StaffMember):

  def code(self):
    print(f"{self.name} is writing code>>>>>")

class Tester(StaffMember):

  def test(self):
    print(f"{self.name} is testing the application code>>>>>>")



d = Developer("Zeel" , "E101")

d.check_in()

d.code()

print()

t = Tester("Amit" , "E102")

t.check_in()

t.test()

# 5. Hybrid Inheritance

# Person  -> Student & Employee -> TeachingAssistant

class Person:

  def __init__(self , name):
    self.name = name
  
  def profile(self):
    print(f"Name : {self.name}")

class Student(Person):

  def __init__(self , name , roll_num):
    Person.__init__(self , name)
    self.roll_num = roll_num

  def profile(self):
    print(f"Roll Number : {self.roll_num}")


class Employee(Person):

  def __init__(self , name , salary):
    Person.__init__(self , name)
    self.salary = salary

  def profile(self):
    print(f"Salary : {self.salary}")

class TeachingAssistant(Student , Employee):

  def __init__(self , name , roll_num , salary , subject):
    Student.__init__(self , name , roll_num)
    Employee.__init__(self , name , salary)
    self.subject = subject
  

  def profile(self):
    Person.profile(self)
    Student.profile(self)
    print(f"Salary : {self.salary}/month")
    print(f"Subject Assisting : {self.subject}")

ta = TeachingAssistant("Zara" , "Z101" , 8000 , "Python Programming")

ta.profile()

 
