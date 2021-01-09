#server.py
from random import choice
import sys
import socket
from _thread import *
import itertools
import re
import json
#create a socket object
s = socket.socket()

#get local machine name
host = socket.gethostname()
port = 8888
ThreadCount = 0
#bind to the port
s.bind((host,port))
print("Socket is bind")
s.listen(5)
print("Socket is listening")
#Waiting for connection from client
print("Waiting for connection from client")

#initializing variable
cards=["Aclub","Adiam","Ahear","Aspad","2club","2diam","2hear","2spad","3club","3diam",\
	"3hear","3spad","4club","4diam","4hear","4spad","5club","5diam","5hear","5spad","6club",\
	"6diam","6hear","6spad","7club","7diam","7hear","7spad","8club","8diam","8hear","8spad",\
	"9club","9diam","9hear","9spad","0club","0diam","0hear","0spad","Jclub","Jdiam",\
	"Jhear","Jspad","Qclub","Qdiam","Qhear","Qspad","Kclub","Kdiam","Khear","Kspad"]
dealer_cards = []
dealer_point = 0
player1_cards = []
player1_point = 0
player1_money = 1000
player2_cards = []
player2_point = 0
player2_money = 1000
dcount = 2
pcount = 2
bet = 100
check = 0
hit = 1
#assign player cards
def assignPlayer1Card(start,end):
	for i in range(start,end):
		random_cards = choice(cards)
		player1_cards.append(random_cards)
		cards.remove(random_cards)

def assignPlayer2Card(start,end):
	for i in range(start,end):
		random_cards = choice(cards)
		player2_cards.append(random_cards)
		cards.remove(random_cards)


#assign table cards
def assignDealerCard():
	for i in range(len(dealer_cards),dcount):
		random_cards = choice(cards)
		dealer_cards.append(random_cards)
		cards.remove(random_cards)

#Point function
def getPoint(cardStrength,player_point):
	if re.search("^A",cardStrength):
		if player_point + 11<=21:
			point = 11
		else:
			point = 1
	elif re.search("^2",cardStrength):
		point = 2
	elif re.search("^3",cardStrength):
		point = 3
	elif re.search("^4",cardStrength):
                point = 4
	elif re.search("^5",cardStrength):
                point = 5
	elif re.search("^6",cardStrength):
                point = 6
	elif re.search("^7",cardStrength):
                point = 7
	elif re.search("^8",cardStrength):
                point = 8
	elif re.search("^9",cardStrength):
                point = 9
	elif re.search("^10",cardStrength):
                point = 10
	elif re.search("^J",cardStrength):
                point = 10
	elif re.search("^Q",cardStrength):
                point = 10
	elif re.search("^K",cardStrength):
                point = 10
	else:
		print("Cannot calculate point")

	point = point + player_point
	return point

#Theread client
def threaded_client(connection):
	print("Conenction establish \n")
	while True:
		#Assign player card and dumps json into element
		card_player1 = json.dumps(assignPLayer1Card(len(player1_cards,pcount)))
		card_player2 = json.dumps(assignPlayer2Card(len(player2_cards,pcount)))
		card_dealer = json.dumps(assignDealerCard())

		#Send and convert to json
		connection.sendall(card_player1.encode('utf-8'))
		connection.sendall(card_player2.encode('utf-8'))
		connection.sendall(card_dealer.encode('utf-8'))

		#debug
		print(card_player1)
		print(card_player2)
		print(card_dealer)


		#Calculate player and dealer point
		for i in range(len(player1_cards)):
			player1_point = getPoint(player1_cards[i],player1_point)
		for i in range(len(player2_cards)):
                        player2_point = getPoint(player2_cards[i],player2_point)
		for i in range(len(dealer_cards)):
                        dealer_point = getPoint(dealer_cards[i],dealer_point)

		#print player and dealer point and send to client
		print("Player 1 point:"+str(player1_point))
		print("Player 2 point:"+str(player2_point))
		print("Dealer  point:"+str(dealer_point))
		connection.send(str(p1).encode())
                connection.send(str(p2).encode())
                connection.send(str(D).encode())
	connection.close()

#Main
while True:
	client,addr = s.accept()
	print("Connected to : "+addr[0]+":"+str(addr[1]))
	start_new_thread(threaded_client,(client,))
	ThreadCount += 1
	playerID[ThreadedCount]
	playerID[ThreadedCount-1]=ThreadedCount
	print('Thread number:'+str(ThreadCount))
	s.send(str(playerID).encode())
except socket.error:
	print('An error has occurred')
s.close()
