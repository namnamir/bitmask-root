from distutils.core import setup
import sys

sys.argv.append("py2exe")

opts = {'py2exe': {
    'dist_dir': "dist",
    'bundle_files': 1,
    'includes': ['zmq.backend.cython', 'UserList', 'UserString', 'commands', 'future.backports.misc'],
}, }

setup(service=['windows_installer'], options=opts, cmdline_style='pywin32',zipfile=None)
