import threading
import time

saldo = 5
sem = threading.Semaphore(0)
sem2 = threading.Semaphore(0)
def transferencia(monto):
    print ("Thread transf: starting")
    time.sleep(5)
    global saldo
    saldo = saldo + monto
    #pto encuentro
    sem2.acquire()
    sem.release()
    print ("saldo final", saldo)
    time.sleep(1)
    print ("hilo transf sigue trabajando")

def extrae(monto):
    print ("Thread extrae: starting")
    #dos segundos del hilo y 
    global saldo
    saldo = saldo - monto
    #pto encuentro
    sem2.release()
    sem.acquire()
    print ("saldo final", saldo )
    time.sleep(2)
    print ("hilo extrae sigue trabajando")


if __name__ == "__main__":
    x = threading.Thread(target=transferencia, args=(10000,))
    y = threading.Thread(target=extrae, args=(2000,))
    x.start()
    y.start()
    x.join()
    y.join()
    time.sleep(2)
    print (saldo)
    exit(0)
