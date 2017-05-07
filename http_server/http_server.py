import socket
import io
import os
import mimetypes


def handle(conn):
    request_string = conn.recv(8192).decode()
    if request_string:
        request = parse_request_string(request_string)
        send_response(conn, request)
    conn.close()

def parse_request_string(request_string):
    request = {}
    head, body = request_string.split("\r\n\r\n")
    lines = head.splitlines()
    request_line = lines[0].split(" ")
    request_headers = lines[1:]

    request['REQUEST_METHOD'] = request_line[0]
    request['PATH_INFO'] = request_line[1]
    request['SERVER_PROTOCOL'] = request_line[2]

    for header in request_headers:
        name, value = header.split(": ", 1)
        name = "HTTP_{}".format(name.replace("-", "_").upper())
        request[name] = value

    request['CONTENT_LENGTH'] = len(body)
    request['BODY'] = body
    return request

def send_response(conn, request):
    response_body = io.BytesIO()
    response_status = "HTTP/1.1 200 OK\r\n"
    response_headers = []

    file_path = request['PATH_INFO'][1:]
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            response_body.write(f.read())
            mimetype = mimetypes.guess_type(request['PATH_INFO'])
            response_headers.append("Content-Type: {}\r\n".format(mimetype[0]))
    else:
        response_body.write(b"404 File Not Found")
        response_status = "HTTP/1.1 404 NOT FOUND\r\n"
        response_headers.append("Content-Type: text/plain\r\n")

    headers = "".join(response_headers)
    start_response = "{}{}\r\n".format(response_status, headers)
    conn.sendall(start_response.encode())
    conn.sendall(response_body.getvalue())
    response_body.close()


def run_server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(("", 8080))
    sock.listen(5)
    print("Running at {}".format(sock.getsockname()))

    while True:
        try:
            conn, addr = sock.accept()
            handle(conn)
        except KeyboardInterrupt:
            print("Shutting down the server")
            break
    sock.close()

if __name__ == "__main__":
    run_server()
