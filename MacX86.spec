# -*- mode: python ; coding: utf-8 -*-
block_cipher = None

a = Analysis(
    ['./Source/gui/msasect/Main.py'],
    pathex=['.'],
    binaries=[('./build/lib/macx86/libgmsh.4.11.1.dylib', '.')],  # Specify the path to gmsh-4.11.dll
    datas=[
    # Existing entries...
    #('./Source/gui/msasect/base/library', 'base/library'),  # Copy base/library folder
    #('./Source/gui/msasect/ui/ico', 'ui/ico'),  # Copy ui/ico folder
    #('./Source/gui/msasect/ui/Template', 'ui/Template'),  # Copy ui/Template folder
    #('./Source/gui/msasect/help/MSASECT2 User Manual-v1.0.pdf', 'help')  # Include the PDF file
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,

)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='MSASect2',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['./Source/gui/msasect/MSASect2.ico'],
)
