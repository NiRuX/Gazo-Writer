 #/bin/bash

 #Determine OS Type
 echo "Determining OS type..."

if [[ $os =~ "arch" ]]; then
 sudo pacman -S pyqt5
 ./dd-gui.py

elif [[ "$os" =~ "debian" ]]; then
  sudo apt install pyqt5-dev
  ./dd-gui.py

elif [[ "$os" =~ "fedora" ]]; then
 sudo dnf install pyqt5
else
  echo "Unrecognized System: $os"
  exit 1
fi
