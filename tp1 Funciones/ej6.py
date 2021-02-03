# 6. Desarrollar una función que reciba como parámetros dos números enteros positivos y devuelva el número que resulte de concatenar ambos valores. Por ejemplo,
# si recibe 1234 y 567 debe devolver 1234567. No se permite utilizar facilidades de
# Python no vistas en clase.

def concatenar(num1, num2):
    contador=1
    num2contador=num2
    while num2contador>9:
        num2contador//=10
        contador+=1
    
    concatenacion=num1*(10**contador)+num2
    return concatenacion

#Programa principal
a=int(input("Ingrese el primer número a concatenar: "))

b=int(input("Ingrese el segundo número a concatenar: "))
        
resultado=concatenar(a, b)

print("El resultado es", resultado)