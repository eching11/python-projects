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
