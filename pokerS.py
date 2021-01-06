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

#creating cards
cards=["1clubs","1diamonds","1hearts","1spades","2clubs","2diamonds","2hearts","2spades","3clubs","3diamonds",\
	"3hearts","3spades","4clubs","4diamonds","4hearts","4spades","5clubs","5diamonds","5hearts","5spades","6clubs",\
	"6diamonds","6hearts","6spades","7clubs","7diamonds","7hearts","7spades","8clubs","8diamonds","8hearts","8spdaes",\
	"9clubs","9diamonds","9hearts","9spades","10clubs","10diamonds","10hearts","10spades","11clubs","11diamonds",\
	"11hearts","11spades","12clubs","12diamonds","12hearts","12spades","13clubs","13diamonds","13hearts","13spades"]
table_cards = []
player1_cards = []
player2_cards = []
tcount = 3
pcount = 2
bet = 100


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

#assign table cards
def assignTableCard():
	for i in range(len(table_cards),tcount)
		random_cards = choice(cards)
		table_cards.append(random_cards)
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
