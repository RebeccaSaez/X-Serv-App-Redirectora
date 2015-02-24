#!/usr/bin/python

"""
Infinite HTTP Server
"""

import socket
import random

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
mySocket.bind((socket.gethostname(), 1234))
mySocket.listen(5)

try:
    while True:
        print 'Waiting for connections...'
        (recvSocket, address) = mySocket.accept()
        print 'Request received:'
        print recvSocket.recv(2048)
        print 'Answering back...'
        recvSocket.send("HTTP/1.1 301 Moved Permanently\nLocation: http://" +
                        socket.gethostname() + ":1234/" +
                        str(random.randrange(1000000)) + "\r\n\r\n" +
                        "<html>" +
                        "<body><h1>Te aburres ya?</h1>" +
                        "<BODY BGCOLOR='#F5A9F2'>" +
                        "</body></html>" +
                        "\r\n")
        recvSocket.close()

except KeyboardInterrupt:
    print "Closing binded socket"
    mySocket.close()
