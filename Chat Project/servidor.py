# Echo server program
import socket
from multiprocessing import Process
from clientServidor import *
import sys


HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port

clientsActius = []		  #List of Active Clients in the server

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
	print 'New client Connected To the Server...'
	client = clientServidor(con, addr)
	while True:
		final = False
		while not final:
			c= ''
			try:
				c = con.recv(1)
			except socket.error:
				pass

			if c == chr(3):
				#Hem assolit el final del missatge
				final = True
				paraules = client.peticio.split()
				print paraules
				if paraules[0] == '\\I':
					#Missatge amb la identitat
					client.fixaIdentitat(paraules[1:len(paraules)])
				elif paraules[0] == '\\M':
					#Consulta de missatges
					if client.HiHaMissatges():
						client.missatgePendent()
					else:
						pass
				elif paraules[0] == '\\F':
					#Tanquem la conexio amb el client i lesborrem de la llista
					con.close()
				else:
					#Missatge que sha denviar a tots els clients
					pass
			else:
				client.construeixPeticio(c)

#Now we keep talking to the client
while 1:
	try:
		con, addr = s.accept()
		con.setblocking(0)
		clientsActius.append(con)
		print 'Connected with ' + addr[0] + ':' + str(addr[1])

		#We create a Process for every client connected and start it
		clientServidor = Process(target=servidor, args=(con,addr)).start()
	except Exception as e:
		pass

s.close()