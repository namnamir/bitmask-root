from jsonrpc2_zeromq import RPCServer
from firewall import Firewall
from leap.bitmask_root.bitmask_root_abstraction import BitmaskRoot

host = "127.0.0.1"
port = "8080"

class BitmaskRootWindows(RPCServer,BitmaskRoot):

    def handle_stop_ovpn_method(self):
        pass

    def handle_start_ovpn_method(self):
        pass

    def handle_start_firewall_method(self):
        firewall = Firewall()
        firewall.start()

    def handle_stop_firewall_method(self):
        firewall = Firewall()
        firewall.stop()

if __name__ == '__main__': pass