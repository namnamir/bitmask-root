from src.leap.bitmask_root.windows.route import Route


class Firewall:
    def __init__(self):
        pass

    def stop(self):
        route = Route()
        route.restore_saved_default_gateway()

    def start(self):
        route = Route()
        route.save_default_gateway()
        route.remove_default_getway()
