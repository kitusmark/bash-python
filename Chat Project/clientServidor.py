class ClientServidor: 
 
    def __init__(self,connexio, adreca):
      """ 
      Guarda els paràmetres de connexió i adreca que provenen de la
      creació del socket entre servidor i client. Inicialitza la
      identificació del client amb l'string '?', crea una
      cua buida de missatges que haurà de rebre i un string buit 
      dedicat a recollir les seves peticions.
      """
 
    def fixaIdentitat(self, identitat):
      """
      Fixa la identitat del client
      """
 
    def afegeixMissatge(self, missatge):
      """
      Afegeix el missatge a la cua de missatges pendents de rebre.
      """
 
    def HiHaMissatges(self):
      """
      Indica si la cua de missatges en té.
      """
 
    def missatgePendent(self):
      """
      Retorna el primer missatge de la cua de missatges pendents de
      rebre. El missatge retornat es treu de la cua.
      """
 
    def connexio(self):
      """
      Retorna la connexió del client
      """
 
    def adreca(self):
      """
      Retorna l'adreça del client.
      """
 
    def identitat(self):
      """
      Retorna la identitat del client.
      """
 
    def construeixPeticio(self, c):
      """
      Afegeix el caràcter c a la petició en curs
      """
 
    def peticio(self):
      """
      Retorna la petició actual i l'esborra.
      """
