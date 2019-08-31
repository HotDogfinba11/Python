from tkinter import *
import tkinter as tk
import random

def game():
    global name1
    global name2
    score1 = 0
    score2 = 0
    rounds = 5

    gameui = tk.Tk()
    gameui.geometry("400x200")
    gameui.title("Dice")
    
    while(rounds > 0):
            dice1 = random.randint(1,6)
            dice2 = random.randint(1,6)
            dice3 = dice1 + dice2
            if(dice3 %2 == 0):
                score1 +=10
            if(dice1 == dice2):
                dice4 = random.randint(1,6)
                score1 += dice4
            if(dice3 %2 != 0):
                score1 -=5
                if(score1 < 0):
                    score1 =0

            score1 += dice3

            if(rounds == 5):
                pr1 = (name1.get(),"got ",score1," first round")
                labelName1 = tk.Label(gameui, text=pr1).grid(row=1, column=1)
            elif(rounds == 4):
                pr1 = (name1.get(),"got ",score1," second round")
                labelName1 = tk.Label(gameui, text=pr1).grid(row=3, column=1)
            elif(rounds == 3):
                pr1 = (name1.get(),"got ",score1,"third round")
                labelName1 = tk.Label(gameui, text=pr1).grid(row=5, column=1)
            elif(rounds == 2):
                pr1 = (name1.get(),"got ",score1," fourth round")
                labelName1 = tk.Label(gameui, text=pr1).grid(row=7, column=1)
            elif(rounds == 1):
                pr1 = (name1.get(),"got ",score1," last round")
                labelName1 = tk.Label(gameui, text=pr1).grid(row=9, column=1)

            player1 = False
                
            while(player1 == False):
                dice1 = random.randint(1,6)
                dice2 = random.randint(1,6)
                dice3 = dice1 + dice2
                if(dice3 %2 == 0):
                    score2 +=10
                if(dice1 == dice2):
                    dice4 = random.randint(1,6)
                    score2 += dice4
                if(dice3 %2 != 0):
                    score2 -=5
                    if(score1 < 0):
                       score2 =0

                score2 += dice3

                if(rounds == 5):
                    pr1 = (name2.get(),"got ",score2," first round")
                    labelName1 = tk.Label(gameui, text=pr1).grid(row=2, column=1)
                elif(rounds == 4):
                    pr1 = (name2.get(),"got ",score2," second round")
                    labelName1 = tk.Label(gameui, text=pr1).grid(row=4, column=1)
                elif(rounds == 3):
                    pr1 = (name2.get(),"got ",score2,"third round")
                    labelName1 = tk.Label(gameui, text=pr1).grid(row=6, column=1)
                elif(rounds == 2):
                    pr1 = (name2.get(),"got ",score2," fourth round")
                    labelName1 = tk.Label(gameui, text=pr1).grid(row=8, column=1)
                elif(rounds == 1):
                    pr1 = (name2.get(),"got ",score2," last round")
                    labelName1 = tk.Label(gameui, text=pr1).grid(row=10, column=1)

                rounds -=1
                player1 = True

    if(score1 > score2):
        pr1 = (name1.get(),"won with",score1,"points")
        labelName1 = tk.Label(gameui, text=pr1).grid(row=10, column=1)
    else:
        pr1 = (name2.get(),"won with",score2,"points")
        labelName1 = tk.Label(gameui, text=pr1).grid(row=10, column=1)      
    
def signin():
    if(school.get() == "light hall"):
        root.destroy()
        game()
    else:
        labelError = tk.Label(root, text="You are not authorised to play").grid(row=5, column=0)

root = tk.Tk()
root.geometry("400x200")
root.title("Dice")

name1 = tk.StringVar()
name2 = tk.StringVar()
school = tk.StringVar()

labelTitle = tk.Label(root, text="Sign in").grid(row=0, column=2)
labelName1 = tk.Label(root, text="Enter first name").grid(row=1, column=0, columnspan=2)
labelName2 = tk.Label(root, text="Enter second name").grid(row=2, column=0, columnspan=2)
labelSchool = tk.Label(root, text="Enter school name").grid(row=3, column=0, columnspan=2)
labelEnter = tk.Button(root, text ="Enter", command=signin, height = 1, width = 3).grid(row=4, column=0)

entryName1 = tk.Entry(root, textvariable=name1).grid(row=1, column=2)
entryName2 = tk.Entry(root, textvariable=name2).grid(row=2, column=2)
entrySchool = tk.Entry(root, textvariable=school).grid(row=3, column=2)
