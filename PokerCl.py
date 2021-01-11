
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
new_pick1 = []

#assign player cards
def assignPlayerCard():
	global player_card
	global pcount
	for i in range(len(player_cards),pcount):
		random_cards = choice(cards)
		player_cards.append(random_cards)
		cards.remove(random_cards)


#receive data from server
def receive_sent_server():
	checkbutton.config(state=tk.DISABLED)
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
	play_again()


#play again button function
def play_again():
	global photo
	global hitDisplay
	global player_cards
	global new_pick
	global new_pick1
	photo = []
	hitDisplay = 2
	player_cards = []
	new_pick = []
	new_pick1 = []
	print(photo)
	print(player_cards)
	print(new_pick)
	print(new_pick1)
	playagainbutton.config(state=tk.NORMAL)
	pass



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
	elif re.search("\A0",cardStrength):
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
	global photo
	global new_pick1

	hitDisplay = hitDisplay + 1
	if hitDisplay >= 5:
		receive_sent_server()

	else:
		card_pick = Image.open("cards/" + photo[hitDisplay-1])
		resized = card_pick.resize((50,90),Image.ANTIALIAS)
		if hitDisplay ==3:
			new_pick1.append(ImageTk.PhotoImage(resized))
			labelframe2 = tk.Label(frame2, image=new_pick1[0], bg='#477148')
			labelframe2.place(relx=0.5,rely=0.2,relwidth=0.2,relheight=0.6)
		elif hitDisplay ==4:
			new_pick1.append(ImageTk.PhotoImage(resized))
			labelframe2 = tk.Label(frame2, image=new_pick1[1], bg='#477148')
			labelframe2.place(relx=0.7,rely=0.2,relwidth=0.2,relheight=0.6)
			hitbutton.config(state=tk.DISABLED)


#display card number
def displayCards(player_cards):
	photo = []
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

#display card in GUI
def displayCardsGUI():
	global photo
	global new_pick
	print(len(cards))
	assignPlayerCard()
	print(len(cards))
	print(player_cards)
	photo = displayCards(player_cards)
	print(photo)
	print(hitDisplay)
	new_pick = []
	for i in range(len(photo)):
		if i < 2:
			card_pick = Image.open("cards/" + photo[i])
			resized = card_pick.resize((50,90),Image.ANTIALIAS)
			if i == 0:
				new_pick.append(ImageTk.PhotoImage(resized))
				labelframe2 = tk.Label(frame2, image=new_pick[i], bg='#477148')
				labelframe2.place(relx=0.1,rely=0.2,relwidth=0.2,relheight=0.6)
			elif i == 1:
				new_pick.append(ImageTk.PhotoImage(resized))
				labelframe2 = tk.Label(frame2, image=new_pick[i], bg='#477148')
				labelframe2.place(relx=0.3,rely=0.2,relwidth=0.2,relheight=0.6)
		elif i < 4:
			card_pick = Image.open("cards/default.png")
			resized = card_pick.resize((50,90),Image.ANTIALIAS)
			if i == 2:
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
		playagainbutton.config(state=tk.DISABLED)
		hitbutton.config(state=tk.NORMAL)
		checkbutton.config(state=tk.NORMAL)



def table():
	#global background_image
	global new_pick
	global player_cards
	global hitDisplay
	global table

	new_pick = []
	table = Toplevel()
	table.title("Poker Table")
	table.geometry("1000x800")
	table.configure(bg='#477148')

	#frame1
	frame1 = tk.Frame(table, bg='#477148')
	frame1.place(relx=0.1, rely=0.01, relwidth=0.8, relheight=0.3)

	global labelamount

	global hitbutton
	#buttonhit
	hitbutton = tk.Button(frame1, text="HIT", font=40, command=playerHit)
	hitbutton.place(relx=0.25, rely=0.55, relwidth=0.1, relheight=0.1)
	hitbutton.config(state=tk.DISABLED)

	global playagainbutton
	#play again button
	playagainbutton = tk.Button(frame1, text="Get Card", font=40, command=lambda: [displayCardsGUI(),labelframe2.destroy()])
	playagainbutton.place(relx=0.42, rely=0.4, relwidth=0.15, relheight=0.15)

	global checkbutton
	#buttoncheck
	checkbutton = tk.Button(frame1, text="Check", font=40, command=receive_sent_server)
	checkbutton.place(relx=0.65, rely=0.55, relwidth=0.1, relheight=0.1)
	checkbutton.config(state=tk.DISABLED)
	global frame2

	#frame2
	frame2 = tk.Frame(table, bg='white')
	frame2.place(relx=0.1, rely=0.22, relwidth=0.8, relheight=0.3)

	#labelPlayer
	labelfirst = tk.Label(frame2, text="FIRST PLAYER", bg='#477148', fg='white')
	labelfirst.place(relx=0.3, rely=0.05, relwidth=0.40, relheight=0.06)

	global labelframe2
	#labelCard
	card_pick = Image.open("cards/default.png")
	resized = card_pick.resize((50,90),Image.ANTIALIAS)
	pick = ImageTk.PhotoImage(resized)
	labelframe2 = tk.Label(frame2, image=pick, bg='#477148')
	labelframe2.place(relx=0.1,rely=0.2,relwidth=0.2,relheight=0.6)

	table.mainloop()


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
labelenter1 = tk.Label(framemenu, text = "ENTER YOUR ID", bg='green', fg='white')
labelenter1.place(relx=0.3,rely=0.30,relwidth=0.40,relheight=0.06)

#entry name1
entrymenu = tk.Entry(framemenu, font=40)
entrymenu.place(relx=0.37,rely=0.40,relwidth=0.25,relheight=0.1)

#sent name to server
def enterPlayerID(entry):
	global playerID
	playerID = entrymenu.get()
	if playerID == "1001" or playerID == "1002":
		ClientSocket.send(playerID.encode("utf-8"))
		entrymenu.destroy()
		button1.destroy()
		labelname = tk.Label(framemenu, text = "Welcome to blackjack " + playerID, bg='#477148', fg='blue', font='Verdana 30 bold')
		labelname.place(relx=0.1,rely=0.60,relwidth=0.80,relheight=0.1)
	else:
		messagebox.showinfo("ERROR 101","You Enter invalid ID!")


button1 = tk.Button(framemenu, text = "ID",command=lambda: enterPlayerID(entrymenu.get()) , font=40,)
button1.place(relx=0.37,rely=0.60,relwidth=0.25,relheight=0.1)
#button start
button2 = tk.Button(framemenu, text = "Start",command=table, font=40,)
button2.place(relx=0.37,rely=0.80,relwidth=0.25,relheight=0.1)


root.mainloop()
