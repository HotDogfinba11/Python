#default username - oliver
#default password - oliver

import random
import time
from time import sleep

global score1
global score2
global counter

score1 = 0
score2 = 0
counter = 5


def score():
    global score1
    global score2

    score1 = str(score1)
    score2 = str(score2)
    
    if(score1 > score2):
        score = open("score.txt","a")
        score.write(score1)
        score.write(" ")
        score.write(name1)
        score.write("\n")
        score.close()
    elif(score1 < score2):
        score = open("score.txt","a")
        score.write(score2)
        score.write()
        score.write(name2)
        score.write("\n")
        score.close()

        
def end():
    global score1
    global score2
    if(score1 == score2):
        player1()
    elif(score1 > score2):
        print(name1,"got a higher score than",name2,"with",score1,"points")
        score()
    elif(score1 < score2):
        print(name2,"got a higher score than",name1,"with",score2  ,"points")
        score()


def main():
    while counter != 0:

        def player2():
            global score2
            global counter
            global name2
            dice1 = random.randint(1,6)
            print(name2,"`s first dice is rolling and got",dice1)
            sleep(1)
            dice2 = random.randint(1,6)
            print(name2,"`s second dice is rolling and got",dice2)
            sleep(1)

            if(dice1 == dice2):
                dice3 = random.randint(1,6)
                dicetot = dice1 + dice2 + dice3
            else:
                dicetot = dice1+dice2

            print("Giving a total of",dicetot)
            if(dicetot %2 == 0):
                score2 +=10

            if dicetot in range(2,5):
                score2 += 3
            elif dicetot in range(6,9):
                score2 += 5
            elif dicetot in range(10,12):
                score2 += 7
            elif dicetot in range(13,18):
                score1 += 9

            sleep(1)
            print(name2,"`s score is now",score2)
            counter -=1


        def player1():
            global score1
            global name1
            dice1 = random.randint(1,6)
            print(name1,"`s first dice is rolling and got",dice1)
            sleep(1)
            dice2 = random.randint(1,6)
            print(name1,"`s second dice is rolling and got",dice2)
            sleep(1)

            if(dice1 == dice2):
                dice3 = random.randint(1,6)
                dicetot = dice1 + dice2 + dice3
            else:
                dicetot = dice1+dice2


            print("Giving a total of",dicetot)
            if(dicetot %2 == 0):
                score1 +=10

            if dicetot in range(2,5):
                score1 += 3
            elif dicetot in range(6,9):
                score1 += 5
            elif dicetot in range(10,12):
                score1 += 7
            elif dicetot in range(13,18):
                score1 += 9

            sleep(1)
            print(name1,"`s score is now",score1)

            player2()

        player1()

    if counter == 0:
        if(score1 == score2):
            player1()
        else:
            score()
            end()

def start():
    global name1
    global name2
    print("Enter first players name")
    name1 = input(">>> ")
    print("Enter second players name")
    name2 = input(">>> ")
    print("Hello",name1,"and",name2)
    main()


def login():
    error = 0
    running = True


    while running:
            print("Type 'user' to change username and password.")
            print("Type 'quit' to leave program.")
            print("Type 'score' to show scoreboard")
            print("Type 'run' to execute program.")
            cmd = input("//")

            if(cmd == "user"):
                    print("Fill in the following.")
                    new_usr = input("New Username: ")
                    newusr = open("username.txt", "w")
                    newusr.write(new_usr)
                    newusr.close()

                    new_psw = input("New Password: ")
                    newpsw = open("password.txt", "w")
                    newpsw.write(new_psw)
                    newpsw.close()

            if(cmd == "quit"):
                    sleep(1)
                    running = False

            if(cmd == "score"):
                score = open("score.txt","r")
                score = score.read()
                print(score)

            
            if(cmd == "run"):
                username = open("username.txt","r")
                usr_read = username.read()
                username.close()

                password = open("password.txt","r")
                psw_read = password.read()
                password.close()

                usr_user = input("Username: ")
                if usr_user == usr_read:
                    pass


                usr_pass = input("Password: ")
                if usr_pass == psw_read:
                        pass
                else:
                    error = 1

                if error == 1:
                        print("error", random.randrange(1, 102))
                        sleep(1)
                        quit()
                else:
                    start()

                        

login()
