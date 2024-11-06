Python Port Scanner

A simple, multi-threaded port scanner built in Python, designed to scan a specified range of ports on a target IP or hostname. This tool identifies open ports, generates helpful nmap and rustscan commands for further inspection, and allows saving results to a file.

Features
Fast Scanning: Multi-threaded scanning for high speed and efficiency.
Configurable Settings: Define port ranges, thread count, and output files.
Command Generation: Generates nmap and rustscan commands for open ports.
Save Results: Option to save results with a timestamp.

 Usage
python port_scanner.py <target> [options]

Arguments
<target>: Target IP or hostname to scan.
-s, --start-port: Starting port for scanning (default: 1).
-e, --end-port: Ending port for scanning (default: 65535).
-t, --threads: Number of threads for concurrent scanning (default: 100).
-o, --output: File to save scan results.


python port_scanner.py 192.168.1.1

python port_scanner.py 192.168.1.1 -s 20 -e 1024

python port_scanner.py 192.168.1.1 -t 200

python port_scanner.py 192.168.1.1 -o results.txt


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
