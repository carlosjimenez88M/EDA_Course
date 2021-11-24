def run():
    limite = 10

    valor_inicial = 0
    
    valor_anexar = 1 + valor_inicial
    
    '''Acá vamos hacer el bucle'''
    while valor_anexar <= limite:
        print(valor_anexar)
        valor_inicial = valor_inicial + 1
        valor_anexar = valor_inicial + 1

## Siempre acaba así cualquier estructura 

if __name__ == '__main__':
    run()