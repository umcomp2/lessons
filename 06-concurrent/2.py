import concurrent.futures
import time
import random


def fun (seg):
    print ("voy a esperar...",seg)
    time.sleep(seg)
    print ("espere ..")
    return seg

inicio = time.perf_counter()

pul = concurrent.futures.ProcessPoolExecutor()

f = pul.submit(fun,1)

print (f.result())

fin = time.perf_counter()
print ("tiempo total ", fin - inicio)
