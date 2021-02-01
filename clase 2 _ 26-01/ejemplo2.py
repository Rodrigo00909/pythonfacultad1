### Como devolver mas de un valor de retorno?
# Escribir una funcion para ingresar una flecha por teclado 

def leerfecha():
    """ Lee una fecha por teclado y devuelve tres enteros """
    dia = int(input("Ingrese un dia: "))    
    mes = int(input("Ingrese un mes: "))
    año = int(input("Ingrese un año: "))
    return dia, mes, año    

#Programa Principal
d,m,a = leerfecha()
print(d,"/",m,"/",a,sep=" ")