# -*- mode: python ; coding: utf-8 -*-
block_cipher = None

a = Analysis(
    ['$Path$/Source/gui/msasect/Main.py'],
    pathex=[],
    binaries=[
        ('$Path$/build/lib/macarm/libgmsh.4.11.1.dylib', '.'),  # Specify the path to gmsh-4.11.dylib
        ('$Path$/build/lib/macarm/libgmsh.4.11.dylib', '.'),
        ('$Path$/build/lib/macarm/libgmsh.dylib', '.')
    ],
    datas=[
    ('$Path$/Source/gui/msasect/base/library/', 'gui/msasect/base/library'),
    ('$Path$/Source/gui/msasect/ui/ico/', 'gui/msasect/ui/ico'),
    ('$Path$/Source/gui/msasect/ui/Template/', 'gui/msasect/ui/Template'),
    ('$Path$/Source/gui/msasect/help/MSASECT2 User Manual-v1.0.pdf', 'gui/msasect/help')
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='MSASect2',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=None
)

coll = COLLECT( exe,
                a.binaries,
                a.zipfiles,
                a.datas,
                strip=False,
                upx=True,
                upx_exclude=[],
                name="MSASect2")
app = BUNDLE(exe,
         name='MSASect2.app',
         icon=None,
         bundle_identifier=None
         )