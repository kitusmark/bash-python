import os

def fill():
    print('Hola soc el fill', os.getpid())
    os._exit(0)

def pare():
    for i in range(4):
        noupid = os.fork()
        if noupid == 0:
            fill()
        else:
            pids = (os.getpid(), noupid)
            print("pare: %d, fill: %d" %pids)

if __name__ == "__main__":
    pare()
