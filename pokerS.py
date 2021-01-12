#server.py
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
client_ID = " "
clients_ID = []


#Theread client
def threaded_client(connection):
	print("Conenction establish \n")
	global clients,player_data,client_name
	ptotal = 0

	client_ID = connection.recv(1024).decode("utf-8")
	clients_ID.append(client_ID)

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
				time.sleep(2)
		if len(player_data) == 2:
				point1 = player_data[0].get("player point")
				point2 = player_data[1].get("player point")
				print(point1)
				print(point2)
				msg2 = {
						"point1":point1,
						"point2":point2,
						"text":" "
				}
				if point1 > point2:
						if point1 <= 21:
								msg2["text"] = "YOU WIN"
								msgSent = pickle.dumps(msg2)
								player_data[0].get("socket").send(msgSent)
								msg2["text"]="SORRY YOU LOSE"
								msgSent = pickle.dumps(msg2)
								player_data[1].get("socket").send(msgSent)
						else:
								msg2["text"]="SORRY YOU LOSE"
								msgSent = pickle.dumps(msg2)
								player_data[0].get("socket").send(msgSent)
								msg2["text"] = "YOU WIN"
								msgSent = pickle.dumps(msg2)
								player_data[1].get("socket").send(msgSent)
				elif point2 > point1:
						if point2 <= 21:
								msg2["text"]="SORRY YOU LOSE"
								msgSent = pickle.dumps(msg2)
								player_data[0].get("socket").send(msgSent)
								msg2["text"] = "YOU WIN"
								msgSent = pickle.dumps(msg2)
								player_data[1].get("socket").send(msgSent)
						else:
								msg2["text"] = "YOU WIN"
								msgSent = pickle.dumps(msg2)
								player_data[0].get("socket").send(msgSent)
								msg2["text"]="SORRY YOU LOSE"
								msgSent = pickle.dumps(msg2)
								player_data[1].get("socket").send(msgSent)
		player_data = []



	connection.close()


#Main
while True:
	client,addr = s.accept()
	print("Connected to : "+addr[0]+":"+str(addr[1]))
	clients.append(client)
	start_new_thread(threaded_client,(client,))
	ThreadCount += 1
s.close()
