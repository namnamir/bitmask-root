class BitmaskRoot:
    def __init__(self):
        pass

    def start_firewall(self):
        raise NotImplementedError()

    def stop_firewall(self):
        raise NotImplementedError()

    def start_ovpn(self):
        raise NotImplementedError()

    def stop_opvn(self):
        raise NotImplementedError()
