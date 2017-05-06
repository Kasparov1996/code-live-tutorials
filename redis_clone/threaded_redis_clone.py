import socket
import threading

local = threading.local()

def handle(conn):
    local.data = {}
    while True:
        message = conn.recv(1024).decode()
        fields = message.rstrip("\r\n").split(" ")
        command = fields[0]
        if command == "QUIT":
            break
        if len(fields) < 2:
            continue

        if command == "GET":
            key = fields[1]
            value = local.data.get(key)
            conn.sendall("{}\r\n".format(value).encode())
        elif command == "SET":
            if len(fields) != 3:
                conn.send("EXPECTED VALUE\r\n".encode())
                continue
            key = fields[1]
            value  = fields[2]
            local.data[key] = value
        elif command == "DEL":
            key = fields[1]
            local.data.pop(key)
        else:
            conn.sendall("INVALID COMMAND {}\r\n".format(command).encode())

    conn.close()


def run_server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(("", 8080))
    sock.listen(1)
    print("Running at {}".format(sock.getsockname()))

    while True:
        try:
            conn, addr = sock.accept()
            print("Connected to {}".format(addr))
            threaded_handler = threading.Thread(target=handle, args=(conn,))
            threaded_handler.start()
        except KeyboardInterrupt:
            print("Shutting down server")
            break

    sock.close()

if __name__ == "__main__":
    run_server()