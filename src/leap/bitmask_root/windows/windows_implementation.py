from jsonrpc2_zeromq import RPCServer
from firewall import Firewall
from bitmask_root_abstraction import BitmaskRoot

class BitmaskRootWindows(RPCServer,BitmaskRoot):
    def handle_stop_ovpn_method(self):
        pass

    def handle_start_ovpn_method(self):
        pass

    def handle_print_ovpn_method(self):
        print "Hello"

    def handle_start_firewall_method(self):
        firewall = Firewall()
        firewall.start()

    def handle_stop_firewall_method(self):
        firewall = Firewall()
        firewall.stop()


if __name__ == '__main__': pass