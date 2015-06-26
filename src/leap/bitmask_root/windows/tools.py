import _winreg as reg
import psutil as psutil


class tools:
    @staticmethod
    def is_openvpn_running():
        try:
            procs = []
            for p in list(psutil.process_iter()):
                try:
                    if p.name() and ('openvpn' in p.name().lower()):
                        procs.append(p)
                except psutil.AccessDenied as e:
                    continue
            return procs
        except psutil.NoSuchProcess as e:
            return procs

    @staticmethod
    def windows_has_tap_device():
        adapter_key = 'SYSTEM\CurrentControlSet\Control\Class' \
                      '\{4D36E972-E325-11CE-BFC1-08002BE10318}'
        with reg.OpenKey(reg.HKEY_LOCAL_MACHINE, adapter_key) as adapters:
            try:
                for i in xrange(10000):
                    key_name = reg.EnumKey(adapters, i)
                    with reg.OpenKey(adapters, key_name) as adapter:
                        try:
                            component_id = reg.QueryValueEx(adapter, 'ComponentId')[0]
                            if component_id.startswith("tap0901"):
                                return True
                        except WindowsError:
                            pass
            except WindowsError:
                pass
        return False
