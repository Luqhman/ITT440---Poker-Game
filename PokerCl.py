
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



HEIGHT = 720
WIDTH = 1280
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

	server_data = ClientSocket.recv(1024)
	server_data2 = pickle.loads(server_data)
	messagebox.showinfo("GAME END", server_data2["text"])


	labelPoint1 = tk.Label(table,text="PLAYER 1 POINT :" + str(server_data2["point1"]), bg="#477148", font="arial 10")
	labelPoint1.place(relx=0.6,rely=0.06,relwidth=0.13,relheight=0.06)

	labelPoint2 = tk.Label(table,text="PLAYER 2 POINT :" + str(server_data2["point2"]), bg="#477148", font="arial 10")
	labelPoint2.place(relx=0.8,rely=0.06,relwidth=0.13,relheight=0.06)
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
	table.destroy()
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
		resized = card_pick.resize((150,250),Image.ANTIALIAS)
		if hitDisplay ==3:
			new_pick1.append(ImageTk.PhotoImage(resized))
			labelframe2 = tk.Label(table, image=new_pick1[0], bg='#477148')
			labelframe2.place(relx=0.5,rely=0.3,relwidth=0.118,relheight=0.347)
		elif hitDisplay ==4:
			new_pick1.append(ImageTk.PhotoImage(resized))
			labelframe2 = tk.Label(table, image=new_pick1[1], bg='#477148')
			labelframe2.place(relx=0.55,rely=0.3,relwidth=0.118,relheight=0.347)
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
	assignPlayerCard()
	print(player_cards)
	photo = displayCards(player_cards)
	print(photo)
	print(hitDisplay)
	new_pick = []
	for i in range(len(photo)):
		if i < 2:
			card_pick = Image.open("cards/" + photo[i])
			resized = card_pick.resize((150,250),Image.ANTIALIAS)
			if i == 0:
				new_pick.append(ImageTk.PhotoImage(resized))
				labelframe2 = tk.Label(table, image=new_pick[i], bg='#477148')
				labelframe2.place(relx=0.4,rely=0.3,relwidth=0.118,relheight=0.347)
			elif i == 1:
				new_pick.append(ImageTk.PhotoImage(resized))
				labelframe2 = tk.Label(table, image=new_pick[i], bg='#477148')
				labelframe2.place(relx=0.45,rely=0.3,relwidth=0.118,relheight=0.347)
		elif i < 4:
			card_pick = Image.open("cards/default.png")
			resized = card_pick.resize((150,250),Image.ANTIALIAS)
			if i == 2:
				new_pick.append(ImageTk.PhotoImage(resized))
				#label
				labelframe2 = tk.Label(table, image=new_pick[i], bg='#477148')
				labelframe2.place(relx=0.8,rely=0.3,relwidth=0.118,relheight=0.347)
			elif i == 3:
				if not (hitDisplay >= 4):
					card_pick = Image.open("cards/default.png")
					resized = card_pick.resize((150,250),Image.ANTIALIAS)
				new_pick.append(ImageTk.PhotoImage(resized))
				#label
				labelframe2 = tk.Label(table, image=new_pick[i], bg='#477148')
				labelframe2.place(relx=0.8,rely=0.3,relwidth=0.118,relheight=0.347)
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

	print(len(cards))
	new_pick = []
	table = Toplevel()
	table.title("Poker Table")
	table.geometry("1280x720")

	#table.configure(bg='#477148')

	#backgroun image for table
	background_image = tk.PhotoImage(file='cards/background.png')
	background_label = tk.Label(table, image=background_image)
	background_label.place(x=0,y=0,relwidth=1,relheight=1)

	#frame1
	#frame1 = tk.Frame(table, bg='white')
	#frame1.place(relx=0.1, rely=0.06, relwidth=0.8, relheight=0.2)

	global labelamount

	global hitbutton
	#buttonhit
	hitbutton = tk.Button(table, text="HIT", font="verdana 15 bold",fg="#094E75", command=playerHit)
	hitbutton.place(relx=0.1, rely=0.1, relwidth=0.1, relheight=0.1)
	hitbutton.config(state=tk.DISABLED)

	global playagainbutton
	#play again button
	playagainbutton = tk.Button(table, text="GET CARD", font="verdana 15 bold", fg="#094E75",command=displayCardsGUI)
	playagainbutton.place(relx=0.075, rely=0.7, relwidth=0.15, relheight=0.15)

	global checkbutton
	#buttoncheck
	checkbutton = tk.Button(table, text="Check", font="verdana 15 bold", fg="#094E75",command=receive_sent_server)
	checkbutton.place(relx=0.1, rely=0.23, relwidth=0.1, relheight=0.1)
	checkbutton.config(state=tk.DISABLED)
	global frame2

	#frame2
	#frame2 = tk.Frame(table, bg='#477148')
	#frame2.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.7)

	global labelPoint1
	labelPoint1 = tk.Label(table,text="PLAYER 1 POINT :", bg="#477148", font="arial 10")
	labelPoint1.place(relx=0.6,rely=0.06,relwidth=0.13,relheight=0.06)
	global labelPoint2
	labelPoint2 = tk.Label(table,text="PLAYER 2 POINT :", bg="#477148", font="arial 10")
	labelPoint2.place(relx=0.8,rely=0.06,relwidth=0.13,relheight=0.06)

	global labelframe2
	#labelCard
	card_pick = Image.open("cards/default.png")
	resized = card_pick.resize((150,250),Image.ANTIALIAS)
	pick = ImageTk.PhotoImage(resized)
	labelframe2 = tk.Label(table, image=pick, bg='#477148')
	labelframe2.place(relx=0.8,rely=0.3,relwidth=0.118,relheight=0.347)

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

login_image_open = Image.open("cards/loginBack.png")
login_resized = login_image_open.resize((500,550),Image.ANTIALIAS)
login_image = ImageTk.PhotoImage(login_resized)
login_frame = tk.Label(root, image=login_image, bg='#477148')
login_frame.place(relx=0.3,rely=0.1,relwidth=0.337,relheight=0.75)


labeluserID = tk.Label(root, text = "BLACKJACK COMMUNITY",font=("Rockwell Condensed",15),bg="white")
labeluserID.place(relx=0.315,rely=0.33,relwidth=0.3,relheight=0.02)

labeluserID = tk.Label(root, text = "User ID",font=("Rockwell Condensed",15),bg="white")
labeluserID.place(relx=0.345,rely=0.45,relwidth=0.05,relheight=0.02)


#entry user ID
entryID = tk.Entry(root, font=("Rockwell Condensed",15),borderwidth=2)
entryID.place(relx=0.35,rely=0.5,relwidth=0.25,relheight=0.051)


#sent name to server
def enterPlayerID(entry):
	global playerID

	playerID = entryID.get()
	if playerID == "1001" or playerID == "1002":
		ClientSocket.send(playerID.encode("utf-8"))
		login_frame.destroy()
		labeluserID.destroy()
		entryID.destroy()
		button1.destroy()


		labelname = tk.Label(root, text = "WELCOME TO BLACKJACK PLAYER " + playerID,compound=tk.CENTER,image=background_image,bg='#477148', fg='white', font=("Rockwell Condensed",50))
		labelname.place(relx=0.15,rely=0.3,relwidth=0.8,relheight=0.1)
		labelname = tk.Label(root, text = "ARE YOU READY!!!! ", compound=tk.CENTER,bg='#477148', image=background_image,fg='white', font=("Rockwell Condensed",50))
		labelname.place(relx=0.34,rely=0.4,relwidth=0.345,relheight=0.1)

		global x
		x = 1
		global button2
		button2 = tk.Button(root,command=table,text="CLICK HERE TO START", compound=tk.CENTER, bg="#0C7A11",fg="white",font=("Rockwell Condensed",30))
		button2.place(relx=0.37,rely=0.6,relwidth=0.25,relheight=0.1)

		#button blinking function
		def label_relod():
			global x
			if x ==3:
				x=1
			if x == 1:
				button2.config(text="")
			elif x == 2:
				button2.config(text="CLICK HERE TO START")
			x += 1
			button2.after(500,label_relod)
		label_relod()




	else:
		messagebox.showinfo("ERROR 101","You Enter invalid ID!")


button1 = tk.Button(root,text = "LOGIN",compound=tk.CENTER,image=background_image,command=lambda: enterPlayerID(entryID.get()) , font=("Rockwell Condensed",15),fg="white")
button1.place(relx=0.35,rely=0.6,relwidth=0.25,relheight=0.08)


root.mainloop()
