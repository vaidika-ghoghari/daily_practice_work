#1. 
print("Hello, World!")

#2.
print("sum of two numbers")
n1=int(input("Enter first number: "))
n2=int(input("Enter second number: "))
sum=n1+n2   
print(f"The sum of {n1} and {n2} is: {sum}")

#3.
print(" \ndifference of two numbers")
n1=int(input("Enter first number: "))       
n2=int(input("Enter second number: "))
sub=n1-n2
print(f"The difference of {n1} and {n2} is: {sub}") 

#4.
print(" \nmultiplication of two numbers")
n1=int(input("Enter first number: "))       
n2=int(input("Enter second number: "))
sub=n1*n2
print(f"The multiplication of {n1} and {n2} is: {sub}") 

#5.
print(" \ndivision of two numbers")
n1=int(input("Enter first number: "))       
n2=int(input("Enter second number: "))
sub=n1/n2
print(f"The division of {n1} and {n2} is: {sub}")

#6.
print("\n remainder of two numbers")
n1=int(input(" Enter first number: "))       
n2=int(input("Enter second number: "))
sub=n1%n2
print(f"The remainder of {n1} and {n2} is: {sub}") 

#7.
print("\n square of a number")
num=int(input(" Enter a number: "))
square=num*num
print(f"The square of {num} is: {square}")

#8
print("\ncube of a number")
num=int(input("Enter a number: "))
cube=num*num*num
print(f"The cube of {num} is: {cube}")  

#9.
print("area of a circle")
r=float(input("\nEnter the radius of the circle: "))
area=3.14*r*r   
print(f"The area of the circle with radius {r} is: {area}")

#10.
print("calculate simple interest")
p=float(input("\nEnter the principal amount: "))
t=float(input("Enter the time in years: ")) 
r=float(input("Enter the rate of interest: "))
si=(p*t*r)/100
print(f"The simple interest for principal amount {p}, time {t} years, and rate {r}% is: {si}")

#11.
print("\nconvert temperature from Celsius to Fahrenheit")
celsius=float(input("Enter the temperature in Celsius: "))      
fernheit=(celsius*9/5)+32
print(f"The temperature in Fahrenheit is: {fernheit}")

#12.
print("\nswap two numbers")
n1=int(input("Enter first number: "))
n2=int(input("Enter second number: "))
print(f"Before swapping: n1 = {n1}, n2 = {n2}")
n1,n2=n2,n1
print(f"After swapping: n1 = {n1}, n2 = {n2}")

#13.
print("\nfind average of three numbers")
n1=int(input("Enter first number: "))
n2=int(input("Enter second number: "))
n3=int(input("Enter third number: "))
avg=(n1+n2+n3)/3
print(f"The average of {n1}, {n2}, and {n3} is: {avg}")

#14.
print("\ncalculate total marks and percentage of a student")
subject1=int(input("Enter marks of subject 1: "))
subject2=int(input("Enter marks of subject 2: "))
subject3=int(input("Enter marks of subject 3: "))
total_marks=subject1+subject2+subject3
percentage=(total_marks/300)*100
print(f"The percentage of the student is: {percentage}")

#15.
print("\nconvert days into years, months and days")
days=int(input("Enter the number of days: "))
years=days//365
months=(days%365)//30
remaining_days=(days%365)%30
print("years:",years,"\nmonths:",months,"\ndays:",remaining_days)
