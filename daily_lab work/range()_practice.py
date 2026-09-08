#1.

while True:
    n=int(input("Enter number : "))

    if n == 0:
        break
    print(f"you entered {n} .")

print("Program end.")

#2.
("\n\nprint 1-10 number and their square ")
for i in range(1,11):
    print("\n",i)
    print( i*i)

#3.
print("\n\neven numbers between 1 to 50.")
i=2

while i<=50:
    if  i % 2 ==0:
        print(i,end="  ")
    i +=2

#4.
print("\n\nprint 1 to 20 and odd numbers.")
for i in range(1,21):
    print(i,end="  ")

for i in range(1,21,2):
    print(i,end="  ")

#5.
print("\n\nuse range() to print multiples of 5 from 5 to 50.")

for i in range(5,51,5):
    print(i,end="  ")

#6.
print("\n\nprint a reverse countdown 10 to 1.")

for i in range(10,0,-1):
    print(i)

#7.
print("\n\nprint number from 1 to 50 using for loop and then check if each number is divisible by 2, 3 or both.")

for i in range(1,51):
    print(i,end="  ")
    
    if i %2 == 0 and i %3 == 0:
        print("Divisible by both.")
    elif  i % 2 == 0:
        print("Divisible by 2.")
    elif  i % 3 == 0:
        print("Divisible by 3.")
    else:
        print("Don't divisible by 2 & 3.")
