import os
import time

print ("soy el padre", os.getpid(), os.getppid())

pid = os.fork()

if pid > 0:
#    os.wait()
    print ("soy el padre")

else:
    time.sleep(3)
    print ("soy el hijo", os.getpid(), os.getppid())
