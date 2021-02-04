lista = ["Oros","Bastos","Copas","Espadas"]
lista2 =[f"{(i%12)+1} {lista[(i//12)]}" for i in range(len(lista)*12)]
print(lista2)