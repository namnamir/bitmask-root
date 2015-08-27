import string
import subprocess
from tools import *
from management import OVPNInterface


class OpenVPNLauncher:
    def __init__(self):
        self.proc = None
        self.interface = OVPNInterface()

    def launch(self, cfgfile, logfile):
        try:
            path = os.path.join(Tools.get_bitmask_home(), 'third-party', 'openvpn')
            args = [os.path.join(path, 'openvpn.exe'),
                    "--config", os.path.join(path, 'ovpn', cfgfile),
                    "--log", os.path.join(path, 'log', logfile),
                    "--management", "127.0.0.1", "7505"]

            self.proc = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            if self.proc.returncode:
                raise NotImplementedError(
                    "Executing external OpenVPN process failed returning %s" % self.proc.returncode)
            return self.proc.pid

        except OSError, e:
            raise NotImplementedError("OpenVPN not found")

    def terminate(self):
        procs = Tools.is_openvpn_running()
        if procs:
            for p in procs:
                p.terminate()

    def get_status(self):
        msg = self.interface.send("state\n")
        if msg is not None:
            lines = string.split(msg, os.linesep)
            for l in lines:
                if ',' in l:
                    parts = string.split(l, ",")
                    if len(parts) < 5:
                        continue
                    tstamp, state, desc, tun_ip, remote_ip = parts
                    if state == "CONNECTED" and desc == "SUCCESS":
                        return {'ovpn_state': "CONNECTED", 'interface': tun_ip.split('\r')[0], 'gateway': remote_ip}
                    elif state == "CONNECTED" and desc == "ERROR":
                        return {'ovpn_state': "DISCONNECTED"}
                    else:
                        return {'ovpn_state': state}
                else:
                    continue
        else:
            return {'ovpn_state': "DISCONNECTED"}
