import string, math, random
import socket
import sys
import json
import time
from time import sleep

ClientSocket = socket.socket()

host = ""

port = 8888

print('Waiting for connection')
try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))

player1_money = 1000
player2_money = 1000
dealer_cards = []
player1_cards = []
player2_cards = []
bet = 100
pc = 1
check = 0
hit = 0
pcount = 0
ppoint = 0
player_name = ""

#Front page function
def fmenu():
	print("-------------------------------Welcome To Poker Game--------------------------------")
	player_name = input("Enter Your Name :")
	playerID = input("Enter Player 1 or 2 :")
	print("|1| Start Game")
	if playerID = 1:
		while True:
			pick = input("Enter your choice:")
			if pick == '1':
				player_bet = input("Input amount to bet :")
				player1_money = player1_money-int(player_bet)
				card = ClientSocket.recv(1024).decode('utf-8')
				a=card[2:7]
				b=card[11:16]
				c=card[20:25]
				d=card[29:34]
				print(a)
				print(b)
				print(c)
				print(d)
			else:
				print("invalid choice")
				fmenu()
		sys.exit()
	elif playerID = 2:
		while True:
                        pick = input("Enter your choice:")
                        if pick == '1':
                                player_bet = input("Input amount to bet :")
                                player1_money = player1_money-int(player_bet)
                                card = ClientSocket.recv(1024).decode('utf-8')
                                a=card[2:7]
                                b=card[11:16]
                                c=card[20:25]
                                d=card[29:34]
                                print(a)
                                print(b)
                                print(c)
                                print(d)
                        else:
                                print("invalid choice")
                                fmenu()
		sys.exit()


def random():
	print("This is the options")
	print("[1] Hit")
	print("[2] Check")
	print("[0] Back to menu")
	while True:
		sel = input("Enter your choice")
		if sel == '1':
			print("Current amount : " + str(player1_money))
			print("Player Card :" + (player1_cards.append()+1))
			pcount += 1
			s.send(sel.encode())
		elif sel == '2':
                        msg = s.recv(36)
                        print("Current amount : " str(player1_money))
			print("Player Card :" + player1_cards.append())
			pcount += 1
			s.send(sel.encode())
		elif sel == '0':
			sys.exit()
		else:
			print("No input from server")



#Player if won the round
def playerWon():
	msg = s.recv(36)
	print("Player Point :" + msg.decode('utf-8'))
	while True :
		if (ppoint1>ppoint2):
			print("You Won")
			player1_money += player2_money
		else:
			print("You Lose")
			player1_money -= player1_money

fmenu()
