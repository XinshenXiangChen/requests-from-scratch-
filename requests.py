from ExampleTCPConnection import ExampleTCPConnection
from TCP.BaseTCPConnection import BaseTCPConnection

def listen(host_ip="127.0.0.1", host_port=8080):
    connection = ExampleTCPConnection(host_ip, host_port)
    connection.tcp_listen()

def get(url):
    pass

def post(url, body="", headers=None):
    pass

def put(url):
    pass

def delete(url):
    pass



if __name__ == '__main__':
    get()