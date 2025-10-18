# CDT 2025 Red Team tool
## Bad ls

Note: build executable on debian bookworm instance

Install libpython3.11
```bash
apt install libpython3.11
```

In the venv, install requirements
```bash
pip install -r requirements.txt
```

Build python script into linux binary
```bash
./convert_to_linux_binary.sh
```

## Starting listener
Port number is subject to change
```bash
nc -nvlp 4444
```

## Upgrading reverse shell to fully interactive tty
Execute this after recieving a netcat connection
Useful for being able to use sudo, etc. 
```bash
python3 -c 'import pty; pty.spawn("/bin/bash")'
```

# TODO
Make "all-in-one" deploy script that will build and then deploy to box
Make reverse shell connect to every red team host instead of just one host

> Author: Daniel Wolosiuk

Oct 17, 2025

