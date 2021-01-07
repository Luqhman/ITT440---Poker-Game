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
player1_cards = []
player1_money = 1000
player2_cards = []
player2_money = 1000
dcount = 2
pcount = 2
bet = 100
check = 0
hit = 0


#assign player cards
def assignPlayerCard():
	for i in range(pcount):
		random_cards = choice(cards)
		player1_cards.append(random_cards)
		cards.remove(random_cards)
	for i in range(pcount):
		random_cards = choice(cards)
		player2_cards.append(random_cards)
		cards.remove(random_cards)

#assign dealer cards
def assignTableCard():
	for i in range(len(dealer_cards),dcount)
		random_cards = choice(cards)
		dealer_cards.append(random_cards)
		cards.remove(random_cards)


#Theread client
def threaded_client(connection)
	print("Conenction establish \n"
	#process



	connection.close()

#Main
while True:
	client,addr = s.accept()
	print("Connected to : "+addr[0]+":"+str(addr[1]))
	start_new_thread(threaded_client,(client,))
	ThreadCount += 1
	print('Thread number:'+str(ThreadCount))
s.close()
