#pre INIT
Author = "WindleSR"
Version = "Beta 1.0"
Name = "WindleOS©"
print(Name + " -" + "\nVersion: " + Version + "\nAuthor: " + Author)

#imports
from time import *
import random
import os

#var
error = 0
running = True

#Code
username = open("username.txt", "r")
usr_read = username.read()
username.close()

password = open("password.txt", "r")
psw_read = password.read()
password.close()

usr_user = input("Username: ")
if usr_user == usr_read:
	pass
else:
	error = 1

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
	pass

while running:
	print("Type user to change username and password.")
	cmd = input("//")

	if cmd == "user":
		print("Fill in the following.")
		new_usr = input("New Username: ")
		newusr = open("username.txt", "w")
		newusr.write(new_usr)
		newusr.close()

		new_psw = input("New Password: ")
		newpsw = open("password.txt", "w")
		newpsw.write(new_psw)
		newpsw.close()

	if cmd == "quit":
		sleep(1)
		running = False