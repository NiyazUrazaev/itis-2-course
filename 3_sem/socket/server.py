import socket

def start_server():
    host = socket.gethostname()
    port = 5123

    server_socket = socket.socket()
    server_socket.bind((host, port))

    server_socket.listen(2)

    conn, address = server_socket.accept()
    print(f'Connected user: {address}')

    while True:
        data = conn.recv(1024).decode()
        print(f'From user: {str(data)}')

        if not data:
            break

        data = input(' -> -: ')
        conn.send(data.encode())

    conn.close()


if __name__ == '__main__':
    start_server()


