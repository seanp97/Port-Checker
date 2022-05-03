import sys
import socket
from contextlib import closing

class PortChecker:

    def __init__(self):
        if len(sys.argv) > 1:
            self.host = sys.argv[1]
            self.port = sys.argv[2]

            self.check_socket(self.host, int(self.port))

        else:
            print("Enter host and port:")
            sys.exit()
   

    def check_socket(self, host, port):
        with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
            if sock.connect_ex((host, port)) == 0:
                print(f"Port {self.port} is open")
            else:
                print(f"Port {self.port} is closed")



PortChecker()