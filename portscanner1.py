#!/bin/python

import sys
import socket
from datetime import datetime

def scan_ports(target):
    try:
        for port in range(1, 65365):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            result = s.connect_ex((target, port))
            if result == 0:
                print(f"Port {port} is open")
            s.close()

    except KeyboardInterrupt:
        print("\nExiting program")
        sys.exit()

    except socket.gaierror:
        print("Hostname could not be resolved")
        sys.exit()

    except socket.error:
        print("Couldn't connect to the server")
        sys.exit()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Invalid number of arguments")
        print("Syntax: python port_scanner.py <hostname or IP>")
        sys.exit()

    target = socket.gethostbyname(sys.argv[1])
    print("-" * 50)
    print(f"Scanning started for :{target}")
    print(f"Time started: {datetime.now()}")
    print("-" * 50)

    scan_ports(target)
