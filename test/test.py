import unittest
from jsonrpc2_zeromq import RPCClient
from os.path import abspath, dirname
from src.leap.bitmask_root.windows.firewall import *
from src.leap.bitmask_root.windows.windows_implementation import *
from src.leap.bitmask_root.windows.tools import tools
from src.leap.bitmask_root.windows.openvpn import *


class TestStringMethods(unittest.TestCase):
    def test_firewall_start(self):
        client = RPCClient("tcp://%s:%s" % (host, port))
        client.start_firewall()
        firewall = Firewall()
        self.assertAlmostEqual(firewall.get_firewall_status(), True)

    def test_firewall_stop(self):
        client = RPCClient("tcp://%s:%s" % (host, port))
        client.stop_firewall()
        firewall = Firewall()
        self.assertAlmostEqual(firewall.get_firewall_status(), False)

    def test_start_ovpn(self):
        client = RPCClient("tcp://%s:%s" % (host, port))
        self.proc = psutil.Process(client.start_ovpn('sample.ovpn', 'log.txt'))
        self.assertAlmostEqual(self.proc.is_running(), True)

    def test_stop_ovpn(self):
        client = RPCClient("tcp://%s:%s" % (host, port))
        client.stop_ovpn()
        self.assertAlmostEqual(len(tools.is_openvpn_running()), 0)
        pass


if __name__ == '__main__':
    unittest.main()
