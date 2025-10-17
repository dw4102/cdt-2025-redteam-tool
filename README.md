# CDT 2025 Red Team tool

Install pyenv and target machine python version
```bash
apt install pyenv
pyenv install 3.8.19
pyenv local 3.8.19
~/.pyenv/versions/3.8.19/bin/python -m venv .venv
source .venv/bin/activate
```

In the venv, install requirements
```bash
pip install -r requirements.txt
```

Build python script into linux binary
```bash
./convert_to_linux_binary.sh
```

> Author: Daniel Wolosiuk

Oct 17, 2025

