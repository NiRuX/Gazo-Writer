<p align="center"><img src="http://codeberg.org/glowiak/dd-gui/raw/branch/master/screenshot.bmp"></p>

# WARNING

please don't use this

or if you specifically want to use this crap anyway, you do it at your own risk

i don't take responsibility if you wreck your hdd with this

# dd-gui - Destroying disks made easier

a simple gui for dd, like rufus

made because i was tired of manually typing dd with all it's flags every time i want to get rid of my hard disk

i don't think anyone except me is gonna use this crap but anyway it's here

### Running

Download latest release and run. Alternatively you can run it with curl:

	curl -L http://codeberg.org/glowiak/dd-gui/raw/branch/master/dd-gui.py | python3

If you want to install it, run as root:

	./setup.py

you can pass the DESTDIR and PREFIX env flags to this.

### Flags

The available env flags are:

	DD_PATH for setting custom dd exexutable path. default is 'dd'

	XZCAT_PATH for setting custom xzcat executable path. default is 'xzcat'

	DOWNLOAD_PATH for setting custom downloads directory. default is '~/.dd-gui/downloads'
