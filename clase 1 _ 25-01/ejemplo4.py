## Funcion range()

### Formato 1: range(<vfinal>)
## Genera una secuencia de numeros enteros entre 0 y el valor final
## valor finalo esta incluido. Si pongo range(10) me generara una secuancia de numeros enteros que comienza en 0 y termina en 9

### Formato 2: range(vinicial, vfinal)
## Genera una secuencia de numeros enteros entre valor inicial y valor final con <inc> es decir incremento. Si no defino el incremento se pone como default 1, pero yo le puedo poner 
## el que necesite. Tambien incrementos negativos. Pero en ese caso el valor inicial debe ser mas grande que el valor final.: range(vinicial, vfinal, inc)

### For y Range: Imprimir numeros impares entre 1 y n
n = int(input("Ingrese un numero: "))
for i in range(1, n+1, 2): ## Porque incremento en 2? xq queriamos numeros IMPARES: 1, 3, 5, 7, etc. Range 1, n+1: el +1 esta para superar 
                            ##el problema de que se termina 1 num antes del num final xq el valor final no esta incluido
    print(i, end=" ");
print()