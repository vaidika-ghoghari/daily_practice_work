class BankAccount:

    def __init__(self ,account_holder ,account_number , balance):
        self.account_holder = account_holder
        self.account_number = account_number
        self.__balance #make balance private

    def deposite(self ,amount):

        if amount > 0:
            self.__balance +=amount
            print(f"{amount} Successfully deposited.")
        else :
            print("Invalid Deposit amount.")

    def withdraw(self ,amount):

        if amount <= 0:
            print(f"inavalid amount.")
            
        elif amount > self.__balance :
            print("Insufficient balance.")

        else :

            self.__balance -= amount
            print(f"{amount} Withdraw Sucessfully.")

    def check_balance(self):
        print(f"Current Balance : {self.__balance}")

    def display(self):
        print("Account Holder : ", self.account_holder)
        print("Account Number : ", self.account_number)
        print("Account Balance : ", self.__balance)

name = input("Enter your name :")
acc_num=int(input("Enter account number : "))
balance = float(input("Enter Opening Balance : "))

account = BankAccount(name ,acc_num , balance)
account.balance = 30000   # creating outside access

while True :
    print("====== Bank Menu ======")
    print("1. Deposite")
    print("2. Withdraw")
    print("3. Check  Balance")
    print("4. Display Account Details")
    print("5. Exit")

    choice = int(input("Enter your choice : "))

    if choice == 1:
        amount = float(input("Enter deposite amount :"))

        account.deposite(amount)
        
    elif choice == 2:
        amount = float(input("Enter withdraw amount :"))

        account.withdraw(amount)

    elif choice == 3:
        account.check_balance()

    elif choice == 4:
        account.display()
        
    elif choice == 5:
        print("Thank you for choosing Bank of Baroda.")

    else:
        print("Invalid Choice")        
     
            
