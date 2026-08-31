print("Q-5. declare two variables with same value and print their memory address.")

a=20
b=20

print("The value of a :",a , "  Memory address : ",id(a))
print("The value of b :",b ,"  Memory address : ",id(b))

b=10
print ("After modification value of b: ",b,"  Memory address : ",id(b))
