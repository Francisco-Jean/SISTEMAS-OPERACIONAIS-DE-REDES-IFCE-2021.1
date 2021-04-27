# server.py
import socket
import time
# create a socket objectne name
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# get local machi
host = socket.gethostname()
port = 9999
# bind to the port
serversocket.bind((host, port))
# starts listening requests
serversocket.listen()
while True:
# establish a connection
    clientsocket,addr = serversocket.accept()
    print("Got a connection from %s" % str(addr))
    currentTime = time.ctime(time.time()) + "\r\n"
    clientsocket.send(currentTime.encode('ascii'))
    clientsocket.close()