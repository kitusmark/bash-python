# -*- encoding: utf-8 -*-

import socket

class conversador:
 
    def __init__(self, identitat, adreca):
        """ 
    	El constructor de la classe
    	estableix la connexió amb el servidor que es troba a ladreca (si es el
    	mateix computador serà localhost) i en el port 50007. La comunicació
    	es fa amb el protocol internet (socket.AF_INET) i en mode
    	stream (socket.SOCK_STREAM). Un cop establerta la connexió,
    	envia al servidor la seva identificació, el segon paràmetre
    	del constructor. La comunicació serà bloquejant. 
        """
        HOST = adreca
        PORT = 50007


        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            s.connect((HOST, PORT))
            print 'Connectat amb exit!'
        except:
            print 'No es pot connectar al servidor'

        #Ara enviem la identitat del comunicador
        print '\\I ' + identitat + chr(3)
        s.send('\\I ' + identitat + chr(3))  #Caracter \I per començar la comunicacio
 
    def parla(self, miss):

        s.sendall(miss + chr(3))

    def escolta(self): 
    	"""
	Envia al servidor el missatge "\\M", acabat amb el caràcter
    	chr(3). Llavors, espera rebre un missatge del servidor que
    	(acabat amb el sentinella chr(3)). La funció retorna el
    	missatge rebut. Si el missatge que rep és "", vol dir que 
	no havia missatge pendent de rebre per part del servidor.
	"""
        s.send('\\M ' + chr(3))
        data = s.recv(1024)

        if data == '':
            print 'Cap missatge pendent'
        else:
            return data
        
    def tanca(self): 
    	"""
        Envia al client el missatge "\\F", acabat amb chr(3) i tanca el socket
        inicialitzat pel constructor de la classe.
    	"""
        s.send('\\F ' + chr(3)) #finalitzem la sessio
        s.close()
