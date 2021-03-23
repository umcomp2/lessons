import os

print("hola mundo " +str(os.getpid()))
os.fork()
print ("soy el procso nuevo "+str(os.getpid()))
os.fork()
print ("soy el ultimo "+str(os.getpid()))
