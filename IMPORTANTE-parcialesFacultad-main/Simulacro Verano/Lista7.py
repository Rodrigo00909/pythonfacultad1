#Desarrollar un programa para generar una lista por comprension con los numeros entre 1 y n que sean multiplos de 7 o que terminen con el digito 7.
# Mostrar por pantalla la lista obtenida, el valor de n se ingresa desde teclado
n = int(input("Ingrese el valor de N: "))
lista = [i for i in range(1, n) if i%7==0 or i%10==7]
print(*lista)