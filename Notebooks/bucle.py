def run():
    limite = 1000

    valor_inicial = 0
    
    valor_anexar = 1 + valor_inicial
    
    '''Acá vamos hacer el bucle, esto es interesante'''
    while valor_anexar < limite:
        print(valor_anexar)
        valor_inicial = valor_inicial + 1
        valor_anexar = valor_inicial + 1

if __name__ == '__main__':
    run()

# Genera error (WIROAL)
#    py bucle.py
# Traceback (most recent call last):
#  File "bucle.py", line 16, in <module>
#    correr ()
# NameError: name 'correr' is not defined