# Daniel Wolosiuk
# Cyber Defense Techniques 2025 Red Team Tool
# Oct 18, 2025
# dw4102@rit.edu

import subprocess
import time
import sys
import os

def start_tmux_listeners():
    """Create a tmux sessions with a netcat listener for every port 
    """
    for team_number in range(1, 4): # Iterate through every team
        for port in range(team_number * 10000, (team_number * 10000) + 255): # 255 for every sent port
            session_name = "c2_t" + str(team_number) + "_p" + str(port)
            cmd = f"tmux new-session -d -s '{session_name}' 'nc -nvlp {port}'"
            subprocess.run(cmd, shell=True, check=True, capture_output=True)


def main():
    start_tmux_listeners()

if __name__ == "__main__":
    main()