
import sys
import pickle
from time import sleep
from tkinter import *
from tkinter import messagebox
import tkinter as tk
from PIL import ImageTk,Image
import re
import string,math,random
import socket
import json
import time
from random import choice


ClientSocket = socket.socket()

host = "192.168.56.101"

port = 8888

print('Waiting for connection')
try:
	ClientSocket.connect((host, port))
except socket.error as e:
	print(str(e))



#initializing variable
cards=["Aclub","Adiam","Ahear","Aspad","2club","2diam","2hear","2spad","3club","3diam",\
	"3hear","3spad","4club","4diam","4hear","4spad","5club","5diam","5hear","5spad","6club",\
	"6diam","6hear","6spad","7club","7diam","7hear","7spad","8club","8diam","8hear","8spad",\
	"9club","9diam","9hear","9spad","0club","0diam","0hear","0spad","Jclub","Jdiam",\
	"Jhear","Jspad","Qclub","Qdiam","Qhear","Qspad","Kclub","Kdiam","Khear","Kspad"]



HEIGHT = 800
WIDTH = 1000
root = tk.Tk()
root.title("Poker Game")
root.configure(bg='#477148')
photo = []
hitDisplay = 2
pcount = 4
player_cards = []
point = 0

#assign player cards
def assignPlayerCard():
	global player_card
	global pcount
	for i in range(len(player_cards),pcount):
		random_cards = choice(cards)
		player_cards.append(random_cards)
		cards.remove(random_cards)





#receive data from server
def receive_server_data():
	global playerID
	player_point = 0
	for i in range(hitDisplay):
		player_point = getPoint(player_cards[i],player_point)

	check = 1

	msg = {
	"player id": playerID,
	"player point": player_point,
	"check": check
	}

	data = pickle.dumps(msg)
	ClientSocket.sendall(data)

	server_data = ClientSocket.recv(1024).decode("utf")
	print(server_data)
	messagebox.showinfo("Congratulation!!!",server_data)


#Point function
def getPoint(cardStrength,player_point):
	global point
	if re.search("\AA",cardStrength):
		if player_point + 11<=21:
			point = 11
		else:
			point = 1
	elif re.search("\A2",cardStrength):
		point = 2
	elif re.search("\A3",cardStrength):
		point = 3
	elif re.search("\A4",cardStrength):
		point = 4
	elif re.search("\A5",cardStrength):
		point = 5
	elif re.search("\A6",cardStrength):
		point = 6
	elif re.search("\A7",cardStrength):
		point = 7
	elif re.search("\A8",cardStrength):
		point = 8
	elif re.search("\A9",cardStrength):
		point = 9
	elif re.search("\A10",cardStrength):
		point = 10
	elif re.search("\AJ",cardStrength):
		point = 10
	elif re.search("\AQ",cardStrength):
		point = 10
	elif re.search("\AK",cardStrength):
		point = 10
	else:
		print("Cannot calculate point")

	point = point + player_point
	return point


#display card rank
def displayCards2(player_cards):
	if re.search(r"diam\b",player_cards):
		image3 = "Diamonds.png"
	elif re.search(r"spad\b",player_cards):
		image3 = "Spades.png"
	elif re.search(r"club\b",player_cards):
		image3 = "Clubs.png"
	elif re.search(r"hear\b",player_cards):
		image3 = "Hearts.png"
	return image3


def playerHit():
	global hitDisplay
	hitDisplay = hitDisplay + 1
	table()
	if hitDisplay >= 5:
		receive_server_data()

def closeConnection():
	ClientSocket.close()


#display card number
def displayCards(player_cards):
	for i in range(len(player_cards)):
		if re.search("\A2",player_cards[i]):
			image = "Two"
			image2 = displayCards2(player_cards[i])
		elif re.search("\A3",player_cards[i]):
			image = "Three"
			image2 = displayCards2(player_cards[i])
		elif re.search("\A4",player_cards[i]):
			image = "Four"
			image2 = displayCards2(player_cards[i])
		elif re.search("\A5",player_cards[i]):
			image = "Five"
			image2 = displayCards2(player_cards[i])
		elif re.search("\A6",player_cards[i]):
			image = "Six"
			image2 = displayCards2(player_cards[i])
		elif re.search("\A7",player_cards[i]):
			image = "Seven"
			image2 = displayCards2(player_cards[i])
		elif re.search("\A8",player_cards[i]):
			image = "Eight"
			image2 = displayCards2(player_cards[i])
		elif re.search("\A9",player_cards[i]):
			image = "Nine"
			image2 = displayCards2(player_cards[i])
		elif re.search("\A0",player_cards[i]):
			image = "Ten"
			image2 = displayCards2(player_cards[i])
		elif re.search("\AJ",player_cards[i]):
			image = "Jack"
			image2 = displayCards2(player_cards[i])
		elif re.search("\AQ",player_cards[i]):
			image = "Queen"
			image2 = displayCards2(player_cards[i])
		elif re.search("\AK",player_cards[i]):
			image = "King"
			image2 = displayCards2(player_cards[i])
		elif re.search("\AA",player_cards[i]):
			image = "Ace"
			image2 = displayCards2(player_cards[i])
		photo.append(image + " of " + image2)
	return photo


def table():
	#global background_image
	global new_pick
	global player_cards
	global hitDisplay
	new_pick = []
	table = Toplevel()
	table.title("Poker Table")
	table.geometry("1000x800")
	table.configure(bg='#477148')


	assignPlayerCard()

	#background image
	#background_image = tk.PhotoImage(file='background.png')
	#background_label = tk.Label(table, image=background_image)
	#background_label.place(x=0,y=0,relwidth=1,relheight=1)

	#frame1
	frame1 = tk.Frame(table, bg='#477148')
	frame1.place(relx=0.1, rely=0.01, relwidth=0.8, relheight=0.3)

	#labeldealer
	#labelchoice = tk.Label(frame1, text="Player money : ", bg='green', fg='white')
	#labelchoice.place(relx=0.05, rely=0.10, relwidth=0.40, relheight=0.06)

	global labelamount

	#labeldealer
	#labelamount = tk.Label(frame1) #AMOUNT MONEY HERE
	#labelamount.place(relx=0.5, rely=0.10, relwidth=0.40, relheight=0.06)

	#labeldealer
	#labelhit = tk.Label(frame1, text="ENTER AMOUNT TO HIT", bg='green', fg='white')
	#labelhit.place(relx=0.05, rely=0.20, relwidth=0.40, relheight=0.06)

	#entry nametable
	#entrytable = tk.Entry(frame1, font=40)
	#entrytable.place(relx=0.5,rely=0.20,relwidth=0.25,relheight=0.1)

	#buttonhit
	button = tk.Button(frame1, text="HIT", font=40, command=playerHit)
	button.place(relx=0.25, rely=0.55, relwidth=0.1, relheight=0.1)

	#buttonstand
	button = tk.Button(frame1, text="Check", font=40, command=receive_server_data)
	button.place(relx=0.65, rely=0.55, relwidth=0.1, relheight=0.1)

	#frame2
	frame2 = tk.Frame(table, bg='white')
	frame2.place(relx=0.1, rely=0.22, relwidth=0.8, relheight=0.3)

	#labeldealer
	labelfirst = tk.Label(frame2, text="FIRST PLAYER", bg='#477148', fg='white')
	labelfirst.place(relx=0.3, rely=0.05, relwidth=0.40, relheight=0.06)

	print(player_cards)

	photo = displayCards(player_cards)
	for i in range(len(photo)):
		card_pick = Image.open("cards/" + photo[i])
		resized = card_pick.resize((50,90),Image.ANTIALIAS)
		if i == 0:
			if not (hitDisplay >= 1):
				card_pick = Image.open("cards/default.png")
				resized = card_pick.resize((50,90),Image.ANTIALIAS)
			new_pick.append(ImageTk.PhotoImage(resized))
			labelframe2 = tk.Label(frame2, image=new_pick[i], bg='#477148')
			labelframe2.place(relx=0.1,rely=0.2,relwidth=0.2,relheight=0.6)
		elif i == 1:
			if not (hitDisplay >= 2):
				card_pick = Image.open("cards/default.png")
				resized = card_pick.resize((50,90),Image.ANTIALIAS)
			new_pick.append(ImageTk.PhotoImage(resized))
			#label
			labelframe2 = tk.Label(frame2, image=new_pick[i], bg='#477148')
			labelframe2.place(relx=0.3,rely=0.2,relwidth=0.2,relheight=0.6)
		elif i == 2:
			if not (hitDisplay >= 3):
				card_pick = Image.open("cards/default.png")
				resized = card_pick.resize((50,90),Image.ANTIALIAS)
			new_pick.append(ImageTk.PhotoImage(resized))
			#label
			labelframe2 = tk.Label(frame2, image=new_pick[i], bg='#477148')
			labelframe2.place(relx=0.5,rely=0.2,relwidth=0.2,relheight=0.6)
		elif i == 3:
			if not (hitDisplay >= 4):
				card_pick = Image.open("cards/default.png")
				resized = card_pick.resize((50,90),Image.ANTIALIAS)
			new_pick.append(ImageTk.PhotoImage(resized))
			#label
			labelframe2 = tk.Label(frame2, image=new_pick[i], bg='#477148')
			labelframe2.place(relx=0.7,rely=0.2,relwidth=0.2,relheight=0.6)
		else:
			pass




#main start
playerID = 0

#canvas size
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

#background image
background_image = tk.PhotoImage(file='cards/background.png')
background_label = tk.Label(root, image=background_image)
background_label.place(x=0,y=0,relwidth=1,relheight=1)

#framemenu
framemenu = tk.Frame(root, bg='#477148', bd=5)
framemenu.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.5)

#label
labelwelcome = tk.Label(framemenu, text = "WELCOME TO POKER GAME", bg='green', fg='white')
labelwelcome.place(relx=0.3,rely=0.20,relwidth=0.40,relheight=0.06)

#label
labelenter1 = tk.Label(framemenu, text = "ENTER YOUR ID", bg='green', fg='white')
labelenter1.place(relx=0.3,rely=0.30,relwidth=0.40,relheight=0.06)

#label
#labelenter0 = tk.Label(framemenu, text = "ENTER |0| TO EXIT GAME", bg='green', fg='white')
#labelenter0.place(relx=0.3,rely=0.40,relwidth=0.40,relheight=0.06)

#entry name1
entrymenu = tk.Entry(framemenu, font=40)
entrymenu.place(relx=0.37,rely=0.40,relwidth=0.25,relheight=0.1)

def enterPlayerID(entry):
	global playerID
	playerID = entrymenu.get()
	ClientSocket.send(playerID.encode("utf-8"))
	messagebox.showinfo("ID accepted","Welcome Player " + playerID)

button = tk.Button(framemenu, text = "ID",command=lambda: enterPlayerID(entrymenu.get()) , font=40,)
button.place(relx=0.37,rely=0.60,relwidth=0.25,relheight=0.1)


#button start
button = tk.Button(framemenu, text = "Start",command=table, font=40,)
button.place(relx=0.37,rely=0.80,relwidth=0.25,relheight=0.1)






root.mainloop()
