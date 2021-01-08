#!/usr/bin/python3

import socket

def banner():
    socket = socket.socket()
    socket.connect((ip, int(port)))
    print(socket.recv(1024))

def main():
    ip = input("Please enter IP address: ")
    port = input("Please enter the port: ")
    banner()

main()
