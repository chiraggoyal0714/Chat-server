import socket
import threading
import sys

class Server:
    sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connections = []
    def __init__(self):
        self.sck.bind(('0.0.0.0',10000))
        self.sck.listen(1)
        print("Server running....")


    def handler(self,c,a):
         while True:
             data = c.recv(1024)
             for connection in self.connections:
                 connection.send(data)
             if not data:
                 print(str(a[0])+ ":" + str(a[1]),'  disconnected')
                 self.connections.remove(c)
                 c.close()
                 break

    def run(self):
        while True:
            c,a = self.sck.accept()
            cThread = threading.Thread(target=self.handler, args=(c,a))
            cThread.daemon = True
            cThread.start()
            self.connections.append(c)
            print(str(a[0]) + ":" + str(a[1]), '  connected')


class Client:
    sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def sendMsg(self):
        while True:
            data = input("")
            self.sck.send(bytes(data, 'utf-8'))

    def __init__(self, address):
        self.sck.connect((address, 10000))
        iThread = threading.Thread(target=self.sendMsg)
        iThread.daemon = True
        iThread.start()
        while True:
            data = self.sck.recv(1024)
            if not data:
                break
            print(str(data, 'utf-8'))

if(len(sys.argv)>1):
    client = Client(sys.argv[1])
else:
    server = Server()
    server.run()