#!/bin/python

import sys
import socket
from datetime import datetime
import argparse
import concurrent.futures

def scan_port(target, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)  # Adjustable timeout
        result = s.connect_ex((target, port))
        s.close()
        if result == 0:
            print(f"Port {port} is open")
            return port
    except socket.error as e:
        print(f"Error scanning port {port}: {e}")
    return None

def scan_ports(target, start_port, end_port, threads):
    open_ports = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        futures = [executor.submit(scan_port, target, port) for port in range(start_port, end_port + 1)]
        for future in concurrent.futures.as_completed(futures):
            port = future.result()
            if port:
                open_ports.append(port)
    return open_ports

def generate_commands(target, open_ports):
    port_list = ','.join(map(str, open_ports))
    print("\nOpen ports found:")
    print(port_list if open_ports else "No open ports found.")

    if open_ports:
        print("\nGenerated commands:")
        print(f"Nmap version scan: nmap -sV -p {port_list} {target}")
        print(f"Nmap service detection: nmap -sV --version-intensity 5 -p {port_list} {target}")
        print(f"Nmap script scan: nmap -sC -p {port_list} {target}")
        print(f"Rustscan with Nmap integration: rustscan -p {port_list} --scripts <scripts> {target}")
        print(f"Nmap service and OS detection: nmap -sV -O -p {port_list} {target}")
        print(f"Nmap aggressive scan: nmap -A -p {port_list} {target}")

def save_results(filename, target, open_ports):
    with open(filename, 'w') as f:
        f.write(f"Scan results for {target}\n")
        f.write(f"Timestamp: {datetime.now()}\n")
        f.write("\nOpen ports:\n")
        for port in open_ports:
            f.write(f"{port}\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Port Scanner")
    parser.add_argument("target", help="Target IP or hostname to scan")
    parser.add_argument("-s", "--start-port", type=int, default=1, help="Starting port (default: 1)")
    parser.add_argument("-e", "--end-port", type=int, default=65535, help="Ending port (default: 65535)")
    parser.add_argument("-t", "--threads", type=int, default=100, help="Number of threads (default: 100)")
    parser.add_argument("-o", "--output", help="Save scan results to a file")
    args = parser.parse_args()

    # Validate port range
    if not (1 <= args.start_port <= 65535 and 1 <= args.end_port <= 65535):
        print("Please enter valid port numbers between 1 and 65535.")
        sys.exit(1)

    target = socket.gethostbyname(args.target)
    print("-" * 50)
    print(f"Scanning started for: {target}")
    print(f"Time started: {datetime.now()}")
    print("-" * 50)

    open_ports = scan_ports(target, args.start_port, args.end_port, args.threads)
    generate_commands(target, open_ports)

    if args.output:
        save_results(args.output, target, open_ports)
        print(f"\nScan results saved to {args.output}")
