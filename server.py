import socket


# ip_address = "192.168.85.1"

# print(f"IP Address: {ip_address}")
# port = 1027

serv = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # create a new socket
serv.bind(("192.168.85.1", 56178)) # bind socket with address
serv.listen()

while True:
    conn , addr = serv.accept()
    data = conn.recv(4096)
    from_client = ''.encode()
    if not data:
        break
    from_client += data
    # print(conn.sendall("connection successful"))
    print(from_client)
    conn.send("I'm a Server\n".encode())
conn.close()
print("client Disconnected")