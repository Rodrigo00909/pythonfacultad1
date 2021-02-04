from random import randint

def cargar_random(n,minimo,maximo):
    lista = [randint(minimo,maximo)for i in range(n)]
    return lista

def normalizar(lista):
    suma =sum(lista)
    num= 1/suma
    for i in range(len(lista)):
        lista[i] = num *lista[i]
    

def main():
    lista = cargar_random(5,1,10)
    print(f'la lista es: {lista}')
    normalizar(lista)
    print(f'la lista normalizada {lista}')
    print(sum(lista))
    
if __name__=="__main__":
    main()


## Normalizar: for q recorre por range y x cada elemento hace 1 sobre el valor de la suma de la lista x el valor de la lista. asi se obtiene la proporcion

## 5 valores entre 1 minimo maximo 10