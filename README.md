# Denial

**Denial** is a demonstration tool simulating a simple Denial of Service (DoS) attack. It sends a large number of requests to a specified host to overload its resources and simulate unavailability.

> **Warning:** This tool is for educational purposes only. Do not use it in any way that violates laws or ethical guidelines.

## Features

- **Random IP Generation**: Simulates attacks from various IP addresses.
- **Server Monitoring**: Continuously checks if the target server is reachable.
- **Multithreading**: Uses 1000 parallel threads for the attack.
- **Customizable Options**: Allows setting the target, port, and an optional fake IP.

## Requirements

- Python 3.x
- Built-in Python libraries: `socket`, `threading`, `time`, `random`

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/HasuTapeKg/denial.git

    Navigate to the project directory:

    cd denial

Usage

    Run the script:

    python Denial.py

    Enter the required inputs:
        Target: IP address of the target server (e.g., 192.168.1.1).
        Port: Port number to attack (e.g., 80 for HTTP).
        Fake IP: Optional IP address for requests (leave blank to generate random IPs).

    To stop the attack, press Ctrl + C.

Example

What is your target (ex. 192.168.1.1)> 192.168.0.1
On which port of 192.168.0.1 to attack (ex. 80 for HTTP)> 80
Which IP do you want to use in the attack (leave blank for random)> 

Console output:

[INFO] 192.168.0.1:80 is still reachable.
[ALERT] 192.168.0.1:80 seems down!

Disclaimer

This tool is provided "as-is" and is currently in beta. The author, HasuTapeKg, takes no responsibility for any damage, loss, or misuse caused by this tool. Use it at your own risk and only for educational purposes.
Author

Created by HasuTapeKg. The tool is shared to help others learn and experiment.
Warning

Denial is intended solely for educational purposes. Unauthorized use of this tool in illegal or unethical activities is strictly prohibited.
