import socket

hostname = socket.gethostname()
LAN_IP = socket.gethostbyname(hostname)
print(LAN_IP)
LAN_PORT = 8080

# AF_INET is for ipv4, and SOCK_SREAM is for TCP connection
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# first param level: protocol layer
# second param is the thing to configure, in this case SO_REUSEADDR set to 1 (enabled) means that once the tcp connection closes the address can be reused
# usually when a tcp
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((LAN_IP, LAN_PORT))

server_socket.listen(5)

while True:
    conn_socket, (client_ip, client_port) = server_socket.accept()
    print(f"Connection from {client_ip}:{client_port}")
    conn_socket.send(bytes("GET / HTTP/1.0\r\n\r\n", "utf-8"))
    conn_socket.close()