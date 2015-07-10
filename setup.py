from py2exe.build_exe import py2exe
from distutils.core import setup
import os
import zmq.libzmq

opts = {'py2exe': {
    'dist_dir': "dist",
    'includes': ['zmq.backend.cython', 'UserList', 'UserString', 'commands', 'future.backports.misc'],
}, }

setup(service=['windows_installer'], options=opts, cmdline_style='pywin32')
