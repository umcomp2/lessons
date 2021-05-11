import threading
import time

saldo = 5
mutex = threading.Lock()
def transferencia(monto):
    print ("Thread transf: starting")
    global saldo
    for i in range(monto):
        mutex.acquire()
        saldo = saldo + 1
        mutex.release()
    print ("termino el hilo transferencia", saldo)

def extrae(monto):
    print ("Thread extrae: starting")
    #dos segundos del hilo y 
    global saldo
    for i in range(monto):
        mutex.acquire()
        saldo = saldo - 1
        mutex.release()
    print ("termino el hilo extraccion", saldo )


if __name__ == "__main__":
    x = threading.Thread(target=transferencia, args=(100000,))
    y = threading.Thread(target=extrae, args=(100000,))
    x.start()
    y.start()
    x.join()
    y.join()
#    transferencia(100000)
#    extrae(100000)
    print ("el valor final del final ", saldo)
    exit(0)
