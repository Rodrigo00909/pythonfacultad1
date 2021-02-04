# 5. Escribir una función que reciba una lista como parámetro y devuelva True si la lista
# está ordenada en forma ascendente o False en caso contrario. Por ejemplo,
# ordenada([1, 2, 3]) retorna True y ordenada(['b', 'a']) retorna False. Desarrollar
# además un programa para verificar el comportamiento de la función. 

def esAscendente(lista):
    ascendente = True 
    i=1 
    while i<len(lista) and ascendente==True: 
        if lista[i]<lista[i-1]:  
            ascendente=False
            break
        i = i + 1 
    return ascendente

#Programa Principal
lista = []
n = int(input("Introduce una lista, -1 para terminar:"))
while n != -1: 
    lista.append(n)
    n = int(input("Introduce una lista, -1 para terminar:"))
resultado = esAscendente(lista)
print(resultado)



