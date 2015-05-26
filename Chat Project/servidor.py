# Echo server program
import socket
from multiprocessing import Process
from clientServidor import *
import sys


HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port


if __name__ == '__main__':
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

#Now we keep talking to the client
	while 1:
		try:
			con, addr = s.accept()
			con.setblocking(0)
			print 'New client Connected To the Server...'
			clientConnectat = clientServidor(con, addr)
			clientsActius.append(con)
			print 'Connected with ' + addr[0] + ':' + str(addr[1])
		except Exception as e:
			pass

		for client in clientsActius:
			final = False
			while not final:
				c = ''
				try:
					c = client.recv(1)
				except socket.error:
					pass

				if c == chr(3):
					#Hem assolit el final del missatge
					final = True
					paraules = clientConnectat.peticio.split()
					print paraules
					if paraules[0] == '\\I':
						#Missatge amb la identitat
						clientConnectat.fixaIdentitat(paraules[1:len(paraules)])
					elif paraules[0] == '\\M':
						#Consulta de missatges
						if clientConnectat.HiHaMissatges():
							client.send(clientConnectat.missatgePendent())
						else:
							client.send('')
					elif paraules[0] == '\\F':
						#Tanquem la conexio amb el client i lesborrem de la llista
						client.close()
						if len(clientConnectat.cuaMissatges) > 0:
							s.close()
					else:
						#Missatge que sha denviar a tots els clients
						for client in clientsActius:
							clientConnectat.afegeixMissatge(paraules[1:len(paraules)])
				else:
					clientConnectat.construeixPeticio(c)
