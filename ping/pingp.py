import sys, os, re, datetime, threading
 
class Ping(threading.Thread):
    nRebuts=[]
    def __init__(self,  ip):
        threading.Thread.__init__(self)
        self.ip = ip
    def run(self):
        ping_out = os.popen("ping -q -c2 " + self.ip, "r")
        for linia in ping_out:
            self.nRebuts = nombrePaquetsRebuts.findall(linia)
 
if __name__ == "__main__":
    t1 = datetime.datetime.now()
    if len(sys.argv)!=4:
        sys.exit(os.EX_USAGE)
    prog, subxarxa, ini, fi=sys.argv
    nombrePaquetsRebuts = re.compile(r"(\d) received")
    estat = ("no respon","no funciona del tot","funciona")
    for sufix in range(int(ini),int(fi)):
        ip = subxarxa+"."+str(sufix)
        p = Ping(ip)
        p.start()
        p.join()
        print(ip+": ... ",end="")
        if p.nRebuts!=[]:
            print(estat[int(p.nRebuts[0])])

    t2 = datetime.datetime.now()
    print('Fet en ',t2 - t1)
