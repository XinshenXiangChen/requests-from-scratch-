import socket
from abc import abstractmethod, ABC
from typing import Any

from .TCPUtils import parse_tcp_request, StatusCodes
from .HttpConst import HTTP_STATUS_CODES, HTTP_HEADERS, methods


class BaseTCPConnection():
    def __init__(self, host_ip="127.0.0.1", port=8080):
        self.host_ip = host_ip
        self.port = port

    """
                        *** TCP SERVER ***
    """

    # Listens for connections
    # TODO: Connection pooling integration
    def tcp_listen(self):
        # AF_INET is for ipv4, and SOCK_SREAM is for TCP connection
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # first param level: protocol layer
        # second param is the thing to configure, in this case SO_REUSEADDR set to 1 (enabled) means that once the tcp connection closes the address can be reused
        # usually when a tcp
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((self.host_ip, self.port))

        server_socket.listen(1)


        conn_socket, (client_ip, client_port) = server_socket.accept()
        print(f"Connection from {client_ip}:{client_port}")
        request = conn_socket.recv(4096)

        decoded_request = request.decode(errors="ignore")


        # returns a dictionary
        parsed_tcp_request, status_code = parse_tcp_request(decoded_request)

        request_handle_return = self.handle_request(parsed_tcp_request, status_code)


        conn_socket.send(bytes(self._response_to_string(request_handle_return), "utf-8"))
        conn_socket.shutdown(socket.SHUT_RDWR)
        conn_socket.close()


    # this should return a dict {}, with status line
    def handle_request(self, tcp_request, status_code) -> dict:
        """
        Generates a proper HTTP response dictionary based on parsed tcp_request.
        tcp_request: tuple(parsed_request_dict, StatusCodes)
        """


        # Example handle_request implementation
        parsed_request, status = tcp_request, status_code

        response_body = ""
        status_line = ""
        response_headers = {}

        # Handle errors first
        if status != StatusCodes.SUCCESS:
            # Use the error message from your HTTP_STATUS_CODES mapping
            response_body = parsed_request.get("error", "Error")
            status_line = f"HTTP/1.1 {status.value} {HTTP_STATUS_CODES.get(status, 'Error')}\r\n"
            response_headers["Content-Type"] = "text/plain"
        else:

            response_body = f"Default response from BaseTCPConnection for {parsed_request['path']}\r\n"
            status_line = "HTTP/1.1 200 OK\r\n"
            response_headers["Content-Type"] = "text/plain"

        response_headers["Content-Length"] = str(len(response_body.encode("utf-8")))
        response_headers["Connection"] = "close"

        return {
            "status_line": status_line,
            "headers": response_headers,
            "body": response_body
        }


    # convert handle_request dictionary to string
    def _response_to_string(self, response) -> str:

        print(response)

        string_response = ""

        for key, value in response.items():
            if key == "status_line" or key == "body":
                string_response += f"{value}"

            # handle headers
            else:
                for header, header_value in value.items():

                    string_response += f"{header}: {header_value.removesuffix("\r\n")}\r\n"

                string_response += f"\r\n"

        return string_response


    """
                        *** TCP CLIENT ***
    """

    def tcp_send(self, request_method, headers, body):
        if request_method not in methods:
            raise Exception(f"Request method {request_method} is not supported.")



    def _request_to_string(self, headers, body):
        pass


if __name__ == "__main__":
    connection = BaseTCPConnection("127.0.0.1", 8080)
    connection.tcp_listen()