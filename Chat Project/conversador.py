class Conversador:
 
    def __init__(self, identitat, adreca):
    	""" 
    	El constructor de la classe
    	estableix la connexió amb el servidor que es troba a l'adreça adreca (si és el
    	mateix computador serà localhost) i en el port 50007. La comunicació
    	es fa amb el protocol internet (socket.AF_INET) i en mode
    	stream (socket.SOCK_STREAM). Un cop establerta la connexió,
    	envia al servidor la seva identificació, el segon paràmetre
    	del constructor. La comunicació serà bloquejant. 
	"""
 
    def parla(self, miss):
        pass
    """
	Envia al servidor el missatge miss, acabat amb el caràcter chr(3).
    """
 
    def escolta(self): 
    	"""
	Envia al servidor el missatge "\\M", acabat amb el caràcter
    	chr(3). Llavors, espera rebre un missatge del servidor que
    	(acabat amb el sentinella chr(3)). La funció retorna el
    	missatge rebut. Si el missatge que rep és "", vol dir que 
	no havia missatge pendent de rebre per part del servidor.
	"""
 
    def tanca(self): 
    	"""
        Envia al client el missatge "\\F", acabat amb chr(3) i tanca el socket
        inicialitzat pel constructor de la classe.
    	"""