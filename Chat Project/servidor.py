# Echo server program
import socket
from multiprocessing import Process
import sys


HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket Created'

#Bind socket to local host and port
try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
     
print 'Socket bind complete'

s.listen(5)
print 'Socket now listening'


def servidor(con, addr):
	print 'New client Connected To the Server... Hello!'
	#client = clientServidor(con, addr)

#Now we keep talking to the client
while 1:
	con, addr = s.accept()
	print 'Connected with ' + addr[0] + ':' + str(addr[1])

	#We create a Process for every client connected
	client = Process(target=servidor, args=(con,addr))
	client.start()

