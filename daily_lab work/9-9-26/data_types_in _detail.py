
#Q-1.
print("Q.1.Take user input and print it in given format.")

fname=input("Enter the first name : ")
lname=input("Enter the last name : ")

print(f"\nHello, {lname}, {fname} ! ")

print("--"*30)

#q.2.
print("Q.2.Display the setence in given format using f-String.")

item="apple"
price=5.50

print("Formated string:")
print(f"\nThe price of {item} is {price} dollars.")

print("--"*30)

#q.3.
print("\nTake string as input and reversed it and also check it sis palindomr or not.")

str =input("Enter a string :")

reverse=str[::-1]

print(reverse)

if str == reverse:
    print("\nThis string is palindrome.")
else:
     print("\nThis string is not palindrome.")

print("--"*30)


#q.4.
print("\nTake string as input and connvert it into uppercase, lowercase and title case.")

str=input("Enter a string:")

print("\nIn uppercase:",str.upper())
print("In lowercase:",str.lower())
print("In titlecase:",str.title())

print("--"*30)

#q.5.
print("\nUse find and replace in string")

str="Machine Learning and AI are trending"

print("Original  string :",str)

print("Replaced string :", str.replace("AI","Artificial Intelligence"))


str1="data data mining and big data"

print("Original  string :",str1)
print("Count the word 'data':", str1.count("data"))

print("--"*30)


#q.6.
print("\nA.Spilt this string in list")

str="apple,banana,grapes"
print("Original string:",str)
print("Converted list:",list(str.split()))


print("\nB.Join the setence in line with space.")

list1=["Python","is","awesome"]
print("Original list :",list1)
print(" ".join(list1))


print("\nC.convert multiline string into a line.")

str1='''hello !
my name is vaidika.
I learning Python.'''

for i in str1.splitlines():
    print(i)

print("Multiline string: ",str1)



print("--"*30)


#Q.7.
print("\nA. check the string that starts with'Hello' andf end with'world'.")
str="Hello !!! World"
print(str)

if "Hello" in str[:5] and "World"  in str[-5:]:
    print("Congrates...! It's match.")
else:
    print("Opps...! It's not match.")


print("\nB. Remove all non-alphabetic character from given string. ")
str1="Data123#Science"
print("String :",str1)

result=""

for ch in str1:
    if ch.isalpha():
        result += ch

print(result)

print("\nC.reverse a python string")

str="Python"

print(str[::-1])
print("--"*30)
print("--"*30)
