from time import sleep, time
import unittest
from jsonrpc2_zeromq import RPCClient
from src.leap.bitmask_root.windows.windows_implementation import *
from src.leap.bitmask_root.windows.openvpn import *


class TestStringMethods(unittest.TestCase):
    def test_firewall_start(self):
        client = RPCClient("tcp://%s:%s" % (host, port))
        client.start_firewall()

    def test_firewall_stop(self):
        client = RPCClient("tcp://%s:%s" % (host, port))
        client.stop_firewall("192.168.1.1")

    def test_start_ovpn(self):
        client = RPCClient("tcp://%s:%s" % (host, port))
        client.start_ovpn('sample.ovpn', 'log.txt')
        ovpn = OpenVPNLauncher()
        while ovpn.get_status().get('ovpn_state') != "CONNECTED":
            print ovpn.get_status()
            sleep(1)

    def test_stop_ovpn(self):
        client = RPCClient("tcp://%s:%s" % (host, port))
        client.stop_ovpn()


if __name__ == '__main__':
    unittest.main()
