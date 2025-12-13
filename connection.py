import socket


class Connection:
    def __init__(self, host_ip, port=8080):
        if host_ip is None:
            host_ip = '127.0.0.1'
        self.host_ip = host_ip
        self.port = port


    def tcp_connection(self, headers):
        # AF_INET is for ipv4, and SOCK_SREAM is for TCP connection
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # first param level: protocol layer
        # second param is the thing to configure, in this case SO_REUSEADDR set to 1 (enabled) means that once the tcp connection closes the address can be reused
        # usually when a tcp
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((self.host_ip, self.port))

        server_socket.listen(5)

        while True:
            conn_socket, (client_ip, client_port) = server_socket.accept()
            print(f"Connection from {client_ip}:{client_port}")

            request = conn_socket.recv(4096)
            print(request.decode(errors="ignore"))

            conn_socket.send(bytes(self._build_tcp_response(headers), "utf-8"))
            conn_socket.shutdown(socket.SHUT_RDWR)
            conn_socket.close()


    def udp_connection(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


    def _build_tcp_response(self, headers):
        body = "Hello world :)\r\n"

        return (
            "HTTP/1.1 200 OK\r\n"
            f"Content-Length: {len(body)}\r\n"
            "\r\n"
            f"{body}\r\n"
        )




if __name__ == "__main__":
    connection = Connection("127.0.0.1", 8080)
    connection.tcp_connection({})