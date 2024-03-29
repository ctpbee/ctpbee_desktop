# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['sht.py'],
             pathex=['venv\\Lib\\site-packages\\shiboken2'],
             binaries=[],
             datas=[("app/static","static"),
             ('venv/Lib/site-packages/PySide2','PySide2'),
             ("venv/Lib/site-packages/ctpbee",'ctpbee')
             ],
             hiddenimports=['PySide2.QtPrintSupport'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='sht',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False,
           icon='C:\\Users\\ljunf\\GIT\\ctpbee_desktop\\bee64.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='sht')
