###q1
print("\nQ1. Develop a program that divides two numbers provided by the user.Use try ... except to handle division by zero.")
try:
    a= float(input("Enter first number:"))
    b= float(input("Enter second number:"))

    result= a / b
    print(f"Division of {a} and {b} is : {result}")

except ZeroDivisionError:
    print("Error: Number cannot divide by zero. ")
    
####q2
print("\nQ.2 Write a program that tries to access an element in a list at a non-existent index.Handle the exception using try ... except.")
try:
    numbers = [10 ,20 ,30 , 40 ,50]
    index = int(input("\nEnter list index : "))
    print("Element :", numbers[index] )

except IndexError:
    print("Error: Index does not exist. ")
except ValueError:
    print("Error: Enter a valid integer index.")
    

###q3
print("\nQ.3 Write a program to input a filename from the user, read its content, and handle any file-related exceptions.Use the else block to print the file content if no exception occurs.")
try:
    filename = input("Enter filename :")
    file = open(filename , "r")
    content = file.read()

except FileNotFoundError:
    print("Error: File Not Found.")

else:
    print("File Content:")
    print(content)
    file.close()

###q4
print("\nQ.4 Write a program that tries to access an element in a string at a non-existent index.Handle exceptions, and use the else block to print the result if no exception occurs.")
try:
    fruits = ["banana","apple","orange","watermelon","mango"]
    index = int(input("\nEnter list index : "))
    print("Element :", fruits[index] )

except IndexError:
    print("Error: Index does not exist. ")
except ValueError:
    print("Error: Enter a valid integer index.")


###q5
print("\nQ.5 Write a program that opens a file, handles any exceptions if the file doesn’t exist, and ensures the file is closed using the finally block.")

try:
    filename = input("\nEnter Filename: ")
    file = open(filename ,"r")
    content = file.read()
    print("------ File content ------\n",content)

except FileNotFoundError:
    print("Error : File doesn't exist.")

finally :
    file.close()

##q6
print("\nQ.6 Create a program that performs division.Handle exceptions for invalid inputs and ensure a final message is displayed using the finally block, regardless of the outcome.")
try:
    a= float(input("Enter first number:"))
    b= float(input("Enter second number:"))

    result= a / b
    

except ZeroDivisionError:
    print("Error: Number cannot divide by zero. ")

except ValueError:
    print("Error: Invalid input .You don't enter string instead of use numbers or decimals.")

finally:
    print(f"Division of {a} and {b} is : {result}")

print("Q.7 Write a program that prompts the user to enter a number and attempts to find its square root.Use try to handle invalid input (e.g., negative numbers), else to print the square root if successful, and finally to display a message like 'Execution complete.'")


import math

try:
  number = float(input("Enter a number:"))
  if number < 0:
    raise ValueError("Negative number is not allowed.")
except ValueError as e:
  print("Error:" , e)
else:
  print("Square Root:" , math.sqrt(number))
finally:
  print("Execution complete.")    

    










