Port Scanner
A simple, multi-threaded port scanner written in Python. This tool scans a specified range of ports on a target IP or hostname, identifies open ports, and generates useful commands for further analysis with nmap and rustscan. You can also save the results to a file.

Features
Fast scanning using multi-threading
Supports configurable port ranges and thread count
Generates commonly used nmap and rustscan commands for open ports
Saves scan results with timestamps
Requirements
Python 3.x
Usage
Clone or download this repository.
Open a terminal and navigate to the project folder.
Run the port scanner with the following syntax:
bash
Copy code
python port_scanner.py <target> [options]
Arguments
<target>: Target IP or hostname to scan.
-s, --start-port: Starting port for scanning (default: 1).
-e, --end-port: Ending port for scanning (default: 65535).
-t, --threads: Number of threads for concurrent scanning (default: 100).
-o, --output: Output file to save scan results.
Example Commands
Basic Scan on Default Range (1-65535)

bash
Copy code
python port_scanner.py 192.168.1.1
Scan Specific Port Range (e.g., 20 to 1024)

bash
Copy code
python port_scanner.py 192.168.1.1 -s 20 -e 1024
Use 200 Threads for Faster Scanning

bash
Copy code
python port_scanner.py 192.168.1.1 -t 200
Save Scan Results to a File

bash
Copy code
python port_scanner.py 192.168.1.1 -o results.txt
Demo
Here’s an example output of a scan on 127.0.0.1 for ports 80-90 using 50 threads:

bash
Copy code
--------------------------------------------------
Scanning started for: 127.0.0.1
Time started: 2024-11-05 12:34:56
--------------------------------------------------

Port 80 is open
Port 88 is open

Open ports found:
80,88

Generated commands:
Nmap version scan: nmap -sV -p 80,88 127.0.0.1
Nmap service detection: nmap -sV --version-intensity 5 -p 80,88 127.0.0.1
Nmap script scan: nmap -sC -p 80,88 127.0.0.1
Rustscan with Nmap integration: rustscan -p 80,88 --scripts <scripts> 127.0.0.1
Nmap service and OS detection: nmap -sV -O -p 80,88 127.0.0.1
Nmap aggressive scan: nmap -A -p 80,88 127.0.0.1

Scan results saved to results.txt
