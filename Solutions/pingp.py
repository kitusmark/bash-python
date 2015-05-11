import sys, os, re, datetime, threading

t1 = datetime.datetime.now()

class comprovaIP(threading.Thread):
   e = ("no respon","no funciona del tot","funciona")
   def __init__ (self,ip):
      threading.Thread.__init__(self)
      self.ip = ip
      self.pingsAssolits = -1
      self.paquetsRebuts = re.compile(r"(\d) received")
   def run(self):
       ping_out = os.popen("ping -q -c2 "+self.ip,"r")
#       print(self.ip+": ... ",end="")
       for linia in ping_out:
           nRebuts = self.paquetsRebuts.findall(linia)
           if nRebuts!=[]:
               self.pingsAssolits=int(nRebuts[0])
   def estat(self):
      return self.e[int(self.pingsAssolits)]

if __name__ == "__main__":
    if len(sys.argv)!=4:
        sys.exit(os.EX_USAGE)
    prog, subxarxa, ini, fi=sys.argv
    fils=[comprovaIP(subxarxa+'.'+str(sfx)) for sfx in range(int(ini),int(fi))]
    for fil in fils:
        fil.start()
    for fil in fils:
        fil.join()
        print(fil.ip,": ", fil.estat())
    t2 = datetime.datetime.now()
    print('Fet en ',t2 - t1)
