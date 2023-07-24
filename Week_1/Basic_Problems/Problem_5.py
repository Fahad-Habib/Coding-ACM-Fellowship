from os import environ

for variable in environ:
    print(variable, environ, sep=': ')
