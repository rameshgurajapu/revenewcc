# -*- mode: python -*-

import os

import gooey
from PyInstaller.building.api import EXE, PYZ, COLLECT
from PyInstaller.building.build_main import Analysis
from PyInstaller.building.datastruct import Tree
from PyInstaller.building.osx import BUNDLE

gooey_root = os.path.dirname(gooey.__file__)
gooey_languages = Tree(os.path.join(gooey_root, 'languages'), prefix='gooey/languages')
gooey_images = Tree(os.path.join(gooey_root, 'images'), prefix='gooey/images')

block_cipher = None

# noinspection PyUnresolvedReferences
a = Analysis(['revenewCC/ranking.py'],
             pathex=['/Users/mj/repos/revenewcc'],
             datas=[
             ('LICENSE', '.'),
             ('MANIFEST.in', '.'),
             ('revenewCC/inputdata/*.csv', 'inputdata'),
             ('revenewCC/inputdata/*.xlsx', 'inputdata'),
             ('revenewCC/inputdata/*.pkl', 'inputdata'),
             ],
             binaries=[('/Users/mj/opt/anaconda3/lib/libpython3.7m.dylib', '.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
          cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='ranking',
          debug=False,
          strip=False,
          upx=True,
          console=True)
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               gooey_languages,
               gooey_images,
               strip=False,
               upx=True,
               name='ranking')

app = BUNDLE(coll,
             name='ranking.app',
             icon=None,
             bundle_identifier=None,
             info_plist={
                 'NSHighResolutionCapable': 'True'
             }
             )