import os
import time
import signal

def handler(nro,frame):
    print ("no se puede escribir en un pipe que tiene todas los descriptores de lectura cerrados")
    exit()
    
signal.signal(signal.SIGPIPE,handler)
fdl,fde = os.pipe()

pid = os.fork()

if pid == 0:
    os.close(fde)
    os.close(fdl)
    time.sleep(10)
    exit()
os.close(fdl)
while True:
    leido = os.read(0,1024)
    if len(leido) == 0:
    #if leido == b'':
        break
    os.write(fde,leido)

