from abc import ABCMeta, abstractmethod


class Bitmask_Root:
    __metaclass__ = ABCMeta

    @abstractmethod
    def StartFirewall(self): pass

    @abstractmethod
    def StopFirewall(self): pass

    @abstractmethod
    def StartOVPN(self): pass

    @abstractmethod
    def StopOVPN(self): pass
