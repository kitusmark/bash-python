import sys, os


def separador(c):
    return c in " \t\n"

def xifra(c):
    return c in "0123456789"

def llegirCaracter():
    return str(os.read(0,1),'utf-8')

def escriureCaracter(c):
    return os.write(1,bytes(c,'utf-8'))

def llegirEnter():
    c=llegirCaracter()
    while separador(c):
        c=llegirCaracter()
    e=0
    if c=='-':
        signe=-1
        c=llegirCaracter()
    elif c=='+':
        signe=1
        c=llegirCaracter()
    else:
        signe=1
    while xifra(c):
       e=e*10+int(c)
       c=llegirCaracter()
    return e*signe


def escriureEnterEspai(e):
    for c in str(e):
        escriureCaracter(c)
    escriureCaracter(' ')
    
