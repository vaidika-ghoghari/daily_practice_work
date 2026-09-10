'''
#q.1.find length of array without built -in function.

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

#q.2.find average without built-in function

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


#q.3.sum of two 1-D array.

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
'''
#q.4.Create an array to print 1 to 10 and multiply by 2 of each element.

arr=[]

for i in range(1,11):
    arr.append(i)

print(arr)

arr2=[]
for i in range(0,10):
    arr2.append(arr[i]*2)

print(arr2)
