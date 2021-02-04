# 8. Utilizar la técnica de listas por comprensión para construir una lista con todos los
# números impares comprendidos entre 100 y 200.
import random

lista = []
cant = random.randrange(100,200)
for i in range(cant):
    lista.append(i)
print(lista)
print()
impares = list(filter(lambda x: x%2!=0, lista))
print(impares)