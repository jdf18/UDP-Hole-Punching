import socket
import sys
import threading

class Client:
    def __init__(self, peer_ip_address:str, source_port:int, destination_port:int):
        self.peer_ip_address = peer_ip_address
        self.source_port = source_port
        self.destination_port = destination_port
        
    def punch_hole(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind(("0.0.0.0", self.source_port))
        sock.sendto(b"0", (self.peer_ip_address, self.destination_port))

    def listen(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind(("0.0.0.0", self.source_port))

        while True:
            data = sock.recv(1024)
            print("\rmsg: {}\n> ".format(data.decode()), end="")

    def create_listener(self):
        listener = threading.Thread(target=self.listen, daemon=True, args=tuple())
        listener.start()

    def console(self):
        self.create_listener()

        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind(("0.0.0.0",self.destination_port))

        while True:
            msg = input('> ')
            sock.sendto(msg.encode(), (self.peer_ip_address, self.source_port))

