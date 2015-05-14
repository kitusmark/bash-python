import os, sys

def creaFilConnectat(sorAnt, executable):
    sor, ent=os.pipe() # crea un pipe a la banda dreta */
    idProces = os.fork()
    if idProces != 0: # pare
        os.close(ent)
        os.close(sorAnt)
    else:
        #                                  procés
        #        +-----+                   +-----+
        #  in -->|ant. |-->sorAnt       +->| fill|--+
        #        +-----+                |  +-----+  |
        #                               |           |
        #                               |  +-+-+    |
        #                           sor +--|0|1|<---+ ent
        #                                  +-+-+pipe
        #>>>>>>> COMPLETEU AQUÍ CODI PER FER LES CONNEXIONS PREVISTES
   #                                  procés
   #        +-----+                   +-----+
   #  in -->|ant. |------------------>| fill|--+ stdout
   #        +-----+sorAnt      stdin  +-----+  |
   #                                           |
   #                                  +-+-+    |
   #                             sor--|0|1|<---+
   #                                  +-+-+pipe
        os.close(sorAnt)    # Donem de baixa les posicions 4a i 5a
                               # de la taula E/S
        os.close(ent)
  # encavalcament amb el programa 'executable'
  #>>entSTD=sys.stdin.fileno()
>>>>>> COMPLETEU AQUÍ CODI PER FER QUE AQUEST PROCÉS
  #>>>>>>>> SIGUI EL PROGRAMA QUE HA D'EXECUTAR-SE
        os.exit(0)
    return(sor)

def canonada(nProc,nomp,nompf):

    entSTD=sys.stdin.fileno()
    sorSTD=sys.stdout.fileno()

    sorp,entp=os.pipe()     # Creació dels processos amb
    for i in range(nProc-1):# els seus pipes connectats.
        sorp=creaFilConnectat(sorp, nomp)

    sorp=creaFilConnectat(sorp, nompf)
    c= os.read(entSTD,1)   #El que arriba del canal
    while len(c)!=0:       #estàndard d'entrada  ho
        os.write(entp, c)  #passem a la canonada.
        c= os.read(entSTD,1)

    c = os.read(sorp,1)    #Recollim el que en ens arriba del
    while len(c)!=0:       #final de la canonada i ho  passem
        os.write(sorSTD,c) #al canal estàndard de sortida.
        c = os.read(sorp,1)
    os.write(sorSTD,bytes('\n','UTF-8'))
    return os.EX_OK




if  __name__ == "__main__":
