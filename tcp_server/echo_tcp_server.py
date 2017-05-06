import socket

def handle(conn):
    while True:
        message = conn.recv(1024)
        if message == b"\r\n":
            break
        conn.sendall(message)
    conn.close()


def run_server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(("", 8080))
    sock.listen(1)
    print("Running at {}".format(sock.getsockname()))

    conn, addr = sock.accept()
    print("Connected to {}".format(addr))
    handle(conn)

    sock.close()

if __name__ == "__main__":
    run_server()