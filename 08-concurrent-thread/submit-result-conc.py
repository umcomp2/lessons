# a una variable compartida y el otro reste un monto (extrae)
#de la misma varaible. Asegurar que se ejecute primero el que deposita,
# para evitar que el saldo sea negativo.

from concurrent.futures import ThreadPoolExecutor
import time
import threading

monto = 0
candado = threading.Lock()

def depositar(hilo, deposito):
    global monto
    print('{} depositando {} de monto ({})...'. format(hilo, deposito, monto))
    for i in range(deposito):
        candado.acquire()
        monto = monto + 1
        candado.release()

def extraer(hilo, extraccion):
    global monto
    print('{} extrayendo {} de monto ({})...'. format(hilo, extraccion, monto))
    for i in range(extraccion):
        candado.acquire()
        monto = monto - 1
        candado.release()

if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=2) as executor:
        #cada executor es un hilo???
        future1 = executor.submit(depositar,'hilo1',100000)
        future2 = executor.submit(extraer,'hilo2', 100000)
    if future1.done() and future2.done():
        print("la tarea se realizo con exito!")
        print('monto final: ', monto)
