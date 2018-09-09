from time import sleep


#starts the presentation 

print("The Starter - Array \n")
sleep(1)

#Explains what arrays are
print("Arrays are basically lists\n")
sleep(2.4)
#How it is started
print("temp = []")
sleep(1)
print("The [] is saying it is an array.")
sleep(2)
#About how it stores and asks the question
print("""
    temp = []
    for i in range(10):
    """)
sleep(1.5)
print("The number in the brackets tells it how many times it should run the question and store the input into 'i'.\n")
sleep(1.5)
print("In this case it is, 'What is the temperature?'\n")

#Waits until you press enter to continue (ask if they understand so far)

while True:
    choice = input("Press enter to continue >>>")

    if choice == "":
        print("Arrays always start by it being defined: (variable name) = [] \n")
        break

#They are definedy
    print("Arrays always start by it being defined: (variable name) = [] \n")
    sleep(3)
#Example of defining
    print("An example of this is: \n")
    sleep(2)
    print("""
    temp = []
    for i in range(24):
    """)
sleep(1.3)
#What the example array is defined as
print("The array above is defined as temp.\n")
sleep(1.6)

#Explains the question section and storing into 'i'
print("On the second line of the array 'for i in range(24)',\n")
sleep(3)
print("It is saying to run the code which is below in the array 24 times and store in the variable 'i'.\n")
sleep(3)
print("Below where you have started the array it will want a question.\n")
sleep(3)
print("In the format, 'variable name = input('Question')\n")
sleep(3)
print("Or if you are using integers(numbers), you will write 'variable name = int(input('Question')\n")
sleep(3)
print("For example, farenheit = int(input('What is the temperature in farenfeit:'))\n")

#Enter to continue
while True:
    choice = input("Press enter to continue >>>")

#Explains what append does
    if choice == "":
        print("Append keeps the array open ready to add the integers or variables and says where to get them from(If you want to put a value in a certain place in a list, use can use insert.)\n")
        break

#Last section of the array(print and it looking in 'i' in 'temp'
sleep(1.5)
print("Once it has ran 24 times(for the example) in this case it will go to next.")
sleep(2)
print("This will then read what is in 'i' in 'temp' then print whatever is there.\n")

#Opens array.py(example). Open seperaterly if you want to
while True:
    choice = input("Press enter to open full example >>>")

    if choice == "":
        print("Explain what the example is doing for each line of code.")
        sleep(5)
        print("\n\n\n")
        import array
        break







