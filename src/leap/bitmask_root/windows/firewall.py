import subprocess


class Firewall:
    def __init__(self):
        pass

    def stop(self, getway="192.168.1.1"):
        subprocess.call(['route', 'add', '0.0.0.0', 'mask', '0.0.0.0', getway])

    def parse_getway(self):
        cmd = subprocess.Popen(['route', 'print'], stdout=subprocess.PIPE)
        out = cmd.stdout.readlines()
        route_table = False

        for line in out:
            if line.startswith('IPv4 Route Table'):
                route_table = True
            if route_table:
                if line.split()[0] == "0.0.0.0" and line.split()[1] == "0.0.0.0":
                    return line.split()[2]

    def start(self):
        getway = self.parse_getway()
        subprocess.call(['route', 'delete', '0.0.0.0', 'mask', '0.0.0.0'])
        return getway
