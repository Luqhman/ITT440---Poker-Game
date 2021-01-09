from tkinter import *
import tkinter as tk
from PIL import ImageTk,Image
import re
from functools import partial
import string,math,random
import socket
import sys
import json
import time
from time import sleep


player2_money = 1000
dealer_cards = []
player1_cards = []
player2_cards = []
bet = 100
check = 0
hit = 0
playerID = 1
playerID1 = 1
playerID2 = 2


HEIGHT = 1000
WIDTH = 800
root = tk.Tk()
root.title("Poker Game")
root.configure(bg='#477148')
global photo

player1_money = 1000
player1_cards = ['Aspad','2diam', 'Jhear', '3club']
player2_cards = ['2hear', '3diam','4club','0spad']
dealer_cards = ['Aclub','5diam','Qspad','Khear']
photo = []

#Player raise bet
def betRaise(player_bet):
	global player1_money
	global bet
	print(player_bet)
	player1_money = player1_money - (int(player_bet))
	bet = bet + (int(player_bet))
	print("Player remaining money : " + str(player1_money))
	hit = 1
	print(hit)
	print(bet)
	labelamount['text'] = player1_money

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

def playerCheck():
	check = 1
	print(check)

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
	global new_pick2
	new_pick = []
	new_pick2 = []

	table = Toplevel()
	table.title("Poker Table")
	table.geometry("800x1000")
	table.configure(bg='#477148')

	#background image
	#background_image = tk.PhotoImage(file='background.png')
	#background_label = tk.Label(table, image=background_image)
	#background_label.place(x=0,y=0,relwidth=1,relheight=1)

	#frame1
	frame1 = tk.Frame(table, bg='blue')
	frame1.place(relx=0.1, rely=0.01, relwidth=0.8, relheight=0.3)

	#labeldealer
	labelchoice = tk.Label(frame1, text="CURRENT AMOUNT : ", bg='green', fg='white')
	labelchoice.place(relx=0.05, rely=0.10, relwidth=0.40, relheight=0.06)
	global labelamount
	#labeldealer
	labelamount = tk.Label(frame1) #AMOUNT MONEY HERE
	labelamount.place(relx=0.5, rely=0.10, relwidth=0.40, relheight=0.06)

	#labeldealer
	labelhit = tk.Label(frame1, text="ENTER AMOUNT TO HIT", bg='green', fg='white')
	labelhit.place(relx=0.05, rely=0.20, relwidth=0.40, relheight=0.06)

	#entry nametable
	entrytable = tk.Entry(frame1, font=40)
	entrytable.place(relx=0.5,rely=0.20,relwidth=0.25,relheight=0.1)

	#buttonhit
	button = tk.Button(frame1, text="HIT", font=40, command=lambda: betRaise(entrytable.get()))
	button.place(relx=0.45, rely=0.40, relwidth=0.1, relheight=0.1)

	#buttonstand
	button = tk.Button(frame1, text="Check", font=40, command=playerCheck)
	button.place(relx=0.45, rely=0.55, relwidth=0.1, relheight=0.1)

	#frame2
	frame2 = tk.Frame(table, bg='yellow')
	frame2.place(relx=0.1, rely=0.22, relwidth=0.8, relheight=0.3)

	#labeldealer
	labelfirst = tk.Label(frame2, text="FIRST PLAYER", bg='green', fg='white')
	labelfirst.place(relx=0.3, rely=0.05, relwidth=0.40, relheight=0.06)

	photo = displayCards(player1_cards)
	for i in range(len(photo)):
		card_pick = Image.open("cards/" + photo[i])
		resized = card_pick.resize((50,90),Image.ANTIALIAS)
		if i == 0:
			new_pick.append(ImageTk.PhotoImage(resized))
			labelframe2 = tk.Label(frame2, image=new_pick[i], bg='blue')
			labelframe2.place(relx=0.1,rely=0.2,relwidth=0.2,relheight=0.6)
		elif i == 1:
			new_pick.append(ImageTk.PhotoImage(resized))
			#label
			labelframe2 = tk.Label(frame2, image=new_pick[i], bg='white')
			labelframe2.place(relx=0.3,rely=0.2,relwidth=0.2,relheight=0.6)
		elif i == 2:
			new_pick.append(ImageTk.PhotoImage(resized))
			#label
			labelframe2 = tk.Label(frame2, image=new_pick[i], bg='red')
			labelframe2.place(relx=0.5,rely=0.2,relwidth=0.2,relheight=0.6)
		elif i == 3:
			new_pick.append(ImageTk.PhotoImage(resized))
			#label
			labelframe2 = tk.Label(frame2, image=new_pick[i], bg='white')
			labelframe2.place(relx=0.7,rely=0.2,relwidth=0.2,relheight=0.6)


	#frame3
	frame3 = tk.Frame(table, bg='green')
	frame3.place(relx=0.1, rely=0.48, relwidth=0.8, relheight=0.3)
	#labeldealer
	labelsecond = tk.Label(frame3, text="SECOND PLAYER", bg='green', fg='white')
	labelsecond.place(relx=0.3, rely=0.05, relwidth=0.40, relheight=0.06)

	photo = displayCards(player2_cards)
	for i in range(len(player1_cards),len(photo)):
		card_pick = Image.open("cards/" + photo[i])
		resized = card_pick.resize((50,90),Image.ANTIALIAS)
		if i == 4:
			new_pick.append(ImageTk.PhotoImage(resized))
			#label
			labelframe3 = tk.Label(frame3, image=new_pick[i], bg='white')
			labelframe3.place(relx=0.1,rely=0.2,relwidth=0.2,relheight=0.6)
		elif i == 5:
			new_pick.append(ImageTk.PhotoImage(resized))
			#label
			labelframe3 = tk.Label(frame3, image=new_pick[i], bg='blue')
			labelframe3.place(relx=0.3,rely=0.2,relwidth=0.2,relheight=0.6)
		elif i == 6:
			new_pick.append(ImageTk.PhotoImage(resized))
			#label
			labelframe3 = tk.Label(frame3, image=new_pick[i], bg='white')
			labelframe3.place(relx=0.5,rely=0.2,relwidth=0.2,relheight=0.6)
		elif i == 7:
			new_pick.append(ImageTk.PhotoImage(resized))
			#label
			labelframe3 = tk.Label(frame3, image=new_pick[i], bg='red')
			labelframe3.place(relx=0.7,rely=0.2,relwidth=0.2,relheight=0.6)

	#frame4
	frame4 = tk.Frame(table, bg='black')
	frame4.place(relx=0.1, rely=0.74, relwidth=0.8, relheight=0.3)
	#labeldealer
	labelsecond = tk.Label(frame4, text="DEALER", bg='green', fg='white')
	labelsecond.place(relx=0.3, rely=0.05, relwidth=0.40, relheight=0.06)

	photo = displayCards(dealer_cards)
	for i in range(len(player1_cards)+len(player2_cards),len(photo)):
		card_pick = Image.open("cards/" + photo[i])
		resized = card_pick.resize((50,90),Image.ANTIALIAS)
		if i == 8:
			new_pick.append(ImageTk.PhotoImage(resized))
			#label
			labelframe4 = tk.Label(frame4, image=new_pick[i], bg='blue')
			labelframe4.place(relx=0.1,rely=0.2,relwidth=0.2,relheight=0.6)
		elif i == 9:
			new_pick.append(ImageTk.PhotoImage(resized))
			#label
			labelframe4 = tk.Label(frame4, image=new_pick[i], bg='white')
			labelframe4.place(relx=0.3,rely=0.2,relwidth=0.2,relheight=0.6)
		elif i == 10:
			new_pick.append(ImageTk.PhotoImage(resized))
			#label
			labelframe4 = tk.Label(frame4, image=new_pick[i], bg='red')
			labelframe4.place(relx=0.5,rely=0.2,relwidth=0.2,relheight=0.6)
		elif i == 11:
			new_pick.append(ImageTk.PhotoImage(resized))
			#label
			labelframe4 = tk.Label(frame4, image=new_pick[i], bg='white')
			labelframe4.place(relx=0.7,rely=0.2,relwidth=0.2,relheight=0.6)


#canvas size
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

#background image
#background_image = tk.PhotoImage(file='background.png')
#background_label = tk.Label(root, image=background_image)
#background_label.place(x=0,y=0,relwidth=1,relheight=1)

#framemenu
framemenu = tk.Frame(root, bg='#477148', bd=5)
framemenu.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.5)

#label
labelwelcome = tk.Label(framemenu, text = "WELCOME TO POKER GAME", bg='green', fg='white')
labelwelcome.place(relx=0.3,rely=0.20,relwidth=0.40,relheight=0.06)

#label
labelenter1 = tk.Label(framemenu, text = "ENTER YOUR NAME", bg='green', fg='white')
labelenter1.place(relx=0.3,rely=0.30,relwidth=0.40,relheight=0.06)

#label
#labelenter0 = tk.Label(framemenu, text = "ENTER |0| TO EXIT GAME", bg='green', fg='white')
#labelenter0.place(relx=0.3,rely=0.40,relwidth=0.40,relheight=0.06)

#entry name1
entrymenu = tk.Entry(framemenu, font=40)
entrymenu.place(relx=0.37,rely=0.60,relwidth=0.25,relheight=0.1)

#button start
button = tk.Button(framemenu, text = "START",command=table, font=40,)
button.place(relx=0.37,rely=0.80,relwidth=0.25,relheight=0.1)

root.mainloop()
