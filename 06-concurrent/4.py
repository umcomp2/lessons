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
fut = []
for i in range(10):
    #segs = random.randint(1,8)
    segs=[1,2,3,4,5,6,7,1,2,3]
    fut.append(pul.submit(fun,segs[i]))

for k in  concurrent.futures.as_completed(fut):
    print (k.result())

fin = time.perf_counter()
print ("tiempo total ", fin - inicio)
