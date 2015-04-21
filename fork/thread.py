import time
import threading

def filProva(i,s):
    print("Esperant %d segons des del fil %d" % (s,i))
    time.sleep(s)
    print("fi fil %d" % (i))

for i in range(10):
    t = threading.Thread(target=filProva, args=(i,15))
    t.start()


print("Aixo es tot!!!!!!")
