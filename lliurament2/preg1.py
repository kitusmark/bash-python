import os, threading, sys

class cercaFitxer(threading.Thread):

    def __init__ (self,directori, fitxer):
        threading.Thread.__init__(self)
        self.llistadir = []
    def run(self):
        llistadir = os.popen('find' + directori + '-name' + fitxer, 'r').readlines()
        




if __name__ == "__main__":
    if len(sys.argv)!=3:
        sys.exit(os.EX_USAGE)
    i = 0
    prog, dir, fitxers = sys.argv
    fils = [cercaFitxer(dir,fitx) for fitx in range(len(sys.argv)-3)]
    for fil in fils:
        fil.start()
    for fil in fils:
        fil.join()
        print(fitxer[i] + ': '),        ##Aqui hem d imprimir cada fitxers amb els seus directoris corresponents
        print(cercaFitxer.llistadir)
        i = i + 1
        
    print('Tasca Finalitzada!)
