# Trazar el borde de un cuadrado con letras X, ingresando por teclado la longitud de cada lado.
# Cuidado que a veces toma este ejercicio como PARCIAL. No es necesario dibujar una matriz xq la pantalla
# ya es una matriz ya que esta diviida en filas y columnas. El unico problema de no usar matriz aca
# es que es mas dificl xq tenemos que imprimir las cosas en orden de arriba hacia abjo. Mientras que en una amtriz podemos
# avanzar y retroceder a voluntad.
# para lograr dibujar un cuadrado vacio con X, el usuario debera empezar introduciendo el lado:

lado = int(input("Ingrese la longitud del lado(mínimo 3): "))
while lado < 3:
    print("Lado inválido. Intente nuevamente")
    lado = int(input("Ingrese la longitud del lado(mínimo 3): "))
print()
print("X" *lado) #Borde superior
# Multiplicamos la X por la cantidad de lados, si introduce 3 seria X*3
relleno = "X" + " " * (lado-2) + "X"
for i in range(lado-2): # Laterales
    print(relleno)
print("X"*lado) # Borde Inferior
