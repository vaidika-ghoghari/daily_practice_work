#1
print("check the number is even or odd.")

n1=int(input("Enter a number : "))

if n1 % 2 == 0 :
    print(f"{n1} is a even number.")
else:
    print(f"{n1} is a odd number.")


#2.
print("\n\nThe use of nested 'if-else' statements to categories the user into age gaps.")

age=int(input("Enter  your age :"))

if age <=12:
    print("You are a child.")
elif 13 <= age <=19:
    print("you are a teenager.")
elif 20 <= age <=59:
    print("you are a adult.")
elif age <=60:
    print("you are a senior.")
else:
    print("invalid input.")

#3.
print("\n\nfind the largest numbers among three  with the use of ladder if else.")

n1=int(input("Enter a first number : "))
n2=int(input("Enter a  second number : "))
n3=int(input("Enter a third  number : "))

if n1 > n2 and n1 > n3:
    print(f"First number {n1} is largest number.")
elif n2 > n1 and n2 > n3:
    print(f"Second number {n2} is largest number.")
else :
    print(f"Third number {n3} is largest number.")


#4.
print("\n\ncheck the number is netural number or not without using ladder if .")

n1=int(input("Enter a number : "))

if n1 > 0:
    print(f"the enter number is natural.")
else:
    print("you entered the number is not netural.")

    
    
