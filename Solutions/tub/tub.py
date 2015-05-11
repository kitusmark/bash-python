import os
import sys

entradaStd=sys.stdin.fileno() 
sortidaStd=sys.stdout.fileno()

idxSortidaTub=0 
idxEntradaTub=1 


def tub():
   if len(sys.argv) != 3:
       print( "Us: %s filtre1 filtre2" % sys.argv[0] )
       sys.exit(os.EX_USAGE)
   tub=os.pipe()
   idProces=os.fork()
   if idProces == 0:
      os.close(sortidaStd); os.dup(tub[idxEntradaTub])
      os.close(tub[idxSortidaTub]); os.close(tub[idxEntradaTub])
      fargv = sys.argv[1].split();  os.execv( fargv[0], fargv);
      sys.stderr.write("filtre 1 ha fallat\n")
   else:
      os.close(entradaStd); os.dup(tub[idxSortidaTub])
      os.close(tub[idxSortidaTub]); os.close(tub[idxEntradaTub])
      fargv = sys.argv[2].split();  os.execv( fargv[0], fargv)
      sys.stderr.write("filtre 2 ha fallat\n")
       
if __name__ == "__main__":
    tub()
