import sys, os, re, datetime
 
t1 = datetime.datetime.now()
 
if __name__ == "__main__":
    if len(sys.argv)!=4:
        sys.exit(os.EX_USAGE)
    prog, subxarxa, ini, fi=sys.argv
    nombrePaquetsRebuts = re.compile(r"(\d) received")
    estat = ("no respon","no funciona del tot","funciona")
    for sufix in range(int(ini),int(fi)):
        ip = subxarxa+"."+str(sufix)
        ping_out = os.popen("ping -q -c2 "+ip,"r")
        print(ip+": ... ",end="")
        for linia in ping_out:
            nRebuts = nombrePaquetsRebuts.findall(linia)
            if nRebuts!=[]:
                print(estat[int(nRebuts[0])])
    t2 = datetime.datetime.now()
    print('Fet en ',t2 - t1)
