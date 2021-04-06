import mmap
import os
import time
import signal

def lee(nro, frame):
    leido = area.read(10)
    print (leido)

signal.signal(signal.SIGUSR1, lee)
area = mmap.mmap(-1, 100)

pid = os.fork()

if pid == 0: #hijo
    area.write(b"algo")
    os.kill(os.getppid(), signal.SIGUSR1)
    time.sleep(2)
    area.seek(0)
    area.write(b"otra cosa")
    exit()

#padre
os.wait()
area.seek(0)
leido = area.read(10)
print (leido)


