

A = []
for i in range(1, 339):
    if i % 3 == 0 and i != 9:
        A.append(i)

print(list(A))
print('los elementos de lista', len(A), 'sin incluir 9')