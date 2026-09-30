#inheritance
#  -- Inheritance is an oop concept where a child class gets the
#       properties and methods of parent class.


# 1. Single inheritance :-

# -- When one child class inherits properties and methods from 
#      one parent class ,it is called single inheitance. 

#example :-

class BankAccount:

    def __init__(self, account_holder ,account_number ,balance):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance

    def display(self):
        print(f"Account Holder : {self.account_holder}")
        print(f"Account Number : {self.account_number}")
        print(f"Account Balance : {self.balance}")

class SavingsAccount(BankAccount):

    def __init__(self, account_holder ,account_number ,balance ,interest_rate):
        super().__init__(account_holder ,account_number ,balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance *self.interest_rate / 100
        self.balance += intrest
        print(f"Interest added : ${interest:.2f} at {self.interst_rate}% rate")

class CurrentAccount(BankAccount):
    def __init__(self, account_holder ,account_number ,balance ,interest_rate):
        super().__init__(account_holder ,account_number ,balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance *self.interest_rate / 100
        self.balance += intrest
        print(f"Interest added : ${interest:.2f} at {self.interst_rate}% rate")

acc_s = SavingsAccount("Rahul Sharma" , "bob102101",10000 , 6 )
acc_c = SavingsAccount("jemish Sharma" , "bob102102",10000 , 4 )

acc_s.display()

acc_c.display()

        
