#server.py
import random
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
