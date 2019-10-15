# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['ctpbee_desktop.py'],
             pathex=['/home/faith/GIT/ctpbee_desktop'],
             binaries=[],
             datas=[("app/static","static"),("venv/lib/python3.7/site-packages/ctpbee-0.31.3-py3.7-linux-x86_64.egg/ctpbee",'ctpbee'),
             ("venv/lib/python3.7/site-packages/PySide2","PySide2")],
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
          name='ctpbee_desktop',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='ctpbee_desktop')
