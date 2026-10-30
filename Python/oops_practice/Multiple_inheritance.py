#  Multiple Inheritance

#  -- When one child class inherits properties and methods from two or more parent
#     classes,  it is called Multiple Inheritance.


class Teacher:
  def __init__(self , subject):
    self.subject = subject
  
  def teach(self):
    print(f"Teaching {self.subject} to students.")

class Administrator:

  def __init__(self , department):
    self.department = department

  def manage(self):
      print(f"Managing the {self.department} department.")

class Headmaster(Teacher , Administrator):

  def __init__(self , subject , department , school_name):
    Teacher.__init__(self , subject)
    Administrator.__init__(self , department)
    self.school_name = school_name

  def guide(self):
    print(f"Guiding staff and students at {self.school_name}")

head = Headmaster("Mathematics",  "Academic" , "Red and White Public School.")

head.teach()
head.manage()
head.guide()
