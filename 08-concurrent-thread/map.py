import concurrent.futures
import time
import random
import os


def fun (seg):
    print ("voy a esperar...",seg)
    time.sleep(seg)
    pid = os.getpid()
    print ("soy el proceso {} espere {}..".format(pid,seg))
    return seg

inicio = time.perf_counter()
pool = concurrent.futures.ThreadPoolExecutor()
#segs = random.randint(1,8)
segs=[1,2,3,4,2,1,3]
r = pool.map(fun,segs)
print (r)
orden = []
for k in r:
   orden.append(k)
print (orden)

fin = time.perf_counter()
print ("tiempo total ", fin - inicio)
