from tkinter import *import tkinter as tkfrom functools import partialimport timeimport decimalfrom tkinter import filedialogdef plus_result(label_result, n1, n2):    if "entryNum1" or "entryNum2" == "":         label_result.config(text="Write figures into both boxes")    number1 = (n1.get())    number2 = (n2.get())    result = float(number1)+float(number2)    answer = decimal.Decimal(result)    label_result.config(text="The answer is:  %s" % str(round(answer,2)))    history = open('Cal History.txt', 'a')    history.write("\n" +str(time))    history.write("\n" +str(number1) +("+") +str(number2))    history.write("\nThe answer was: %s" % str(round(answer,2)))    history.write("\n")    history.close()def times_result(label_result, n1, n2):    if "entryNum1" or "entryNum2" == "":        label_result.config(text="Write figures into both boxes")    number1 = (n1.get())    number2 = (n2.get())    result = float(number1)*float(number2)    answer = decimal.Decimal(result)    label_result.config(text="The answer is: %s" % str(round(answer,2)))    history = open('Cal History.txt', 'a')    history.write("\n" +str(time))    history.write("\n" +str(number1) +("x") +str(number2))    history.write("\nThe answer was: %s" % str(round(answer,2)))    history.write("\n")    history.close()def divide_result(label_result, n1, n2):    if "entryNum1" or "entryNum2" == "":        label_result.config(text="Write figures into both boxes")    number1 = (n1.get())    number2 = (n2.get())    result = float(number1)/float(number2)    answer = decimal.Decimal(result)    label_result.config(text="The answer is: %s" % str(round(answer,2)))        history = open('Cal History.txt', 'a')    history.write("\n" +str(time))    history.write("\n" +str(number1) +("/") +str (number2))    history.write("\nThe answer was: %s" % str(round(answer,2)))    history.write("\n")    history.close()def minus_result(label_result, n1, n2):    if "entryNum1" or "entryNum2" == "":        label_result.config(text="Write figures into both boxes")    number1 = (n1.get())    number2 = (n2.get())    result = float(number1)-float(number2)    answer = decimal.Decimal(result)    label_result.config(text="The answer is: %s" % str(round(answer,)))    history = open('Cal History.txt', 'a')    history.write("\n" +str(time))    history.write("\n" +str(number1) +("-") +str(number2))    history.write("\nThe answer was: %s" % str(round(answer,2)))    history.write("\n")    history.close()root = tk.Tk()root.geometry('400x200')root.title('Calculator')number1 = tk.StringVar()number2 = tk.StringVar()result = tk.StringVar()time = time.asctime( time.localtime(time.time()))labelTitle = tk.Label(root, text="Calculator").grid(row=0, column=2)labelNum1 = tk.Label(root, text="Enter first number").grid(row=1, column=0, columnspan=2)labelNum2 = tk.Label(root, text="Enter second number").grid(row=2, column=0, columnspan=2)labelResult = tk.Label(root)labelResult.grid(row=3, column=2)entryNum1 = tk.Entry(root, textvariable=number1).grid(row=1, column=2)entryNum2 = tk.Entry(root, textvariable=number2).grid(row=2, column=2)plus_result = partial(plus_result, labelResult, number1, number2)times_result = partial(times_result, labelResult, number1, number2)divide_result = partial(divide_result, labelResult, number1, number2)minus_result = partial(minus_result, labelResult, number1, number2)buttonPlus = tk.Button(root, text="+", command=plus_result, height = 1, width = 4).grid(row=5, column=0)buttonMinus = tk.Button(root, text ="-", command=minus_result, height = 1, width = 4).grid(row=5, column=1)buttonTimes = tk.Button(root, text ="*", command=times_result, height = 1, width = 4).grid(row=4, column=0)buttonDivide = tk.Button(root, text ="/", command=divide_result, height = 1, width = 4).grid(row=4, column=1)root.mainloop()