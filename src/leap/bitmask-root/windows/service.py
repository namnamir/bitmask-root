import win32service
import win32event
import socket
import time
from SimpleXMLRPCServer import SimpleXMLRPCServer

import win32serviceutil
import servicemanager

from windows_implementation import BitmaskRootWindows


class AppServerSvc(win32serviceutil.ServiceFramework):
    _svc_name_ = "bitmask-root"
    _svc_display_name_ = "bitmask-root"
    _stoped = False
    _server = SimpleXMLRPCServer(('127.0.0.1', 8080), logRequests=True, allow_none=True)

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        socket.setdefaulttimeout(60)
        self._server.register_introspection_functions()
        self._server.register_multicall_functions()
        self._server.register_instance(BitmaskRootWindows())

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)
        self._stoped = True

    def SvcDoRun(self):
        servicemanager.LogMsg(servicemanager.EVENTLOG_INFORMATION_TYPE,
                              servicemanager.PYS_SERVICE_STARTED,
                              (self._svc_name_, ''))
        self._server.serve_forever()
        self.main()

    def main(self):
        while True:
            if self._stoped:
                break
            pass
            time.sleep(1)


if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(AppServerSvc)
