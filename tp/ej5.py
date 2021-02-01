# 5. Escribir dos funciones separadas para imprimir por pantalla los siguientes patrones
# de asteriscos, donde la cantidad de filas se recibe como parámetro:

# Una funcion deberia ser para el patron de asteriscos en matriz y otro en escaleras. El primero debera recorrer con un for en el rango que se ingrese por teclado (cantidad de filas)
# otro for deberá ir debajo para multiplicar x2 el rango de las filas, debera imprimir un *

def imprimirAsteriscosEnMatriz(cantidadFilas):
    """ Imprime una serie de asteriscos en forma de Matriz """
    for i in range(cantidadFilas):
        for j in range(cantidadFilas*2):
            print("*", end="")
        print() #Este print logra que no siga  derecho y ocupe un espacio mas reducido

def imprimitAsteriscosEnEscalera(cantidadFilas):
    """ Imprime una serie de asteriscos en forma de Matriz """
    asteriscos = 2 # la diferencia de la matriz es que este debe seguir una escalera, entonces igualo una variable a 2
    for i in range(cantidadFilas): # Este for imprimira las filas (de arriba a abajo)
        for j in range(asteriscos): # Este for imprimira las columnas (de costado), que deberá empezar por 2
            print("*", end="") # Dibuja los asteriscos
        print() # Separacion
        asteriscos += 2 # Y sumando 2 asteriscos a la variable por cada iteracion hará que cada renglon tenga 2 asteriscos mas formando una escalera

#Programa Principal
filas = int(input("Ingrese la cantidad de filas: "))

print("Patrón en Matriz")
imprimirAsteriscosEnMatriz(filas)

print("Patrón en Escalera")
imprimitAsteriscosEnEscalera(filas)