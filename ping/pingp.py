import sys, os, re, datetime, threading
 
t1 = datetime.datetime.now()

class Ping(threading.Thread):
    def __init__(self,  ip):
        threading.Thread.__init__(self)
        self.ip = ip
    def run(self):
        ping_out = os.popen("ping -q -c2 " + self.ip, "r")
        print(self.ip+": ... ", end="")
        for linia in ping_out:
            nRebuts = nombrePaquetsRebuts.findall(linia)
            if nRebuts!=[]:
                print(estat[int(nRebuts[0])])
 
if __name__ == "__main__":
    if len(sys.argv)!=4:
        sys.exit(os.EX_USAGE)
    prog, subxarxa, ini, fi=sys.argv

    

    t2 = datetime.datetime.now()
    print('Fet en ',t2 - t1)
