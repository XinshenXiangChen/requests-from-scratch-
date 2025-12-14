from ExampleTCPConnection import ExampleTCPConnection
from .TCP.BaseTCPConnection import BaseTCPConnection

def listen(host_ip="127.0.0.1", host_port=8080):
    connection = ExampleTCPConnection(host_ip, host_port)
    connection.tcp_listen()
    connection.handle_request()

def post(url):
    pass

def put(url):
    pass

def delete(url):
    pass

