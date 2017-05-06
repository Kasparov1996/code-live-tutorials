import socket
from datetime import datetime

def run_server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(("", 8080))
    sock.listen(1)
    print("Running at {}".format(sock.getsockname()))

    conn, addr = sock.accept()
    message = "Hello World\r\n{}\r\n".format(datetime.now())
    conn.sendall(message.encode())
    conn.close()
    sock.close()

if __name__ == "__main__":
    run_server()
