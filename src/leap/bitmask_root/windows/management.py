import socket
import time


class OVPNInterface:
    def __init__(self):
        self.sock = None
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.settimeout(2)
        self.connected = False

    def send(self, command):
        try:
            if not self.connected:
                self.sock.connect(("127.0.0.1", 7505))
                self.connected = True
            self.sock.send(command)
            time.sleep(0.5)
            result = self.sock.recv(1024)
            return result
        except Exception:
            return None

    def terminate(self):
        self.send("signal SIGTERM\n")
