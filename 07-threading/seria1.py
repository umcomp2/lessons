import threading
import time

saldo = 5

def transferencia(monto):
    print ("Thread transf: starting")
    global saldo
    time.sleep(0.1)
    saldo = saldo + monto
    print ("termino el hilo transferencia", saldo)

def extrae(monto):
    print ("Thread extrae: starting")
    #dos segundos del hilo y 
    global saldo
    while (saldo - monto) < 0:
        #print('.', end='')
        pass
    saldo = saldo - monto
    print ("termino el hilo extraccion", saldo )


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

