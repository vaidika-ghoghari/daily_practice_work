#while loop program

#41.
print("print number  1 to 10")

i=1

while i <= 10:
    print(i)
    i += 1

#42.
print("\nprint even  numbers.")

n=int(input("enter the number:"))

i=1
while i <= n:
    if i % 2 == 0:
        print(i)
    i += 1

#43.
print("\nprint odd  numbers.")

n=int(input("enter the number:"))

i=1
while i <= n:
    if i % 2 != 0:
        print(i)
    i += 1

#44.
print("\nprint factorial of  numbers.")

n=int(input("enter the number:"))
factorial = 1
i = 1

while i <= n:
    factorial *= i
    i += 1

print("Factorial of number is :" ,factorial)


#45.
print("\n reverse a number")
n = int(input("Enter the number: "))
rev = 0

while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10

print("reverse number :", rev)


#46.
print("\nsum of digits.")
n = int(input("Enter the number: "))
sum = 0

while n > 0:
    digit = n % 10
    sum = sum + digit
    n = n // 10

print("sum of digit :", sum)

#47.
print("\n count the digit in number")
n = int(input("Enter the number: "))
count = 0

while n > 0:
    n = n // 10
    count = count + 1

print("Number of digits :", count)

#48.
i = 7
n = int(input("\nGuess the number between 1 to 10: "))

while n != i:
    print("Wrong guess!")
    n = int(input("Try again: "))

print("Correct guess! ")

#49.
print("\nmenu driven calculator.")
while True:
    print("\n1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("0. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 0:
        print("Calculator closed.")
        break

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    if choice == 1:
        print("Answer =", a + b)
    elif choice == 2:
        print("Answer =", a - b)
    elif choice == 3:
        print("Answer =", a * b)
    elif choice == 4:
        print("Answer =", a / b)
    else:
        print("Invalid choice")
else:
        print("Invalid choice")

#50.
print("\nContinue taking input until user enters 0.")
while True:
    n = int(input("Enter a number: "))

    if n == 0:
        break

    print("You entered:", n)

print("Program ended.")





    
