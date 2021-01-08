import string, math, random
import socket
import sys
import time
from time import sleep

s = socket.socket()

host = ""

port = 8888

print(f"Connecting to {host}:{port}")

s.connect((host, port))
print("connected")
time.sleep(1)

player1_money = 1000
player2_money = 1000
dealer_cards = []
player1_cards = []
player2_cards = []
bet = 100
pc = 1
check = 0
hit = 0
playerID = 1
playerID1 = 1


#Front page function
def fmenu():
	print("-------------------------------Welcome To Poker Game--------------------------------")
	print("|1| Start Game")
	print("|0| Exit")
	while True:
		pick = input("Enter your choice:")
		if pick == '1':
			poker()
		elif pick == '0':
			break
		else:
			print("invalid choice")
			fmenu()
	sys.exit()

def random():
	print("This is the options")
	print("[1] Call")
	print("[2] Check")
	print("[2] Fold")
	print("[0] Back to menu")
	while True:
		sel = input("Enter your choice")
		if sel == '1':
			s.send(sel.encode())
			msg = s.recv(36)
			input("Amount :")
			print("Current amount : " % msg.decode('utf-8'))
		elif sel == '2':
			s.send(sel.encode())
                        msg = s.recv(36)
                        print("Current amount : %s" % msg.decode('utf-8'))
		elif sel == '3':
			fmenu()
		elif sel == '0':
			sys.exit()
		else:
			print("No input from server")




fmenu()


#Player raise function
def betRaise(bet,player_money):
	player_bet = input("Enter amount to raise : (must be more than {bet}) ")
	player_money -= int(player_bet)
	bet = bet + int(player_bet)
	print("Player bet : " + player_bet)
	return bet, player_money

#asking a player to raise or hold
if playerID == playerID1:
	bet, player1_money = betRaise(bet,player1_money)
else:
	print("Not your turn!")



playerInput = input("Enter 1 to hit and 0 to check : ")
print(playerInput)

#if raise pc = 0, if hold pc = 1
if int(playerInput) == 1:
	hit = 1
	#send data to server
elif int(playerInput) == 0:
	check += 1
	#send data to server


#display for debugging purpose
print("Player money : " + str(player1_money))
print("Bet now : " + str(bet))
