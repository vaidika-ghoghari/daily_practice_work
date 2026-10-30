#16.
print("\ncheck whether a number is positive, negative or zero.")
number = int(input("Enter a number: "))
if number > 0:
    print("The number you have entered is positive.")
elif number < 0:
    print("The number you have entered is negative.")
else:
    print("The number you have entered is zero.")


#17.
print("\ncheck whether a number is even or odd.")
number = int(input("Enter a number: ")) 
if number % 2 == 0:
    print("The number you have entered is even.")   
else:
    print("The number you have entered is odd.")    

#18.
print("\nfind largest of two numbers.")
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
if number1 > number2:
    print("The largest number is:", number1)
else:
    print("The largest number is:", number2)

#19.
print("\nfind largest of three numbers.")
number1 = int(input("Enter the first number: "))  
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))
if (number1 >= number2) and (number1 >= number3):
    largest = number1
elif (number2 >= number1) and (number2 >= number3):
    largest = number2
else:
    largest = number3   
print("The largest number is:", largest)

#20.
print("\nfind smallest of three numbers.")
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))
if (number1 <= number2) and (number1 <= number3):
    smallest = number1
elif (number2 <= number1) and (number2 <= number3):
    smallest = number2
else:
    smallest = number3
print("The smallest number is:", smallest)



#21.
print("\ncheck whether a person is eligible to vote or not.")
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")



#22.
print("\ncheck whether a year is a leap year or not.")
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or(year % 400 == 0):
    print(year, "is a leap year.") 
else:
    print(year, "is not a leap year.")  


#23.
print("\ncheck whether a character is a vowel or consonant.")
character = input("Enter a character: ")
if character in 'aeiouAEIOU':
    print("The character you have entered is a vowel.")
else:
    print("The character you have entered is a consonant.")


#24.
print("\ncheck whether a number is divisible by 5 or not.")
number = int(input("Enter a number: "))
if number % 5 == 0:
    print("The number you have entered is divisible by 5.")
else:
    print("The number you have entered is not divisible by 5.")


#25.
print("\nsimple calculator using if-else statements.")
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. floor division")
print("6. power")
print("7. modulus")

operation = int(input("Enter your choice (1-7): "))

if operation == 1:
    result = num1 + num2
    print("Result:", result)
elif operation == 2:
    result = num1 - num2
    print("Result:", result)
elif operation == 3:
    result = num1 * num2
    print("Result:", result)
elif operation == 4:
    if num2 != 0:
        result = num1 / num2
        print("Result:", result)
    else:
        print("Error: Division by zero is not allowed.")
elif operation == 5:
    if num2 != 0:
        result = num1 // num2
        print("Result:", result)
    else:
        print("Error: Division by zero is not allowed.")
elif operation == 6:
    result = num1 ** num2
    print("Result:", result)
elif operation == 7:
    if num2 != 0:
        result = num1 % num2
        print("Result:", result)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid choice.")