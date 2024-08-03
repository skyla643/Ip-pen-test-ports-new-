import socket
import ipaddress
import asyncio
import concurrent.futures

def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Set timeout to 1 second
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"Port {port} is open")
        sock.close()
    except socket.error as e:
        print(f"Socket error: {e}")
    except TimeoutError:
        print("Timeout error")

async def scan_ports(ip, start_port=1, end_port=100):
    loop = asyncio.get_running_loop()
    tasks = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        for port in range(start_port, end_port + 1):
            task = loop.run_in_executor(executor, scan_port, ip, port)
            tasks.append(task)

        await asyncio.gather(*tasks)

def main():
    ip = input("Enter the IP address to scan: ")

    try:
        ipaddress.ip_address(ip)
    except ValueError:
        print("Invalid IP address")
        return

    print(f"Starting port scan on {ip}...")
    asyncio.run(scan_ports(ip))
    print("Port scan complete!")

if __name__ == "__main__":
    main()