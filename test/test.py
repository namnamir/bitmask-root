import unittest

from src.leap.bitmask.windows.firewall import Firewall


class TestStringMethods(unittest.TestCase):
    def test_get_firewall_status(self):
        firewall = Firewall()
        self.assertIn(firewall.get_firewall_status(), [True, False])

    def test_firewall_start(self):
        firewall = Firewall()
        self.assertAlmostEqual(firewall.start(), True)

    def test_firewall_stop(self):
        firewall = Firewall()
        self.assertAlmostEqual(firewall.stop(), False)

if __name__ == '__main__':
    unittest.main()
