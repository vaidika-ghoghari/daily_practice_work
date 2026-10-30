# real world :Online shopping costumers

class customer:

    def __init__ (self ,name):
        self.name = name

    def shopping(self):
        print(f"{self.name } is shopping.")

    def __del__(self):
        print(f"{self.name } is logged out.")


c1 = customer("vaidika")
c1.shopping()

del c1


#employee attendence

class Employee:

    def __init__(self):
        self.name = "vaidika"
        self.department ="IT"

    def display(self):
        print("Employee : ", self.name)
        print("Department :" ,self.department)


    def __del__(self):
        print(self.name , "Left office. Goodbye!")

e1 = Employee()
e1.display()


        
