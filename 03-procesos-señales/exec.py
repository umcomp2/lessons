import os
import time

print ("soy el padre", os.getpid(), os.getppid())

pid = os.fork()

if pid > 0:
    os.wait()
    print ("soy el padre")

else:
    print ("soy el hijo", os.getpid(), os.getppid())
#    time.sleep(3)
    #os.execlp("ls","/usr/bin/ls","-l")
    #comando = input()
    os.execlp("rm","/usr/bin/rm","-f" ,"/root/algo.txt")
    print ("soy el hijo y no importa lo que haga a partir de este punto ... nunca se ejecutara")
