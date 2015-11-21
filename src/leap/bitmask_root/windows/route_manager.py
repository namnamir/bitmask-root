import subprocess

default_gw_filename = 'defaultgw'


class RouteManager:
    def __init__(self):
        pass

    def restore_saved_default_gateway(self):
        try:
            with open(default_gw_filename) as f:
                default_getway = f.read()
                subprocess.call(['route', 'add', '0.0.0.0', 'mask', '0.0.0.0', default_getway])
        except IOError, e:
            self.log.warning(str(e))

    def save_default_gateway(self):
        if self.parse_default_getway() is None:
            self.log.warning('Gateway not found')
        else:
            with open(default_gw_filename, 'w') as f:
                f.write(self.parse_default_getway())

    def remove_default_getway(self):
        subprocess.call(['route', 'delete', '0.0.0.0', 'mask', '0.0.0.0'])

    def parse_default_getway(self):
        cmd = subprocess.Popen(['route', 'print'], stdout=subprocess.PIPE)
        out = cmd.stdout.readlines()
        route_table = False

        for line in out:
            if line.startswith('IPv4 Route Table'):
                route_table = True
            if route_table:
                if line.split()[0] == "0.0.0.0" and line.split()[1] == "0.0.0.0":
                    return line.split()[2]
        return None
