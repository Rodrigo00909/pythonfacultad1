def ascendente(lista):
    esAscendente= True 
    i=1 
    while i<len(lista) and esAscendente==True: 
        if lista[i]<lista[i-1]:  
            esAscendente=False
            break
        i = i + 1 
    return esAscendente

#programa principal
milista=[1,2,3,4]
#milista=["b", "a"]
resultado= ascendente(milista)
print(resultado)