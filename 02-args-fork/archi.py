import os

fd = os.open("archivo.txt",os.O_RDWR|os.O_CREAT)
#fd = os.open("archivo.txt",os.O_RDWR|os.O_APPEND)
#fd = os.open("archivo.txt",os.O_RDWR|os.O_TRUNC)
os.write(fd, b"hola mundo\n")
#os.lseek(fd,10,os.SEEK_END)
#os.lseek(fd,10,os.SEEK_SET)
#os.lseek(fd,10,os.SEEK_CUR)
os.close(fd)

