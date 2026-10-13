age = 20

if age < 18:
  raise ValueError("Age Must be 18 or above")

print("Age is valid")

def get_age(age):
  if age < 0:
    raise ValueError("Age cannot be negative")
  return age

try:

  get_age(5)

except ValueError as e:
  print(f"Error : {e}")

def process_data(data):
  try:
    return 10 / data
  except ZeroDivisionError:
    print("division by zero attempted")
    raise

try:
  process_data(0)
except ZeroDivisionError:
  print("calling exception handeling.")

'''

# ASSERT KEYWORD
'''
marks = -10

assert marks >= 0 , "Marks cannot be nagative"

print("Marks is valid")

def calculate_average(numbers):
  assert len(numbers) > 0 , "List cannot be empty"

  return sum(numbers) / len(numbers)


print(calculate_average([10 , 20 , 30]))


# 3. assert with message

marks = -10

assert marks >= 0 , "Marks cannot be nagative"

print("Marks is valid")

#4. custom exception

class AgeError(Exception):
  pass

age = 18

try:

  if age < 18:

    raise AgeError("Age Must be 18 or above")

  print("Eligible for voting")

except AgeError as e:
    print("Error :" , e)


class InsufficientFundsError(Exception):
  pass

class BankAccount:

  def __init__(self , balance = 0):
    self.balance = balance

  def withdraw(self , amount):

    assert amount > 0 , "Withdrwal amount must be positive"

    if amount > self.balance:

      raise InsufficientFundsError(f"cannot withdraw {amount}, balance is only {self.balance}")

    self.balance -= amount
    return self.balance

account = BankAccount(1000)

try:

  print(account.withdraw(1000))

except InsufficientFundsError as e:

