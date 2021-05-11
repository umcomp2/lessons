import threading
import time

saldo = 5
t_wait_e = threading.Semaphore(0)
t_wait_h = threading.Semaphore(0)
e_wait_t = threading.Semaphore(0)
e_wait_h = threading.Semaphore(0)
h_wait_e = threading.Semaphore(0)
h_wait_t = threading.Semaphore(0)

def transferencia(monto):
    print ("Thread transf: starting")
    global saldo
#    time.sleep(5)
    saldo = saldo + monto
    #pto encuentro
    h_wait_t.release()
    e_wait_t.release()
    t_wait_e.acquire()
    t_wait_h.acquire()
    print ("saldo final", saldo)
    time.sleep(1)
    print ("hilo transf sigue trabajando")

def extrae(monto):
    print ("Thread extrae: starting")
    #dos segundos del hilo y 
    global saldo
    saldo = saldo - monto
    #pto encuentro
    t_wait_e.release()
    h_wait_e.release()
    e_wait_t.acquire()
    e_wait_h.acquire()
    print ("saldo final", saldo )
    time.sleep(2)
    print ("hilo extrae sigue trabajando")


def hb(monto):
    print ("Thread hb: starting")
    #dos segundos del hilo y 
    time.sleep(2)
    global saldo
    saldo = saldo - monto
    #pto encuentro
    t_wait_h.release()
    e_wait_h.release()
    h_wait_t.acquire()
    h_wait_e.acquire()
    print ("saldo final", saldo )
    time.sleep(2)
    print ("hilo extrae sigue trabajando")



if __name__ == "__main__":
    x = threading.Thread(target=transferencia, args=(10000,))
    y = threading.Thread(target=extrae, args=(2000,))
    z = threading.Thread(target=hb, args=(1500,))
    x.start()
    y.start()
    z.start()
    x.join()
    y.join()
    z.join()
    time.sleep(2)
    print (saldo)
    exit(0)
