#socket server
import socket

HOST='127.0.0.1'
PORT=2499

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((HOST, PORT))

while True:
	msg = server.recv(1024)
	print(msg.decode("utf-8"))
	username = input("please input username : ")
	password = input("please input password : ")
    
   
