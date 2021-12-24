# -*- mode: python ; coding: utf-8 -*-

block_cipher = None
import os

spec_root = os.path.abspath(SPECPATH)


a = Analysis(['main.py'],
             pathex=['C:\\Users',],
             binaries=[('icon.assoc','.')],
             datas=[('script/gui/img', 'script/gui/img')],
             hiddenimports=[],
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
          name='Albie',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          manifest=None,
          console=False,
          icon='script/gui/img/logo1.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='main')
