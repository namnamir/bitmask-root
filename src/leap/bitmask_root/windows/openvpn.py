import os
import subprocess
import time
from tools import *


class VPNLauncherException(Exception):
    pass


class OpenVPNNotFoundException(VPNLauncherException):
    pass


class OpenVPNLauncher:
    def __init__(self):
        self.proc = None

    def launch(self, cfgfile, logfile):
        try:
            dir = tools.get_bitmask_home() + "\\third-party\\openvpn\\"
            args = [dir + "openvpn.exe", "--config",
                    dir + cfgfile, "--log",
                    dir + logfile, "--management",
                    "127.0.0.1", "7505"]

            self.proc = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            if self.proc.returncode:
                raise VPNLauncherException(
                    "Executing external OpenVPN process failed returning %s" % self.proc.returncode)

            return self.proc.pid

        except OSError, e:
            raise OpenVPNNotFoundException()

    def terminate(self):
        try:
            procs = tools.is_openvpn_running()
            if procs:
                for p in procs:
                    p.terminate()
        except:
            pass
