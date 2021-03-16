#!/usr/bin/python3
# -*- coding: UTF-8 -*-
#print ("hóla")

import os
#import sys


leido = os.read(0,20)
os.write(2,leido)

#try:
#	os.read(1,20) # TypeError
#	os.write(1,b"hola\n")
#except TypeError as err:
#  sys.stderr.write(str(err))
#  sys.exit(1)
