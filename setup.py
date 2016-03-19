import os
from distutils.core import setup
import py2exe
import zmq.libzmq
from py2exe.build_exe import Target

service = Target(
    description="Administrative service for bitmask client",
    modules=["windows_installer"],
    cmdline_style='pywin32',
)

opts = {'py2exe': {
    'dll_excludes': ['libzmq.pyd', 'OLEAUT32.dll', 'USER32.dll', 'SHELL32.dll', 'ole32.dll',
                     'MSVCP90.dll', 'ADVAPI32.dll', 'NETAPI32.dll', 'WS2_32.dll', 'GDI32.dll',
                     'VERSION.dll', 'KERNEL32.dll', 'WINSPOOL.DRV', 'mfc90.dll', 'ntdll.dll'],
    'includes': ['UserList', 'UserString', 'commands', 'zmq.backend.cython'],
    'dist_dir': "dist"
}}

setup(service=[service], options=opts, zipfile=None,
      data_files=[(os.path.join(os.getcwd(), 'dist'), (zmq.libzmq.__file__,))])
