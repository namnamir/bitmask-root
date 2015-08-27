class BitmaskRoot:
    def handle_start_firewall_method(self):
        raise NotImplementedError()

    def handle_stop_firewall_method(self):
        raise NotImplementedError()

    def handle_start_ovpn_method(self):
        raise NotImplementedError()

    def handle_stop_ovpn_method(self):
        raise NotImplementedError()

    def handle_test_service_method(self):
        raise NotImplementedError()
