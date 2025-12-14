from enum import Enum

from TCP.HttpConst import HTTP_STATUS_CODES, HTTP_HEADERS



class StatusCodes(Enum):
    SUCCESS = 200
    MalformedResponse = 400
    NotSupported = 505

# this returns the method, and a dictionary f headers
def parse_tcp_request(request):
    parts = request.split()

    # request line is malformed
    if len(parts) < 3:
        return {"error": HTTP_STATUS_CODES.get(StatusCodes.MalformedResponse)}, StatusCodes.MalformedResponse

    method, path, version = parts[:3]

    protocol_name, protocol_version = version.split("/")

    # version has a weird non normal format
    if len(version.split('/')) != 2:
        return {"error": HTTP_STATUS_CODES.get(StatusCodes.MalformedResponse)}, StatusCodes.MalformedResponse

    # protocol_name is not in protocls
    if protocol_name not in protocols:
        return {"error": HTTP_STATUS_CODES.get(StatusCodes.MalformedResponse)}, StatusCodes.MalformedResponse
    else:
        # protocol version is not suppported, TODO: Probably make protocols a user defined dict of allowed protocols and versions
        if protocol_version not in protocols[protocol_name]:
            return {"error": HTTP_STATUS_CODES.get(StatusCodes.NotSupported)}, StatusCodes.NotSupported


    method_and_headers, body = request.split("\r\n\r\n")
    headers = method_and_headers.split("\r\n")

    headers_dict = {}
    found_host = False
    for header in headers:
        if ": " in header:
            header, value = header.split(":", 1)
            if header == "Host":
                found_host = True
            headers_dict[header] = value

    if protocol_version == "1.1" and not found_host:
        return {"error": HTTP_STATUS_CODES.get(StatusCodes.MalformedResponse)}, StatusCodes.MalformedResponse


    # this does not handle 3xx status codes (for now) code is probably absurdly inefficient.

    return {"method": method, "path": path, "version": version, "headers": headers_dict, "body": body}, StatusCodes.SUCCESS



def parse_tcp_response(response):
    pass