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

f = [ pool.submit(fun,i) for i in range(1,4) ]
print (f)

for k in  concurrent.futures.as_completed(f):
    print (k.result())

print (f)

fin = time.perf_counter()
print ("tiempo total ", fin - inicio)
