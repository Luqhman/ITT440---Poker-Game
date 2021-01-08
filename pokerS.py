#server.py
from random import choice
import sys
import socket
from multiprocessing import Process
from _thread import *
#create a socket object
s= socket.socket()

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
cards=["Aclubs","Adiamonds","Ahearts","Aspades","2clubs","2diamonds","2hearts","2spades","3clubs","3diamonds",\
	"3hearts","3spades","4clubs","4diamonds","4hearts","4spades","5clubs","5diamonds","5hearts","5spades","6clubs",\
	"6diamonds","6hearts","6spades","7clubs","7diamonds","7hearts","7spades","8clubs","8diamonds","8hearts","8spdaes",\
	"9clubs","9diamonds","9hearts","9spades","10clubs","10diamonds","10hearts","10spades","Jclubs","Jdiamonds",\
	"Jhearts","Jspades","Qclubs","Qdiamonds","Qhearts","Qspades","Kclubs","Kdiamonds","Khearts","Kspades"]
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
def threaded_client(connection)
	print("Conenction establish \n")
	while True:
		loop = 0
		while loop == 0
			#Assign player card
			assignPlayer1Card(len(player1_cards,pcount))
			assignPlayer2Card(len(player2_cards,pcount))
			assignDealerCard()
			print(player1_cards)
			print(player2_cards)
			print(dealer_cards)
			print(len(cards))
		#accept data from client
		sel = connection.recv(1024).decode('utf-8')
		#chech whetheir input form player 1 or player 2
		#if P1==P1
			if hit == 1:
				pcount+=1
				print("Player 1 add a card")
				assignPlayer1Card(len(player1_cards),pcount)
				loop = 1
			print(player1_cards)
		#elif P2==P2
			if hit == 2:
				pcount+=1
				print("Player 2 add a card"
				assignPlayer2Card(len(player2_cards,pcount)
				loop = 2
			print(player2_cards)
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
		p1 = player1_point
		connection.send(str(p1).encode())
		p2 = player2_point
                connection.send(str(p2).encode())
		D = dealer_point
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
