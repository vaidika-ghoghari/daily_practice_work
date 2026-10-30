
#1.
print("find max number among in three")

n1=int(input("Enter a first number :"))
n2=int(input("Enter a second number :"))
n3=int(input("Enter a third number :"))

if n1 >n2:
    if n1>n3:
                print(f"First number {n1} is maximum number among of all.")
    else :
        print(f"Third number {n3} is maximum number among of all.")

else:
    
    if n2> n3:
         print(f"Sceond number {n2} is maximum number among of all.")
    else:
        print(f"Third number {n3} is maximum number among of all.")


#2.

print("\n\nfind minj number among in three")

n1=int(input("Enter a first number :"))
n2=int(input("Enter a second number :"))
n3=int(input("Enter a third number :"))

if n1 <n2:
    if n1<n3:
                print(f"First number {n1} is minimum number among of all.")
    else :
        print(f"Third number {n3} is minimum number among of all.")

else:
    
    if n2<n3:
         print(f"Sceond number {n2} is minimum number among of all.")
    else:
        print(f"Third number {n3} is minimum number among of all.")


#3.
print("\n\nfind max number among in four")

n1=int(input("Enter a first number :"))
n2=int(input("Enter a second number :"))
n3=int(input("Enter a third number :"))
n4=int(input("Enter a forth number :"))

if n1 >n2:
    if n1>n3:
        if n1> n4:
            print(f"First number {n1} is maximum number among of all.")
        else :
            print(f"Third number {n4} is maximum number among of all.")
    else:
        print(f"Third number {n3} is maximum number among of all.")
else:
    if n2> n3:
        if n2 > n4:
             print(f"Sceond number {n2} is maximum number among of all.")
        else:
            print(f"Third number {n4} is maximum number among of all.")
    else:
        print(f"Third number {n3} is maximum number among of all.")



#4.
print("\n\nperform arithmetic operator using switch -case.")

print("\n1. Addition (+)")
print("2. subtraction (-)")
print("3. multiplcation (*)")
print("4. division ( / )")
choice=input("Enter your choice between(1 - 4) : ")

a=int(input("Enter a first value : "))
b=int(input("enter a second value : "))

match choice:
    case "1":
        print("the addition of two number is ", a + b)
    case "2":
        print("the subtraction of two number is ", a-b)
    case "3":
        print("the multiplication of two number is ", a*b)
    case "4":
        print("the division of two number is ", a/b)
    case _:
        print(" Invalid input...")



#5.
print("menu-drivem program for fast-food order system using match case.")


print("\nPrees 1 to order a Sandwich")
print("Prees 2 to order a Pizza")
print("Prees 3 to order a Burger")
choice=input("Enter your choice between(1 - 3) : ")

match choice:
    case "1":
        print("\nPress 1 for Cheese Sandwich ")
        print("Press 2 for Mayonise Sandwich ")
        print("Press 3 for panner Sandwich ")
        sandwich=input("Enter your choice between(1 - 3) : ")

        match sandwich:
            case "1":
                print("You ordered a cheese sandwich.")
            case "2":
                print("You ordered a Mayonise sandwich.")
            case "3":
                print("You ordered a panner sandwich.")
            case _:
                print("You Enetred a wrong choice....")


    case "2":
        print("\nPress 1 for Thin Crust Pizza")
        print("Press 2 for Cheese Brust Pizza  ")
        print("Press 3 for Fresh Dough Pizza  ")
        pizza=input("Enter your choice between(1 - 3) : ")

        match pizza:
            case "1":
                print("You ordered a Thin Crust Pizza.")
            case "2":
                print("You ordered a Cheese Brust Pizza.")
            case "3":
                print("You ordered a Fresh Dough Pizza.")
            case _:
                print("You Enetred a wrong choice....")

    case "3":
        print("\nPress 1 for Veggie Burger")
        print("Press 2 for Cheese Burger  ")
        print("Press 3 for Allu Tikki Burger  ")
        burger=input("Enter your choice between(1 - 3) : ")

        match burger:
            case "1":
                print("You ordered a Veggie Burger.")
            case "2":
                print("You ordered a Cheese Burger.")
            case "3":
                print("You ordered a Allu Tikki Burger.")
            case _:
                print("You Enetred a wrong choice....")

    case _:
        print("Invalid choice...!")


#6.
        
print("\n\nmenu-drivem program for telecome calling system using match case.")


print("\nPrees 1 for English")
print("Prees 2 for Hindi")
print("Prees 3 for Gujarati")
choice=input("Enter your choice between(1 - 3) : ")

match choice:
    case "1":
        print("\nPress 1 for voice call ")
        print("Press 2 for video call ")
        print("Press 3 for conference call")
        english=input("Enter your choice between(1 - 3) : ")

        match english:
            case "1":
                print("You selected English and You selected a Voice call.")
            case "2":
                print("You selected English and You selected a video call")
            case "3":
                print("You selected English and You selected a conference call.")
            case _:
                print("You Enetred a wrong choice....")


    case "2":
        print("\nPress 1 for voice call")
        print("Press 2 for video call  ")
        print("Press 3 for conference call  ")
        hindi=input("Enter your choice between(1 - 3) : ")

        match hindi:
            case "1":
                print("You selected hindi and You selected a Voice call.")
            case "2":
                print("You selected hindi and You selected a video call.")
            case "3":
                print("You selected hindi and You selected a conference call.")
            case _:
                print("You Enetred a wrong choice....")

    case "3":
        print("\nPress 1 for voice call")
        print("Press 2 for video call  ")
        print("Press 3 forconference call ")
        gujarati=input("Enter your choice between(1 - 3) : ")

        match gujarati:
            case "1":
                print("You selected gujarati and You selected a Voice call.")
            case "2":
                print("You selected gujarati and You selected a video call.")
            case "3":
                print("You selected gujarati and You selected a conference call.")
            case _:
                print("You Enetred a wrong choice....")

    case _:
        print("Invalid choice...!")
    






        
