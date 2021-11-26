##Punto extra 4

for i in range (5):
    for j in range(7):
        if (i == 0 or i == 4) and (1 <= j <= 3):
            print("*", end='')
        if (0 < i < 4) and (1 <= j <= 4):
            print("*", end='')
        if i == 2 and j == 5:
           print("*", end='') 
    print()
print()