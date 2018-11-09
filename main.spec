# # -*- coding: utf-8 -*-
# -*- mode: python -*-

block_cipher = None


a = Analysis(['main.py','help1.py','shangChuan.py','UpdatesoilT.py'],
             pathex=['E:\\PythonFile\\first-GUI\\yjtd'],
             binaries=[],
             datas=[('E:\\PythonFile\\first-GUI\\yjtd\\images','images')],
             hiddenimports=['yjtd'],
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
          exclude_binaries=True,
          name='main',
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
               name='main')
