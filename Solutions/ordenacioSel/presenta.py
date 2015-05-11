#!/usr/bin/env python3
from entsort import llegirEnter, escriureEnterEspai


sentinella=-1

def presenta():
    n=llegirEnter()
    if n!=sentinella:
        minim=True;
        Min=n
        n=llegirEnter()
        while n!=sentinella:
            if n<Min:
                Min=n
            else: # n>=Min:
                pass
            n=llegirEnter()
    else: # n==sentinella
        minim=False
    #
    # Segona fase esperem que processos precedents enviin els seus resultats
    # abans que el meu resultat
    #
    n=llegirEnter()
    while n!=sentinella:
        escriureEnterEspai(n)
        n=llegirEnter()
    if minim:
        escriureEnterEspai(Min)

if __name__ == "__main__":
    presenta()
