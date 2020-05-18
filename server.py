#socket server
import socket

HOST=socket.gethostbyname(socket.gethostname())
PORT=2499

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)
# socket.AF_INET > untuk IPv4
# socket.SOCK_STREAM menggunakan protocol tcp
# server.bind untuk binding on hostname/ip:port
# server.listen(5) connection/5 user
#test edit


while True:
	clientsocket, address = server.accept()
	print(f"connection from {address} has been established")
	clientsocket.send(bytes("Welcome to the server!", "utf-8"))
	

