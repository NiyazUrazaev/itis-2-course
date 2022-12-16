import socket


def start_client():
    host = socket.gethostname()
    port = 5123

    client_socket = socket.socket()
    client_socket.connect((host, port))

    message = input(' -> ')

    while message != 'bye':
        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()
        print(f'Get from server: {data}')

        message = input(' -> ')

    client_socket.close()


if __name__ == '__main__':
    start_client()