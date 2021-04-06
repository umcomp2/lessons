import os

fdl,fde = os.pipe()


pid = os.fork()

if pid == 0:
    os.close(fde)
    while True:
        leido = os.read(fdl,1024)
        if len(leido) == 0:
        #if leido == b'':
            break
        os.write(1,leido)
    exit()
os.close(fdl)
while True:
    leido = os.read(0,1024)
    if len(leido) == 0:
    #if leido == b'':
        break
    os.write(fde,leido)

