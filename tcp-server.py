'''
Purpose: tcp-server.py creates a server socket and sends a message after client successfully connects.

Source: freeCodeCamp's Python for Pen Testing - Understanding Sockets and Creating a TCP Server

Created: Jan 3, 2021
'''
#!/use/bin/python3
import socket

# create server socket object
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostbyname()
port = 777

# binds host and port to socket
socket.bind((host, port))

# set up TCP listener to allow 2 simultaneous connections
socket.listen(2)

while True:
    clientsocket, address = socket.accept() # accept info from clientsocket
    print("Received connection from " + str(address))

    # send message to client
    message = 'Success! You\'ve connected to the server' + "\r\n"
    clientsocket.send(message.encode('ascii'))

    # close clientsocket
    clientsocket.close()
