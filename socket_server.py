import socket

def server_program():
    host = socket.gethostname()
    port = 5002
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(2)
    c, a = server_socket.accept()
    print("Connection from: " + str(a))
    while True:
        data = c.recv(1024).decode()
        if not data:
            break
        print('Received from server: ' + data)

        data = input('--> ')
        c.send(data.encode())
    c.close()

if __name__ == '__main__':
    print("Kindly wait for anyone to join with you ")
    server_program()