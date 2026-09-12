'''
#q.1.
print("q.1.Create a 3x3 matrix.")
arr=[]
for i in range(3):
    element=list(map(int,input(f"Enter row {i+1}:").split()))
    arr.append(element)

print(arr)

for element in arr:
    for value in element:
        print(value,end="\t")
    print()

print("--"*50)

#q.2.
print("\n q.2. transpose 2x3 into 3x2.")
arr=[]
for i in range(2):
    element=list(map(int,input(f"Enter row {i+1}:").split()))
    arr.append(element)

print(arr)

transposed=[]

for j in range(3):
    temp=[]
    for i in range(2):
        temp.append(arr[i][j])
    transposed.append(temp)

for element in transposed:
        print(element)

print("--"*50)
'''
#q.3.
print("\nq.3.sum of all element in array.")

n=int(input("Enter the size of array:"))
arr=[]
for i in range(n):
    element=list(map(int,input(f"Enter row {i+1}:").split()))
    arr.append(element)

print(arr)
total=0
for element in arr:
    for i in element:
        total+=i

print(total)
        
