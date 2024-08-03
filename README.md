# Python Port Scanner

## Overview
This is a simple port scanner written in Python using the `socket` and `asyncio` libraries. The scanner takes an IP address as input and scans for open ports on the target machine. This is an update from my last IP pen tester on the Hacker OS website. 

## How it Works
The scanner follows these steps to scan for open ports:
1. **Input Validation**: The user is prompted to enter an IP address, which is validated using the `ipaddress` library to ensure it is a valid IP address.
2. **Port Scanning**: The scanner uses a thread pool executor to scan for open ports on the target machine. The `scan_port` function is called for each port in the range of 1 to 100 (by default), you can change this number to your pleasing but it may take longer, I made this keeping processing speed in mind. 
3. **Socket Connection**: The `scan_port` function creates a socket object and attempts to connect to the target machine on the specified port. If the connection is successful, the port is considered open.
4. **Result Printing**: The results of the port scan are printed to the console, indicating which ports are open.

## Code Structure
The code is structured into the following functions:
- **`main` function**: This is the entry point of the program, responsible for prompting the user for input and calling the `scan_ports` function.
- **`scan_ports` function**: This function scans for open ports on the target machine. It uses a thread pool executor to call the `scan_port` function for each port in the specified range.
- **`scan_port` function**: This function scans a single port on the target machine. It creates a socket object and attempts to connect to the target machine on the specified port.

## Technical Details
- **Socket Library**: The `socket` library is used to create socket objects and attempt connections to the target machine.
- **Asyncio Library**: The `asyncio` library is used to create a thread pool executor and run the `scan_port` function concurrently for each port in the range.
- **ThreadPoolExecutor**: A thread pool executor is used to run the `scan_port` function concurrently for each port in the range. This allows the scanner to scan multiple ports simultaneously, improving performance.

## Development Process
The code was developed using the following steps:
1. **Initial Research**: Research was conducted to determine the best approach for building a port scanner in Python.
2. **Code Writing**: The code was written using the `socket` and `asyncio` libraries.
3. **Testing**: The code was tested to ensure that it worked correctly and produced the expected results.
4. **Refactoring**: The code was refactored to improve performance and readability.

## Future Development
Future development plans include:
- **Improving Performance**: Improving the performance of the scanner by using more efficient algorithms and data structures.
- **Adding Features**: Adding additional features to the scanner, such as the ability to scan for specific services or protocols.
- **Error Handling**: Improving error handling to make the scanner more robust and reliable.

## Usage
To use the port scanner, simply run the script and enter the IP address you want to scan when prompted:
```bash
python port_scanner.py

Example
Here's an example of how to use the port scanner:

Enter the IP address to scan: 192.168.1.1
Starting port scan on 192.168.1.1...
Port 22 is open
Port 80 is open
Port scan complete!

License
This project is licensed under the Apache License. See the LICENSE file for more details.

Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue to suggest improvements or report bugs.

