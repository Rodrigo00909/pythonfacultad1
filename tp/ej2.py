# 2. Desarrollar una función que reciba tres números enteros positivos y verifique si
# corresponden a una fecha válida (día, mes, año). Devolver True o False según la
# fecha sea correcta o no. Realizar también un programa para verificar el comportamiento de la función.

## Hacer la funcion para el año bisiesto
## hacer una funcion para verificar si el año es correcto: deberia confirmar si el dia es mayor a 0 para que no haya errores. Si pasa, deberia confirmar que 
## el mes sea mayor a 0 y menor a 13 para que no haya errores. Si esta ok entonces deberia confirmar si el año es bisiesto usando la funcion que retorne antes.
## Además, antes de las comprobaciones deberia agregar una variable en falso que compruebe el resultado del calculo. Falso si falla, verdadero si queda. Se cambiara depdneindo del IF
## Tambien habrá una comprobacion dentro del año bisiesto para ver si dia es menor o igual a 29, en ese caso el resultado del calculo sera verdadero, tambien debera haber un elif
## para decir que en caso contrario, osea en caso de que bisiesto sea falso, comprobar si el dia es menor o igual a 28. En ese caso el año resultado tambien sera verdadero.
## Ahora comprobar que si el mes es 1 o 3 o 5 o 7 o 8 o 10 o 12 para luego comprobar si es menor o igual a 31. En este caso el resultado del calculo tambien sera verdadero.
## Ahora para los dias restantes comprobarlo, y luego comprobar dentro del mismo si el dia es menor o igual a 30. En caso aprobado el año resultados era verdadero.
## Para finalizar la funcion retornamos el calculo del año.

## Ahora para el programa principal: hay que ingresar en variables tanto el dia como el mes como el año. Asignamos una variable que guardará el resultado del año bisiesto los resultados
## de la funcion del mismo nombre, pasandole como parametro el año. 
## Luego en una variable total guardamos el resultado de la funcion del calculo de la fecha, pasandole como parametro tanto el dia como el mes como el año y el resultado que guardamos
## como variable anteriormente. Ahora hacemos una comprobacion: que si el resultado total es verdadero entonces la fecha sera correcta, y si no es incorrecta

def añobisiesto(a):
    """ Calcula si el año es bisiesto o no """
    bisiesto=False
    if (a%4) == 0:
        if (a%100)==0:
            if (a%400) == 0:
                bisiesto=True
        else:
            bisiesto=True
    return bisiesto

def calcularFecha(d,m,a,aBisiesto):
    """ Calcula si la fecha es correcto o no """
    confirmarValorAño = False
    if d > 0:
        if m > 0 and m < 13:  
            if aBisiesto == True:
                if d <= 29:
                    confirmarValorAño = True
            elif aBisiesto == False:
                if d <= 28:
                    confirmarValorAño = True
        if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
            if d <= 31:
                confirmarValorAño = True
        if m == 2 or m == 4 or m == 6 or m == 9 or m == 11:
            if d <= 30:
                confirmarValorAño = True
    return confirmarValorAño

#Programa Principal
dia = int(input("Ingrese el día: "))
mes = int(input("Ingrese el mes: "))
año = int(input("Ingrese el año: "))
resultadoBisiesto = añobisiesto(año)
fechaTotal = calcularFecha(dia,mes,año,resultadoBisiesto)
if fechaTotal == True:
    print("La fecha ingresada",dia,"/",mes,"/",año, "es correcta")
else:
    print("La fecha ingresada fue incorrecta")


