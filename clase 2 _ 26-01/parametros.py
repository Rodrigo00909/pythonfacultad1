### Parametros y Variables

### Variable Local: Variable creada dentro de una función. 
### Varible global: existen en todo el programa principal
### Vamos a usar las LOCALES
# Las variables del programa principal NO pueden ser utilizadas dentro de una funcion a menos que se pasen como parametro.

## Parametros reales: son los que se escriben en la llamada a la funcion
## parametros formales: son los que aparecen en el encabezado de la funcion

### Mutables e Inmutables
### Inmutables: Variables simples, cadenas de caracteres (string), y tuplas.
### Mutables: Listas, conjuntos y diccionarios

## Parametros mutables:
def agregarTotal(lista):
    total = 0
    for i in range(len(lista)):
        total = total + lista[i]
    lista.append(total)

#Programa Principal
milista = [1,2,3,4]
agregarTotal(milista)
print(milista)

# En este programa, al ser una lista el protagonista, es decir un mutable, el valor de lista en la funcion guardará el dato configurado en milista por mas que no lo retorne.
# Es decir, si bien la variable lista local de la funcion agregarTotal se le agregará un hijo, tambien se hará en milista(el parametro) porque es mutable

### Si la modificación se hace sobre un parametro formal inmutable, el parametro real no resulta afectado