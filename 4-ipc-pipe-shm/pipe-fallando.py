import os

fdl,fde = os.pipe()


pid = os.fork()
#hijo
if pid == 0:
##descomentar##    os.close(fdl)
    while True:
        leido = os.read(1,1024)
        if len(leido) == 0:
        #if leido == b'':
            break
        os.write(fde,leido)
    exit()
#padre
##descomentar##os.close(fde)
while True:
    leido = os.read(fdl,1024)
    if len(leido) == 0:
    #if leido == b'':
        break
    os.write(1,leido)

