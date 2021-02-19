from time import sleep #imports library sleep to add delays for running code

def add(x, y): #creates the 'add' function, asks for num1 and num2 and renames them to 'x' and 'y'
   return x + y #result of adding x (num1) and y (num2) will be sent to the print of where it was used

def subtract(x, y): #creates the 'subtract' function, asks for num1 and num2 and renames them to 'x' and 'y'
   return x - y #result of subtracting x (num1) and y (num2) will be sent to the print of where it was used

def multiply(x, y): #creates the 'multiply' function, asks for num1 and num2 and renames them to 'x' and 'y'
   return x * y #result of multiplying x (num1) and y (num2) will be sent to the print of where it was used

def divide(x, y): #creates the 'divide' function, asks for num1 and num2 and renames them to 'x' and 'y'
   return x / y #result of dividing x (num1) and y (num2) will be sent to the print of where it was used


def calculator(): #main caluclator function, when this is called everything beneath will run line by line
    sleep(0.7) #using imported sleep library, 700ms delay
    print("Select operation.") #prints to user, "select operaton"
    print("1.Add") #prints to user, "add"
    print("2.Subtract") #prints to user, "subtract"
    print("3.Multiply") #prints to user, "multiply"
    print("4.Divide") #prints to user, "divide"

    choice = input("Enter choice(1/2/3/4):\n") #what user writes will be set to choice

    sleep(0.3) #delay of 300ms
    num1 = float(input("Enter first number: ")) #inputted number by user is set to 'num1'
    sleep(0.3) #delay of 300ms
    num2 = float(input("Enter second number: ")) #inputted number by user is set to 'num2'

    if choice == '1': #the value set to choice a few lines up is compared against each if and elif statement until it is true
       print(num1,"+",num2,"=", add(num1,num2)) #outputs to user the sum that they did and then calls the add function giving the values of 'num1' and num2'

    elif choice == '2': #is choice 2
       print(num1,"-",num2,"=", subtract(num1,num2)) #outputs to user the sum that they did and then calls the subtract function giving the values of 'num1' and num2'

    elif choice == '3': #is choice 3
       print(num1,"*",num2,"=", multiply(num1,num2)) #outputs to user the sum that they did and then calls the multiply function giving the values of 'num1' and num2'

    elif choice == '4': #is choice 4
       print(num1,"/",num2,"=", divide(num1,num2)) #outputs to user the sum that they did and then calls the divide function giving the values of 'num1' and num2'
    else: #if what the user inputted when asked for choice doesn't match any of the above, they inputted wrongly
       print("Invalid input") #tells user they entered wrong

calculator() #calls/runs the calculator function