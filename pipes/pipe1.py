import os, sys

def pare(com):
    str1 = com.split('"',0)
    os.execlp(str1)
    print("Filtre 1 ha fallat")
def fill(com):
    str2 = com.split('"',0)
    os.execlp(str2)
    print("Filtre 2 ha fallat")

if __name__ == "__main__":
    if len(sys.argv)!=3:
        print("Us: %s filtre1 filtre2" % sys.argv[0])
        sys.exit(os.EX_USAGE)
    prog, com1, com2 = sys.argv

    tub = os.pipe()
    idProces = os.fork()
    if idProces != 0:     #proces pare
        os.close(1)
        os.dup(tub[1])
        os.close(tub[0])
        os.close(tub[1])
        pare(com1)
    else:                 #proces fill
        os.close(0)
        os.dup(tub[0])
        os.close(tub[0])
        os.close(tub[1])
        fill(com2)
        
