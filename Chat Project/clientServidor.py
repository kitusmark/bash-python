# -*- encoding: utf-8 -*-

class clientServidor: 
 
    def __init__(self,connexio, adreca):
      """ 
      Guarda els paràmetres de connexió i adreca que provenen de la
      creació del socket entre servidor i client. Inicialitza la
      identificació del client amb l'string '?', crea una
      cua buida de missatges que haurà de rebre i un string buit 
      dedicat a recollir les seves peticions.
      """
      self.nom = ''
      self.peticio = ''
      
    def fixaIdentitat(self, identitat):
      """
      Fixa la identitat del client. Arriba una taula amb les paraules
      """
      for paraula in identitat:
        self.nom = self.nom + paraula
 
    def afegeixMissatge(self, missatge):
      """
      Afegeix el missatge a la cua de missatges pendents de rebre.
      """
      pass

 
    def HiHaMissatges(self):
      """
      Indica si la cua de missatges en té. Retorna Boolea
      """
      pass
 
    def missatgePendent(self):
      """
      Retorna el primer missatge de la cua de missatges pendents de
      rebre. El missatge retornat es treu de la cua.
      """
      pass

    def connexio(self):
      """
      Retorna la connexió del client
      """
      return connexio
 
    def adreca(self):
      """
      Retorna l'adreça del client.
      """
      return adreca
 
    def identitat(self):
      """
      Retorna la identitat del client.
      """
      return self.identitat
 
    def construeixPeticio(self, c):
      """
      Afegeix el caràcter c a la petició en curs
      """
      
      self.peticio = self.peticio + c

    def peticio(self):
      """
      Retorna la petició actual i l'esborra.
      """
      return self.peticio