#socket server
import socket

HOST='13.250.95.31'
PORT=30080

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((HOST, PORT))

while True:
	msg = server.recv(1024)
	print(msg.decode("utf-8"))
	username = input("please input username : ")
	password = input("please input password : ")
    
   
