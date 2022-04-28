print("Welcome to Ashish's calculator!!")
def value():
    print("Available operations are: \n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Modulus\n6.Power\n7.Square\n8.Cube\n9.Square Root\n10.Cube Root")
    val = int(input("Enter your choice : "))
    return val

def add(x,y):
    return(x+y)
def sub(x,y):
    return(x-y)
def mul(x,y):
    return(x*y)
def div(x,y):
    return(x/y)
def mod(x,y):
    return(x%y)
def pow(x,y):
    return(x**y)
def sqr(x):
    return(x**2 )
def cub(x):
    return(x**3)
def sqroot(x):
    return(x**(1/2))
def cubroot(x):
    return(x**(1/3))
           
def user():
    ch = int(input("Which values do you want to enter : \n 1. integer \n 2. float\n"))
    while(ch):
        if ch == 1:
            a = int(input("Enter the 1st number : "))
            b = int(input("Enter the 2nd number : "))
            break
        elif ch==2:
            a = float(input("Enter the 1st number : "))
            b = float(input("Enter the 2nd number : "))
            break
        else:
            print("Error!! Invalid choice")
            break
    return a,b

def user1():
    ch = int(input("Which values do you want to enter : \n 1. integer \n 2. float\n"))
    while(ch):
        if ch == 1:
            a = int(input("Enter the the number : "))
            break
        elif ch==2:
            a = float(input("Enter the the number : "))
            break
        else:
            print("Error!! Invalid choice")
            break
    return a


def cal():
    val=value()
    while True:
       
        if val==1:
            a,b=user()
            print(a," + ",b," = ",add(a,b))
            break
        elif val==2:
            a,b=user()
            print(a," - ",b," = ",sub(a,b))
            break
        elif val==3:
            a,b=user()
            print(a," * ",b," = ",mul(a,b))
            break
        elif val==4:
            a,b=user()
            if b!=0:
                print(a," / ",b," = ",div(a,b))
                break
            else:
                print("The second operand is zero.\nZero divison error!!")
                break
        elif val==5:
            a,b=user()
            print(a," % ",b," = ",mod(a,b))
            break
        elif val==6:
            a,b=user()
            print(a," ** ",b," = ",pow(a,b))
            break
        elif val==7:
            a=user1()
            print(a," squre is = ",sqr(a))
            break
        elif val==8:
            a=user1()
            print(a," cube is = ",cub(a))
            break
        elif val==9:
            a=user1()
            print(a," sqr root  ",sqroot(a))
            break
        elif val==10:
            a=user1()
            print(a," cube root  = ",cubroot(a))     
            break
        else:
            print("Invalid Choice!")
            print("Please enter a valid choice: ")
            break


cal()

while True:
    next_calculation = input("Let's do next calculation? (yes/no): ")
    if next_calculation == "yes":
        print(cal())
    else:
        print("Thank you")
        break

      
