# Install

`apt install python3`

`pip3 install openpyxl`

`pip3 install pysftp`

`pip3 install xlrd`

# Run

`cd src`

`./main.py`

# Config

Edit src/Config.py

Download path, there must be bunch of free space
- 'download_path': 'path_to_working_dir',

Upload parameters - host address, username, password and path
- 'upload_addr': 'os.uploads.ing.enigma.com',
- 'upload_user': 'kkuloshvili',
- 'upload_pass': '',
- 'upload_path': 'uploads',

Remove or not csv files after they are used
- 'remove_temp': False,

