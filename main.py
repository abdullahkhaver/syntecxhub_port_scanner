import socket
import threading
import logging
from datetime import datetime

# Configuration Sections
TIMEOUT = 1
LOG_FILE = "scan_results.log"

logging.basicConfig(
	filename=LOG_FILE,
	level=logging.INFO,
	format="%(asctime)s - %(message)s"
)

print_lock = threading.Lock()

def scan_port(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(TIMEOUT)
        result = sock.connect_ex((host, port))
        sock.close()

        with print_lock:
            if result == 0:
                print(f"[+] Port {port} OPEN")
                logging.info(f"Port {port} OPEN")
            else:
                print(f"[-] Port {port} CLOSED")
                logging.info(f"Port {port} CLOSED")

    except socket.timeout:
        with print_lock:
            print(f"[!] Port {port} TIMEOUT")
            logging.info(f"Port {port} TIMEOUT")

    except Exception as e:
        with print_lock:
            print(f"[ERROR] Port {port}: {e}")
            logging.error(f"Port {port}: {e}")

def main():
    host = input("Enter target host (e.g. 127.0.0.1): ")
    start_port = int(input("Start port: "))
    end_port = int(input("End port: "))

    print("\nStarting scan...")
    print(f"Target: {host}")
    print(f"Ports: {start_port}-{end_port}")
    print("-" * 40)

    start_time = datetime.now()

    threads = []

    for port in range(start_port, end_port + 1):
        t = threading.Thread(target=scan_port, args=(host, port))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    end_time = datetime.now()
    print("-" * 40)
    print(f"Scan completed in {end_time - start_time}")

if __name__ == "__main__":
    main()
