import unittest
from jsonrpc2_zeromq import RPCClient
from leap.bitmask_root.windows.firewall import Firewall
from leap.bitmask_root.windows.windows_implementation import *

class TestStringMethods(unittest.TestCase):
    def test_get_firewall_status(self):
        firewall = Firewall()
        self.assertIn(firewall.get_firewall_status(), [True, False])

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

if __name__ == '__main__':
    unittest.main()
