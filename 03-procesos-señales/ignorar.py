import os
import time
import signal

#signal.signal(signal.SIGKILL,signal.SIG_IGN)
signal.signal(signal.SIGSTOP,signal.SIG_IGN)
signal.signal(signal.SIGINT,signal.SIG_IGN)
print ("soy el padre", os.getpid(), os.getppid())

pid = os.fork()

if pid > 0:
    #os.wait()
    time.sleep(30)
    print ("soy el padre")

else:
    print ("soy el hijo")
