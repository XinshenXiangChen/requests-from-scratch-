from ExampleTCPConnection import ExampleTCPConnection
from TCP.BaseTCPConnection import BaseTCPConnection

def listen(host_ip="127.0.0.1", host_port=8080):
    connection = ExampleTCPConnection()
    connection.tcp_listen(host_ip, host_port)

def get(url):
    connection = BaseTCPConnection()
    headers = {
        "User-Agent": "curl/7.85.0",  # or any browser UA
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Connection": "close"
    }
    connection.tcp_send("GET", headers, "", url)

def post(url, body="", headers=None):
    pass

def put(url):
    pass

def delete(url):
    pass



if __name__ == '__main__':
    get("www.google.com/")