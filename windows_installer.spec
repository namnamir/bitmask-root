# -*- mode: python -*-
a = Analysis(['windows_installer.py'],
             pathex=['C:\\Users\\Alireza\\Desktop\\bitmask-root'],
             hiddenimports=['UserString','UserList','commands','future.backports.misc','zmq.backend.cython',
             'zmq.backend.cython.constants','zmq.backend.cython.error','zmq.backend.cython.message','zmq.backend.cython.context',
             'zmq.backend.cython.socket','zmq.backend.cython.utils','zmq.backend.cython._poll','zmq.backend.cython._version','zmq.backend.cython._device'
             ],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='windows_installer.exe',
          debug=False,
          strip=None,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=None,
               upx=True,
               name='windows_installer')
