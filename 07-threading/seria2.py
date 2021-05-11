import threading
import time

saldo = 5

def transferencia(monto):
    print ("Thread transf: starting")
    global saldo
    time.sleep(3)
    saldo = saldo + monto
    print ("termino el hilo transferencia", saldo)

def extrae(monto):
    print ("Thread extrae: starting")
    #dos segundos del hilo y 
    global saldo
    x.join()
    saldo = saldo - monto
    print ("termino el hilo extraccion", saldo )


if __name__ == "__main__":
    x = threading.Thread(target=transferencia, args=(10000,))
    y = threading.Thread(target=extrae, args=(2000,))
    x.start()
    y.start()
    x.join()
    y.join()
    print (saldo)
    exit(0)

