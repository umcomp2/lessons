import signal, os
import time

def handler(signum, frame):
    print('Signal handler called with signal', signum)
    signal.alarm(1)

# Set the signal handler and a 5-second alarm
signal.signal(signal.SIGALRM, handler)
signal.alarm(1)


time.sleep(10)

print ("termino el programa")
