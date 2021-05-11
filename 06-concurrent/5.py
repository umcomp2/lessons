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
pul = concurrent.futures.ProcessPoolExecutor(4)
#segs = random.randint(1,8)
segs=[1,2,3,4,3,2,2]
r = pul.map(fun,segs)

for k in r:
    print (k)

fin = time.perf_counter()
print ("tiempo total ", fin - inicio)
