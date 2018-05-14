import socket


def client_program():
    host = socket.gethostname()
    port = 5002
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    message = input("--> ")

    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()
        print('Received from server: ' + data)
        message = input("--> ")
    client_socket.close()


if __name__ == '__main__':
    print("To end type bye")
    client_program()