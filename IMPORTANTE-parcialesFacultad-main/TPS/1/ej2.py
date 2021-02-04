"""
2. Desarrollar una función que reciba tres números enteros positivos y verifique si
corresponden a una fecha válida (día, mes, año). Devolver True o False según la
fecha sea correcta o no. Realizar también un programa para verificar el comportamiento de la función.
"""

def añocorrecto(d,m,a):
    """Recibe dia, mes y año para calcular si es bisiesto o no con este último. Una vez hecho esto, 
    hace el calculo para ver si la fecha ingresada es correcta. """
    bisiesto=False
    if (año%4) == 0:
        if (año%100)==0:
            if (año%400) == 0:
                bisiesto=True
        else:
            bisiesto=True
    añoresultado=False
    if d > 0:
        if 0 < m < 13:
            if m == 2 :
                if bisiesto == True:
                    if d <= 29:
                        añoresultado=True
                elif bisiesto == False:
                    if d <= 28:
                        añoresultado=True
            if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12 :
                if d <=31:
                    añoresultado=True
            if m == 4 or m == 6 or m == 9 or m == 11:
                if d <= 30:
                    añoresultado=True
    return añoresultado
                    
    
dia=int(input("ingrese un dia: "))
mes=int(input("ingrese un mes: "))
año=int(input("ingrese un año: "))
resultadototal=añocorrecto(dia,mes,año)
if resultadototal ==True:
    print("La fecha ingresada es correcta")
else:
    print("la fecha ingresada es incorrecta")