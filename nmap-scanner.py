'''
Purpose: Script that automates nmap scans on network.

Source: freeCodeCamp's Python for Pen Testing - Developing an Nmap Scanner (part 1)

Created: Jan 3, 2021
'''

#!/use/bin/python3
import nmap

scanner = nmap.PortScanner()

ip_addr = input("Enter the IP address or range to scan: ")
print("The IP address or range you entered is: ", ip_addr)

type(ip_addr)

response = input("""Which type of scan?
                    1. SYN ACK scan
                    2. UDP scan
                    3. Comprehensive scan
                    4. Exit""")

print("You have selected option: ", response)

if response == '1':
    print("nmap version: ", scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -sS')
    print(scanner.scaninfo())
    print("IP status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open ports: ", scanner[ip_addr]['tcp'].keys())
elif response == '2':
    print("nmap version: ", scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -sU')
    print(scanner.scaninfo())
    print("IP status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open ports: ", scanner[ip_addr]['udp'].keys())
elif response == '3':
    print("nmap version: ", scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -sS -sV -sC -A -O')
    print(scanner.scaninfo())
    print("IP status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open ports: ", scanner[ip_addr]['tcp'].keys())
else
    print("Please enter a valid option.")
