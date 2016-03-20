from jsonrpc2_zeromq import RPCServer
from firewall import Firewall
from src.leap.bitmask_root.bitmask_root_abstraction import BitmaskRoot
from openvpn import *

host = "127.0.0.1"
port = "8080"


class BitmaskRootWindows(RPCServer, BitmaskRoot):
    def handle_stop_ovpn_method(self):
        ovpn = OpenVPNLauncher()
        ovpn.terminate()

    def handle_start_ovpn_method(self, config, log):
        if Tools.windows_has_tap_device() and Tools.is_ovpn_installed():
            ovpn = OpenVPNLauncher()
            ovpn.launch(config, log)
            return True
        return False

    def handle_start_firewall_method(self):
        firewall = Firewall()
        firewall.start()

    def handle_stop_firewall_method(self):
        firewall = Firewall()
        firewall.stop()

    def handle_test_service_method(self):
        return True


if __name__ == '__main__':
    pass
