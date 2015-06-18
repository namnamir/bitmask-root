import win32service
import win32event
import socket
import time
import win32serviceutil
import servicemanager
from windows_implementation import BitmaskRootWindows


class AppServerSvc(win32serviceutil.ServiceFramework):
    _svc_name_ = "bitmask-root"
    _svc_display_name_ = "bitmask-root"
    _stoped = False
    _server = BitmaskRootWindows("tcp://127.0.0.1:8080")

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        socket.setdefaulttimeout(60)

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)
        self._stoped = True

    def SvcDoRun(self):
        servicemanager.LogMsg(servicemanager.EVENTLOG_INFORMATION_TYPE,
                              servicemanager.PYS_SERVICE_STARTED,
                              (self._svc_name_, ''))
        self._server.run()
        self.main()

    def main(self):
        while True:
            if self._stoped:
                break
            pass
            time.sleep(1)


if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(AppServerSvc)
