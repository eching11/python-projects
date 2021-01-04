'''
Purpose: tcp-client.py opens a connection to server and once successfully connected, client receives a message from the server.

Source: freeCodeCamp's Python for Pen Testing - Creating a TCP Client

Created: Jan 3, 2021
'''
#!/use/bin/python3
import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 777

clientsocket.connect((host, port))
message = clientsocket.recv(1024) $ set max amount of data to be transmitted

clientsocket.close()

print(message.decode('ascii'))
