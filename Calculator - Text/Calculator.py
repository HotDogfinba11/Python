import getpass
from time import sleep
import sys
import hashlib
import getpass
import csv
import sys



Author = "Oliver"
Version = "Version 1.0"
Name = "Zenflex®"
print(Name + " -" + "\nVersion: " + Version + "\nAuthor: " + Author)


def add(x, y):
   return x + y

def subtract(x, y):
   return x - y

def multiply(x, y):
   return x * y

def divide(x, y):
   return x / y


def calculator():
    sleep(0.7)
    print("Select operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")

    choice = input("Enter choice(1/2/3/4):\n")

    sleep(0.3)
    num1 = float(input("Enter first number: "))
    sleep(0.3)
    num2 = float(input("Enter second number: "))

    if choice == '1':
       print(num1,"+",num2,"=", add(num1,num2))

    elif choice == '2':
       print(num1,"-",num2,"=", subtract(num1,num2))

    elif choice == '3':
       print(num1,"*",num2,"=", multiply(num1,num2))

    elif choice == '4':
       print(num1,"/",num2,"=", divide(num1,num2))
    else:
       print("Invalid input")

login()

