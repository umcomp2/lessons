import multiprocessing
import time
import random


def fun (seg):
    print ("voy a esperar...",seg)
    time.sleep(seg)
    print ("espere ..")

inicio = time.perf_counter()
hijos = []
for i in range(10):
    segs = random.randint(1,9)
    hijos.append( multiprocessing.Process(target=fun,args=(segs,)))
    hijos[i].start()

for h in hijos:
    h.join()

fin = time.perf_counter()
print ("tiempo total ", fin - inicio)
