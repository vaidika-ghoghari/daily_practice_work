#1.print 1 to 20 and skip number divisible by 4.

for i in range(1,21):
    if i  % 4 ==0 :
        continue
    print(i)

print("-"*50)

#2.stop the while loop using break while number is 7

i=1

while 1<=10:
    if i==7:
        break
    print(i)
    i+=1
    
print("-"*50)
#3.use continue keyword for to skip vowels in python
str="PYTHON"

for element in str:
    if element in "AEIOU"  :
        continue
    else:
        print(element)
        
print("-"*50)
#4.print multiplication tabel

n=int(input("\nWhich tabel you want : "))
i=1
for i in range(1,11):
    print(f"{n}  x  {i} = ",n*i)

print("-"*50)
#5.print right angled numeric pattern .
    

for i in range(1,6):

    for i in range(i):
        print( i+1,end=" "  )

    print("\n")

print("-"*50)

#6..print right angled numeric pattern .
    
for i in range(5,0,-1):

    for j in range(5,i-1,-1):
        print( j ,end=" "  )

    print()
    
print("-"*50)

#7.print right angled numeric pattern 5 to 1 .
    
for i in range(5,0,-1):

    for j in range(i,6):
        print( j ,end=" "  )

    print()
    
print("-"*50)

#8.print right angled numeric pattern .
    
for i in range(1,6):

    for j in range(i,6):
        print( j ,end=" "  )

    print()
    
print("-"*50)
