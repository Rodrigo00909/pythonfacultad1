def eliminarcaracteres(vec1,vec2):
    """ELIMINA LAS PALABRAS DE LA PRIMERA LISTA QUE SE ENCUENTRAN EN LA SEGUNDA"""
    cont=0
    while cont!=len(vec1):
        if vec1[cont] in vec2:
            vec1.pop(cont)
        else:
            cont+=1
    return vec1
#pp
print("CARGADO DE LISTA INICIAL:")
lista1=[]
a=input("Ingrese una palabra o END (en mayusculas) para terminar: ")
while a!="END":
    lista1.append(a)
    a=input("Ingrese otra palabra o END (en mayusculas) para terminar: ")
print("CARGADO DE LA LISTA DE PALABRAS A ELIMINAR:")

lista2=[]
b=input("Ingrese una palabra o END (en mayusculas) para terminar: ")
while b!="END":
    lista2.append(b)
    b=input("Ingrese otra palabra o END (en mayusculas) para terminar: ")
print("LISTAS:")
print("Lista inicial:",lista1)
eliminarcaracteres(lista1,lista2)
print("Lista de palabras a eliminar:",lista2)
print("Lista final:",lista1)