import socket

# ip_address = "192.168.85.1"
# port = 1027
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
client.connect(("192.168.85.1", 56178))
client.send("I'm a Client\n".encode())
from_server=client.recv(4096)
client.close()
print(from_server)