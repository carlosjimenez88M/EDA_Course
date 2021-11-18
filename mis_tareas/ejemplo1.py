Peso = float(input("Por favor ingrese su peso : "))
Estatura = float(input("Por favor ingrese su estatura : "))
BMI = Peso/(Estatura**2)
if BMI <= 18.5:
    print('Tu indice de masa corporal es :', BMI, ' Estas flaco')

elif 18.5 < BMI < 25:
    print('Tu indice de masa corporal es :', BMI,'Ni fu ni fa')

elif 25 < BMI < 30:
    print('Tu indice de masa corporal es :', BMI,' Estamos gorditos!!')

elif BMI > 30:
    print('Tu indice de masa corporal es :', BMI,'No sigas asi! vas a explotar ')