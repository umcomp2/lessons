import os
import time

print ("soy el padre", os.getpid(), os.getppid())

pid = os.fork()

if pid > 0:
    #os.wait()
    time.sleep(30)
    print ("soy el padre")

else:
    print ("soy el hijo")
