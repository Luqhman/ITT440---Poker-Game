#server.py
from random import choice
import sys
import socket
from _thread import *
import itertools
import re
import json
import pickle
import time


#create a socket object
s = socket.socket()

#get local machine name
host = ""
port = 8888
ThreadCount = 0
#bind to the port
s.bind((host,port))
print("Socket is bind")
s.listen(5)
print("Socket is listening")
#Waiting for connection from client
print("Waiting for connection from client")

clients = []
player_data = []


#Theread client
def threaded_client(connection):
	print("Conenction establish \n")
	global clients,player_data
	ptotal = 0
	while True:


		#received data from client
		mydata = connection.recv(1000)
		if not mydata:break

		dataDic = pickle.loads(mydata)
		print(dataDic["player id"])
		point1 = 0
		point2 = 0
		pid = dataDic["player id"]
		pp = dataDic["player point"]
		pc = dataDic["check"]


		msg = {
			"socket": connection,
			"player id": pid,
			"player point": pp
		}


		if len(player_data) < 2:
			player_data.append(msg)
		if len(player_data) == 2:
			point1 = player_data[0].get("player point")
			point2 = player_data[1].get("player point")
			print(point1)
			print(point2)
			if point1 > point2:
				if point1 <= 21:
					player_data[0].get("socket").send(b"Nice you win")
					player_data[1].get("socket").send(b"Sorry you lose")
				else:
					player_data[0].get("socket").send(b"Sorry you lose")
					player_data[1].get("socket").send(b"Nice you win")
			elif point2 > point1:
				if point2 <= 21:
					player_data[0].get("socket").send(b"Sorry you lose")
					player_data[1].get("socket").send(b"Nice you win")
				else:
					player_data[0].get("socket").send(b"Nice you win")
					player_data[1].get("socket").send(b"Sorry you lose")


	connection.close()


#Main
while True:
	client,addr = s.accept()
	print("Connected to : "+addr[0]+":"+str(addr[1]))
	clients.append(client)
	start_new_thread(threaded_client,(client,))
	ThreadCount += 1
s.close()
