import getopt

args = '-a b -cfoo d bar a1 a2'.split()

opciones, argumentos = getopt.getopt(args, 'za:c:')
print(opciones)
print(argumentos)
opciones, argumentos = getopt.getopt(args, 'z:a:c:')
print(opciones)
print(argumentos)

