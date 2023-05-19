# Important notice: PLEASE SHUT DOWN ANTIVIRUS SOFTWARE!
import os
import subprocess
import shutil
import platform
import datetime
import zipfile

import gui.msasect.Configuration as Conf

def replace_file_path(file_path, new_path):
    # Open the 'MacARM.spec' file
    with open(file_path, 'r') as file:
        content = file.read()

    # Replace the string "$Path$" with the given file path
    updated_content = content.replace('$Path$', new_path)

    # Save the updated content to a new file named 'temp.spec'
    with open('temp.spec', 'w') as file:
        file.write(updated_content)


Version = Conf.Version
now = datetime.datetime.now()
current_time = now.strftime("%Y%m%d")
zip_file_name = f"./build/release/windows/{current_time}-MSASect2-v{Version}-Windows.zip"

def run_pyinstaller(spec_file):
    cmd = ['pyinstaller', spec_file]
    subprocess.run(cmd, check=True)

# Specify the path to the spec file based on the operating system
system = platform.system()
if system == 'Windows':
    spec_file_path = 'Windows.spec'
elif system == 'Darwin' and platform.machine() == 'x86_64':
    spec_file_path = 'MacX86.spec'
elif system == 'Darwin' and platform.machine() == 'arm64':

    current_file_path = os.path.abspath(__file__)
    folder_path = os.path.dirname(current_file_path)

    file_path = 'MacARM.spec'
    new_path = folder_path
    replace_file_path(file_path, new_path)
    spec_file_path = 'temp.spec'
else:
    raise Exception('Unsupported operating system')

# Run PyInstaller with the specified spec file
run_pyinstaller(spec_file_path)

if system == 'Windows':

    release_folder = './build/release/windows/' + Version

    # Delete the release folder if it exists
    if os.path.exists(release_folder):
        shutil.rmtree(release_folder)

    # Delete the zip file if it exists
    if os.path.exists(zip_file_name):
        os.remove(zip_file_name)

    # Copy base/library folder
    shutil.copytree('./Source/gui/msasect/base/library', './dist/base/library')

    # Copy ui/ico folder
    shutil.copytree('./Source/gui/msasect/ui/ico', './dist/ui/ico')

    # Copy ui/Template folder
    shutil.copytree('./Source/gui/msasect/ui/Template', './dist/ui/Template')

    # Copy the PDF file
    shutil.copytree('./Source/gui/msasect/help/', './dist/help')

    # Delete the build/Windows folder
    shutil.rmtree('./build/Windows')

    # Create the new 'release' folder
    os.makedirs('./build/release', exist_ok=True)

    # Move the 'dist' folder to the new 'release' folder and rename it as 'windows'
    shutil.move('./dist', release_folder)

    src_dir = f"./build/release/windows/{Version}"
    dest_dir = "./build/release/windows"
    with zipfile.ZipFile(zip_file_name, mode='w', compression=zipfile.ZIP_DEFLATED) as zf:
        for foldername, subfolders, filenames in os.walk(src_dir):
            for filename in filenames:
                file_path = os.path.join(foldername, filename)
                arcname = os.path.relpath(file_path, src_dir)
                zf.write(file_path, arcname)


elif system == 'Darwin' and platform.machine() == 'x86_64':
    print("Mac OS - x86")

elif system == 'Darwin' and platform.machine() == 'arm64':
    print("Mac OS - ARM")

    release_folder = './build/release/MacARM/' + Version

    # Delete the build/Windows folder
    shutil.rmtree('./build/temp')

    # Create the new 'release' folder
    os.makedirs('./build/release')

    # Move the 'dist' folder to the new 'release' folder and rename it as 'windows'
    shutil.move('./dist', release_folder)

    # Delete the build/Windows folder
    #shutil.rmtree('./build/MacARM')

    # Check if the file exists before attempting to delete it
    if os.path.exists('temp.spec'):
        os.remove('temp.spec')

else:
    raise Exception('Unsupported operating system')




