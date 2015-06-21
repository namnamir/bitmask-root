from SimpleXMLRPCServer import SimpleXMLRPCServer


server = SimpleXMLRPCServer(('localhost', 9000), logRequests=True, allow_none=True)
server.register_introspection_functions()
server.register_multicall_functions()

class BitmaskRootWindows(bitmask_root_abstraction):

    def start_ovpn(self): pass