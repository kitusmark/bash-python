# Echo client program
import socket
from conversador import *

adreca = 'localhost'
identitat = raw_input('Indica el teu nom: ')

client = conversador(identitat, adreca)

while True:
	message = raw_input('Your message: ')
	s.send(message)

	print 'Waiting the response...'

	reply = s.recv(1024)

	print 'Recieved data', repr(reply)

s.close()
