""" Uso del operador IN """ 
# Escribir una funcion que reciba como parametros dos numeros correspondientes al mes y año de una fecha y devuelva cuantos dias tiene ese mes en ese año
def obtener_cant_dias(mes, año):
    """ Devuelve cuantos dias tiene X mes en X año """
    if mes in [1,3,5,7,8,10,12]: #Lista implicita # Meses que tienen 31 dias
        dias = 31
    elif mes in [4,6,9,11]: # Meses que tienen 30 dias
        dias = 30
    elif mes == 2: # Es febrero?
        if(año%4==0 and año%100==0) or (año%400==0): # Es un año bisiesto? tiene q ser divisible x 4. Pero si es divisible x 4 y tb x 100 no es bisiesto, pero si si es divisible x 400
            dias = 29
        else: 
            dias = 28
    else: 
        dias = -1 # Mes inválido
    return dias

mes = int(input("Introduce un mes: "))
año = int(input("Introduce un año: "))
print(f"El mes {mes} del año {año} tiene {obtener_cant_dias(mes,año)}")