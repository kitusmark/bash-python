#!/usr/bin/env python3
from entsort import llegirEnter, escriureEnterEspai


sentinella=-1

def min():
    n=llegirEnter()
    if n!=sentinella:
        minim=True;
        Min=n
        n=llegirEnter()
        while n!=sentinella:
            if n<Min:
                escriureEnterEspai(Min) 
                Min=n
            else: # n>=Min:
                escriureEnterEspai(n)
            n=llegirEnter()
#            print(n)
    else: # n==sentinella
        minim=False
    escriureEnterEspai(sentinella);
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
    escriureEnterEspai(n) # escrivim sentinella

if __name__ == "__main__":
    min()
