def Add(x,y):
     return x+y
def Subtract(x,y):
     return x-y 
def Multiply(x,y):
     return x*y
def Divide(x,y):
    return x/y

import math
def LOG(x,y):
    return math.log(x)/math.log(y)
print("select operation:")
print("1.ADD")
print("2.SUBTRACT")
print("3.MULTIPLY")
print("4.DIVIDE")
print("5.LOG")

while True:
    operation=input("ENTER operation(1/2/3/4/5):")

    if operation in operation:
        try:
            num1=float(input("Enter x:"))
            num2=float(input("Enter y:"))
        except ValueError:
            print("invalid output.Please try with integers")
            continue

        if operation=='1':
            print(num1,"+",num2,"=",Add(num1,num2))
        elif operation=='2':
            print(num1,"-",num2,"=",Subtract(num1,num2))
        elif operation=='3':
            print(num1,"*",num2,"=",Multiply(num1,num2))
        elif operation=='4':
            print(num1,"/",num2,"=",Divide(num1,num2))
        elif operation=='5':
            print(math.log(num1,num2))
    
    #niche wala internet say guide liya hai
        NEXT_CALCULATION=input("lets do another one?(Y/N):")
        if NEXT_CALCULATION=="N":
            break
             