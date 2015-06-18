from jsonrpc2_zeromq import RPCServer
from leap.bitmask_root.bitmask_root_abstraction import BitmaskRoot
from leap.bitmask_root.windows.firewall import Firewall


class BitmaskRootWindows(BitmaskRoot, RPCServer):
    def handle_start_firewall_method(self):
        firewall = Firewall()
        firewall.start()

    def handle_stop_firewall_method(self):
        firewall = Firewall()
        firewall.stop()

    def handle_start_ovpn_method(self): pass

    def handle_stop_opvn_method(self): pass
