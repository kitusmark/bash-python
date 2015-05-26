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
      self.con = connexio
      self.addr = adreca

      self.cuaMissatges = []
      self.nom = '?'
      self.peticio = ''
      
    def fixaIdentitat(self, identitat):
      """
      Fixa la identitat del client. Arriba una taula amb les paraules
      """
      self.nom = ''
      for paraula in identitat:
        self.nom = self.nom + paraula
 
    def afegeixMissatge(self, missatge):
      """
      Afegeix el missatge a la cua de missatges pendents de rebre.
      Rebem el missatge com una llista de paraules
      """
      text = ''
      for paraula in missatge:
        text = text + paraula 
      
      self.cuaMissatges.append(text)

 
    def HiHaMissatges(self):
      """
      Indica si la cua de missatges en té. Retorna Boolea
      """
      return len(self.cuaMissatges) > 0
 
    def missatgePendent(self):
      """
      Retorna el primer missatge de la cua de missatges pendents de
      rebre. El missatge retornat es treu de la cua.
      """
      return self.nom + 'diu: ' + self.cuaMissatges.pop(1) + chr(3)

    def connexio(self):
      """
      Retorna la connexió del client
      """
      return self.con
 
    def adreca(self):
      """
      Retorna l'adreça del client.
      """
      return self.addr
 
    def identitat(self):
      """
      Retorna la identitat del client.
      """
      return self.nom
 
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
      self.peticio = ''