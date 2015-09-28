from distutils.core import setup
import py2exe
import sys

sys.argv.append('py2exe')

opts = {'py2exe': {
    'dist_dir': 'dist',
    'dll_excludes': ['OLEAUT32.dll', 'USER32.dll', 'SHELL32.dll', 'ole32.dll', 'MSVCP90.dll',
                     'ADVAPI32.dll', 'NETAPI32.dll', 'WS2_32.dll', 'GDI32.dll', 'VERSION.dll', 'KERNEL32.dll'],
    'bundle_files': 2,
    'optimize': 2,
    'includes': ['zmq.backend.cython', 'UserList', 'UserString', 'commands', 'future.backports.misc'],
}, }

setup(service=['windows_installer'], options=opts, cmdline_style='pywin32', zipfile=None)
