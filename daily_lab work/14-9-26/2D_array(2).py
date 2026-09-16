'''
#q.4.
print("Q-4. find min and max value in 2D array.")

arr=[]

n=int(input("\nEnter the size of array : "))

for i in range(n):
    elements=list(map(int,input(f"Enter arr[{i}] :").split()))
    arr.append(elements)

for elements in arr:
    print("\n",elements , end="\t")

print("\nminimum value of array is : ", min(elements))
print("maximum value of array is : ", max(elements))

print("--"*50)

#q.5.
print("Q-5.create list of integers and sort it using sort() method.")

list1=[12,45,89,46,72,78,34,94,65,67]

print("Unsorted list :",list1)
list1.sort()
print("Sorted list :",list1)

print("--"*50)

#q.6.
print("\nQ-6.sort a list of tuples based on the second element of each tuples.")

marks=[
    (1,7.45),
    (2,7.14),
    (3,7.00),
    (4,6.86),
    (5,6.55),
    (6,7.81)
    ]

sorted=sorted(marks ,key= lambda x: x[1],reverse=True)
print("\nSorted second element :",sorted)

print("--"*50)
'''

#q.7.
print("\nQ-7.sort a list of dictionary by a specific key uing the sorted().")

student=[
    {"name" : "Vaidika"},
    {"age" : 20},
    {"course" : "Python"},
    ]

sorted=sorted(student , key =lambda x: x,reverse=False)
print(sorted)




