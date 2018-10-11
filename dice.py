import random
import time
from time import sleep

global dicetot
global dicetot1
global name
global name1


def compare():
    global dicetot
    global dicetot1
    global name
    global name1
    if(dicetot > dicetot1):
        print(name,"won")#prints variable and won
        print("He got ",dicetot)
        again = input("Want to play again? Y/N>>>\n") #asks to run the program again
        if (again == "y"):
            player1()#runs def player1 if input is y
        else:
            print("Thanks for playing")
    else:
        print(name1,"won")
        print("He got ",dicetot1)
            


def player2():
    global dicetot
    global dicetot1
    dice = random.randint(1,6)
    sleep(1)
    print(name1,"`s first dice is rolling")
    sleep(1)
    print("He got",dice)
    dice1 = random.randint(1,6)
    sleep(1)
    print(name1,"`s second dice is rolling")
    sleep(1)
    print("He got",dice1)
    if(dice == dice1): #compares the two variables
        print("Both outcomes were",dice)
        sleep(1)
        print(name1,"`s third dice is rolling")
        dice2 = random.randint(1,6)
        print("He got",dice2)
        dicetot1 = dice + dice1 + dice2

    else:
        dicetot1 = dice + dice1
        compare()

def player1():
    global dicetot
    global dicetot1
    dice = random.randint(1,6)#pseudo-random number assigned to dice
    sleep(1)
    print(name,"`s first dice is rolling")#prints the dice output
    sleep(1)
    print("He got",dice)
    dice1 = random.randint(1,6)
    sleep(1)
    print(name,"`s second dice is rolling")
    sleep(1)
    print("He got",dice1)
    if(dice == dice1):
        print("Both outcomes were",dice)
        sleep(1)
        print(name1,"`s third dice is rolling")
        dice2 = random.randint(1,6)
        print("He got",dice2)
        dicetot = dice + dice1 + dice2#adds variables, dice, dice1, dice2 and assigns to dicetot
        player2()
        
    else:
        dicetot = dice + dice1
        player2()
            
def start():
    global name
    global name1
    name = input("Enter first players name >>> \n")#user input is assigned to 
    name1 = input("Enter second players name >>> \n")
    print("Hello",name,"and",name1)
    player1()



start()
