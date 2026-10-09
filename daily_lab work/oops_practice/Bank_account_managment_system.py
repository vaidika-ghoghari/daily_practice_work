print("======== BANK ACCOUNT MANAGEMENT SYSTEM ========")

from abc import ABC  ,  abstractmethod

# abstract class

class Account(ABC):

  """Abstract base class. cannot be initialize directly."""

  @abstractmethod

  def deposit(self  , amount):
    pass

  def withdraw(self , amount):
    pass

# Encapsulations

class BankAccount(Account):

  """ A basic account. Balance is private and only changed via methods."""

  def __init__(self , account_number , account_name , balance = 0):
    self.account_number = account_number
    self.account_name = account_name
    self.__balance = balance

  def deposit(self , amount):
    if amount > 0:
      self.__balance += amount
    
    else:
      print("Deposit amount must be positive.")

  def withdraw(self , amount):

    if 0 < amount <= self.__balance:
      self.__balance -= amount

    else:

      print("Withdraw failed: invalid amount or insufficient funds.")

  def get_balance(self):

    return self.__balance

  def get_account_number(self):
    return self.account_number

  def _update_balance(self , new_balance):

    self.__balance = new_balance

  
# Inheritance

class SavingAccount(BankAccount):

  def __init__(self , account_number, account_name ,   balance = 0 , interest_rate = 4):
    super().__init__(account_number , account_name , balance)
    self.interest_rate = interest_rate

  def add_interest(self):
    interest = self.get_balance() * self.interest_rate / 100
    self.deposit(interest)
    return interest

# Polymorphism

class CurrentAccount(BankAccount):

  """ current account that allow overdraft up to limit."""

  def __init__(self , account_number , account_name ,  balance = 0 , overdraft_limit = 1000):
    super().__init__(account_number , account_name ,  balance)
    self.overdraft_limit = overdraft_limit

  def withdraw(self , amount):

    new_balance = self.get_balance() - amount

    if amount >= 0 and new_balance >= self.overdraft_limit:
      self._update_balance(new_balance)
    
    else:
      print(f"Withdraw failed: overdraft limit of {self.overdraft_limit} exceeded.")

def show(account):
  """Display an account's type , number and balance."""
  print(f"[{type(account).__name__}]"
        f"{account.get_account_number()} -> {account.get_balance():.2f}"
  )

if __name__ == "__main__":

  saving = SavingAccount("SAVING-101" , "Vivek" , 5000 , interest_rate=4)

  show(saving)

  saving.deposit(15000)

  show(saving)

  saving.withdraw(5000)

  show(saving)

  earned = saving.add_interest()

  show(saving)

  current = CurrentAccount("CUR-101" ,"Vivek" ,   2000 , overdraft_limit=1000)

  show(current)

  current.withdraw(3000)

  show(current)















            
            
