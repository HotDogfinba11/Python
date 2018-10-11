import random

global score
global score1

score = 0
score1 = 0

def player2():
    global score
    dice1 = random.randint(1,6)
    print(name1,"`s first dice is rolling")

    dice2 = random.randint(1,6)
    print(name1,"`s second dice is rolling")

    dicetot = dice1+dice2

    if(dicetot %2 == 0):
        score +=10
        print(score)

def start():
    global name
    global name1
    name1 = input("Enter first players name >>> \n")#user input is assigned to 
    name2 = input("Enter second players name >>> \n")
    print("Hello",name,"and",name1)
    player2()



start()
