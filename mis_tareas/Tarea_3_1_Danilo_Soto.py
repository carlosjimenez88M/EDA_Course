########### punto 1 ###################

def conversion_grados (f):
    return(f-32)/1.8

f = float (input("Por favor ingrese el valor a calcular: "))

c = conversion_grados (f)

print( f"Los {f} grados equivalen a {c} grados celsius")









