#Simple Calculator
from tkinter.constants import TRUE


def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def division(x,y):
    return x / y

print("select operation")
print("1. ADD")
print("2. SUBTRACT")
print("3. MULTIPLY")
print("4. DIVISION")

choice = input("Enter the choice of operation from 1 to 4 :")

while TRUE:
    if choice in('1','2','3','4'):
        num1 = float(input("enter the value of x:"))
        num2 = float(input("enter the value of y:"))
        if choice == '1':
            print("add of two no. =", add(num1, num2))

        elif choice == '2':
            print("subtraction of two no.:", subtract(num1 , num2))

        elif choice == '3':
            print("multiplication of two no.:", multiply(num1 , num2))

        elif choice == '4':
            print('division of two no.:', division(num1, num2))
    
        break
    else:
        print("invalid output")




