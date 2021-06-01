import concurrent.futures
import time
import random
import os


def fun (seg):
    print ("voy a esperar...",seg)
    print (os.getpid())
    time.sleep(seg)
    print ("espere ..")
    return seg

inicio = time.perf_counter()

pool = concurrent.futures.ThreadPoolExecutor()

f = [ pool.submit(fun,i) for i in range(1,20) ]
print (f)

for i in range(len (f)):
    print (f[i].result())

print (f)

fin = time.perf_counter()
print ("tiempo total ", fin - inicio)
