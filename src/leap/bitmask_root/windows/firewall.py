import subprocess


class Firewall:
    def __init__(self):
        pass

    def stop(self):
        subprocess.call(['netsh', 'advfirewall', 'set', 'allprofiles', 'state', 'off'])
        return self.get_firewall_status()

    def start(self):
        subprocess.call(['netsh', 'advfirewall', 'set', 'allprofiles', 'state', 'on'])
        return self.get_firewall_status()

    def get_firewall_status(self):
        cmd = subprocess.Popen(['netsh', 'advfirewall', 'show', 'currentprofile'], stdout=subprocess.PIPE)
        out = cmd.stdout.readlines()

        for line in out:
            if line.startswith('State'):
                if line.split()[1] == "ON":
                    return True
                else:
                    return False