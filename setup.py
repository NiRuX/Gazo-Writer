#!/usr/bin/env python3
# script to install dd-gui on unix-like systems
import os, os.path, sys, shutil, pathlib, random

__PKG_NAME__ = "dd-gui"
__PKG_VERSION__ = "0.5"
__PKG_SOURCES__ = f"{os.getcwd()}/{__PKG_NAME__}.py"
__PKG_DEPS__ = "PyQt5"

try:
    __PKG_DEST__ = os.environ['DESTDIR']
except:
    __PKG_DEST__ = "/"

try:
    __PKG_PREFIX__ = os.environ['PREFIX']
except:
    __PKG_PREFIX__ = "/usr/local"

def do_install():
    print(f"---> Starting install process for {__PKG_NAME__}")
    print("--> Installing dependiences")
    os.system(f"python3 -m pip install {__PKG_DEPS__}")
    print("--> Copying files...")
    try:
        os.system(f"mkdir -p {__PKG_DEST__}/{__PKG_PREFIX__}/bin")
        shutil.copy(__PKG_SOURCES__, f"{__PKG_DEST__}/{__PKG_PREFIX__}/bin/{__PKG_NAME__}")
        os.system(f"chmod 775 {__PKG_DEST__}/{__PKG_PREFIX__}/bin/{__PKG_NAME__}")
        print("Installation succeeded.")
    except:
        print("Looks like the install failed. Try re-running this script as root.")
        sys.exit(1)

if __name__ == '__main__':
    do_install()
