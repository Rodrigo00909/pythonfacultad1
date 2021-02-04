#Escribir una función que reciba una lista como parámetro y devuelva True si la lista
#está ordenada en forma ascendente o False en caso contrario. Por ejemplo,
#ordenada([1, 2, 3]) retorna True y ordenada(['b', 'a']) retorna False. Desarrollar
#además un programa para verificar el comportamiento de la función. 

def ascendente (lista):
    esAscendente= True 
    i=1 
    while i<len(lista) and esAscendente==True: 
        if lista[i]<lista[i-1]:  
            esAscendente=False
            break
        i = i + 1 
    return esAscendente

#programa principal
milista=[11,9,8,7]
resultado= ascendente(milista)
print(resultado)