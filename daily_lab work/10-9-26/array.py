
#q.1
print("q.1.find length of array without built -in function.")

n=int(input("\nEnter a size of array:"))
a=[]

for i in range(n):
    element=int(input(f"b[{i}] = "))
    a.append(element)

count=0
for element in a:
    count +=1

print("Length of array",count)

print("--"*50)

#q.2.
print("q.2.find average without built-in function.")

n=int(input("\nEnter a array size:"))
a1=[]

for i in range(n):
    element=int(input(f"a1[{i}] :"))
    a1.append(element)

total=0
for element in a1:
    total+=element

print("Average of array :",total/n)

print("--"*50) 


#q.3.
print("q.3.sum of two 1-D array.")

n=int(input("\nEnter a array size:"))
a=[]
b=[]
c=[]

for i in range(n):
    element=int(input(f"a[{i}] : "))
    a.append(element)

for i in range(n):
    element=int(input(f"b[{i}] : "))
    b.append(element)
    
for i in range(n):
    c.append(a[i]+b[i])

print("Sum of two array is :",c)

print("--"*50) 

#q.4.
print("q.4.Create an array to print 1 to 10 and multiply by 2 of each element.")

arr=[]

for i in range(1,11):
    arr.append(i)

print("Array :",arr)

arr2=[]
for i in range(0,10):
    arr2.append(arr[i]*2)

print("With muliplication :",arr2)

print("--"*50) 

#q.5.
print("q.6.whether number is exists in array.")

arr=[10,20,30,40,50,55,65,75,85,95]

n=int(input("\nEnter a number:"))
found = False
for i in range(len(arr)):
    if arr[i]==n:
        print("The index of the element :",i)
        found=True
        break
    
if found==False:
        print("Not found...")
    
print("--"*50) 

#q.6.
print("q.6.print odd and even numbers from user-define array.")

n=int(input("\nEnter a size of array :"))

arr=[]
odd=[]
even=[]

for i in range(n):
    element=int(input(f"arr[{i}] :"))
    arr.append(element)

for element in arr:
    if element % 2 ==0:
        even.append(element)
        
print("Even number list :",even)


for element in arr:
    if element % 2 != 0 :
        odd.append(element)
        
print("Odd number list :",odd)




