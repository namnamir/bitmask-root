from src.leap.bitmask_root.windows.route_manager import RouteManager


class Firewall:
    def __init__(self):
        pass

    def stop(self):
        route = RouteManager()
        route.restore_saved_default_gateway()

    def start(self):
        route = RouteManager()
        route.save_default_gateway()
        route.remove_default_getway()
