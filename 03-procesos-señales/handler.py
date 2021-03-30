import os
import time
import signal

def manejador(nro,frame):
    print ("llego la señal", nro)
    print("esta seguro que quiere terminar el programa?")
    signal.signal(signal.SIGINT,signal.SIG_DFL)

#signal.signal(signal.SIGKILL,signal.SIG_IGN)
#signal.signal(signal.SIGSTOP,signal.SIG_IGN)
signal.signal(signal.SIGINT,manejador)
print ("soy el padre", os.getpid(), os.getppid())

pid = os.fork()

if pid > 0:
    #os.wait()
    time.sleep(30)
    print ("soy el padre")

else:
    print ("soy el hijo")
