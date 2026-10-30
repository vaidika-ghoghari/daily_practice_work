
print("Q-1.  personal info of user.")

print("name","age", sep=" | ")
print("vaidika","20",sep=" | ")

print("hello ! ",end=" ")
print("my name is vaidika.")

print("Q-2.  personal info of user.")

name= input("Enter your name: ")
age= input("Enter your age: ")
hobby= input("Enter your hobby: ")

print(f"Hello ,{name} ! At {age} , enjoying {hobby} sounds fun !")


print("~"*60)

#####
print("Q-3.  Arithmetic operators")


n1=int(input("Enter first number :"))
n2=int(input("Enter second number :"))

print("1. addition", n1+n2)
print("2. subtraction", n1-n2)
print("3. multiplication", n1*n2)
print("4. division", n1/n2)
print("5. floor division", n1//n2)
print("6. moduls", n1**n2 )


print("~"*60)

####

print("Q-4. declare variables and print thier type through type().")

var1= 100
var2 = 3.14
var3 = "vaidika"
var4 = True
var5 = 4 +3j
print(type( var1))
print(type( var2))
print(type( var3))
print(type( var4))
print(type( var5))



print("~"*60)


####
print("Q-5. take user input of height & weight and display it.")

height=int(input("Enter your height in cm :"))
weight=int(input("Enter your weight in kg :"))

print(f"This is the your height in cm  {height}.")
print(f"This is the your weight in cm  {weight}.")



print("~"*60)


#####

print("Q-6.Asking user for input in bool values and demonstrate logical operator.")

a=input("Eneter first input :")
b=input("Eneter second input :")
print("a : ", a )
print("b :", b )
print("a and b :", a and b)
print("a or b :", a or b)
print(" not a :", not a )
print(" not b  :", not b)






#####


print("Q-7. assignment operater")


a = 60
print("1. Assignment operater  / print the value of A :", a)
a += 5
print("2. add & assign operater :" , a)
a -= 3
print("3.  subtract & assign operater :",a )
a *= 2
print("4.  multiply & assign operater :",a )
a /= 9
print("5.  divide & assign operater :",a )
a //= 2
print("6.  floor division & assign operater :",a )
a **= 3
print("7.  moduls & assign operater :", a)









