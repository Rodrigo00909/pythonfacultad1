## FUNCIONES LISTAS
#Largo de la lista
lista = [3,4,5,6,7,8,9,0,3,3,3,3]
print(len(lista))
#Suma
lista2 = [3,4,5,6]
print(sum(lista2)) # 18
#Devuelve el mayor
lista3 = [4,6,3,5]
print(max(lista3)) # 6 
#Devuelve el menor
lista4 = [4,6,3,5] # 3
print(min(lista4)) 
## EL FALSO SE CONSIDERA 0 Y EL VERDADERO SE CONSIDERA 1. El falso es menor
#Convierte cualquier iterable en una lista usando otra funcion como range.
lista5 = list(range(5))
print(lista5) # [0,1,2,3,4]
#IN: Permite verificar la presencia de un elemento devolviendo ture o false.
# NOT IN: verifica la ausencia
lista6 = [3,4,5,6]
if 4 in lista6:
    print("Hay un 4 en la lista")