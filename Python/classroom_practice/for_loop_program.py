
#26.

print("print numbers from 1 to 10.")

for i in range(1,11):
    print( i )


#27.
print("\nprint numbers from 10 to 1.")

for i in range(10,0,-1):
    print(i)


#28.
print("\nprint even numbers from 1 to 50.")

for i in range(2,51,2):
    print(i)


#29.
print("\nprint odd numbers from 1 to 50.")

for i in range(1,50,2):
    print(i)


#30.
print("\nprint multiplication tabel.")

n=int(input("\nEnter the number :"))

for i in range(1, 11):
    print(n, "x", i ,"=", n *i)


#31.
print("\nfind sum of numbers from 1 to N.")

n=int(input("\nEnter the number :"))

sum=0

for i in range(1, n+1):
    sum += i

print("Sum= ", sum)




#32.
print("\nfind factorial of numbers from 1 to N.")

n=int(input("\nEnter the number :"))

factorial=1

for i in range(1, n+1):
    factorial *= i

print("Factorial= ", factorial)


#33.
print("\nCount digit  of numbers from 1 to N.")

n=int(input("\nEnter the number :"))

digit=0

for i in str(n):
    digit +=  1

print("Number of digit= ", digit)


#34.
print("Reverse a number.")
n=input("\nEnter the number :")
rev=""

for i in n:
    rev = i+ rev

    
print("Reverse number :",rev)

#35.
print("\nprint fibbonacci series.")

n=int(input("\nEnter the number of terms:"))
a=0
b=1

for i in range(n):
    print(a ,end ="  ")
    a,b= b,a+b

#36.

print("\nCheck whether the number is prime.")

n=int(input("\nEnter the number:"))
a=0

for i in range(1,n+1):
    if n % i == 0:
        a+=1

if a==2:
    print("this is a prime number.")
else:
    print("this isn't a prime number.")

    
#37.

print("\n print all prime numbers between 1 to 100.")


a=0

for n in range(2,101):
    count= 0

    for i in range(1, n+1):
        if n%i ==0:
            count += 1

    if count == 2:
        print(n, end="  ")
    


#38.
print("\n Sum digit  of numbers.")

n=int(input("\nEnter the number :"))

digit=0

for i in str(n):
    digit +=int(i)

print("sum of digit= ", digit)

#39.
print("\n find largest digit  in number.")

n=input("\nEnter the number :")

largest=0
for i in n:
    if int(i) > largest:
        largest= int(i)
    
print("Largest number of digi: ",largest)


''''
#40.
print("print star pattern.")
'''
