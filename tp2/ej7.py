# 7. Escribir una función diasiguiente(…) que reciba como parámetro una fecha cualquiera expresada por tres enteros (correspondientes al día, mes y año) y calcule y
# devuelva tres enteros correspondientes el día siguiente al dado.
# Utilizando esta función, desarrollar programas que permitan:
# a. Sumar N días a una fecha.
# b. Calcular la cantidad de días existentes entre dos fechas cualesquiera.


def bisiesto(ano):
    if ano %4 == 0:
        if ano % 100:
            return ano %400 == 0
        return True
    return False

def dia_siguiente(dia,mes,ano):
    m_30=[4,6,9,11]
    
    if mes == 2:
        dias = 28
        if bisiesto(ano):
            dias=29
    elif mes in m_30:
        dias = 30
    else:
        dias = 31
        
    if dia<dias:
        dia+=1
    else:
        dia=1
        if mes == 12:
            mes =1
            ano +=1
        else:
            mes+=1
    return dia,mes,ano

def sumar_dias():
    dia,mes,ano = [int(x) for x in input('ingrese la fecha en formato dd,mm,aaaa: ').split(',')]
    a_suma = int(input('ingrese la cantidad de dias a sumar'))
    
    while a_suma <0 and a_suma !=-1:
        print('suma invalida ingrese un valor positivo')
        a_suma =int(input('ingrese la cantidad de dias a sumar'))
        
        
    for _ in range (a_suma):
        dia,mes,ano = dia_siguiente(dia,mes,ano)
    print(f'la nueva fecha es {dia}/{mes}/{ano}')
    
def dias_entre(d1,m1,a1,d2,m2,a2):
    dias=0
    while (d1!=d2) or (m1!=m2) or (a1!=a2):
        dias +=1
        d1,m1,a1 = dia_siguiente(d1,m1,a1)
    return dias

def diferencia_fechas():
    dia,mes,ano=[int(x) for x in input('ingrese la fecha1 en formato dd,mm,aaaa: ').split(',')]
    dia2,mes2,ano2=[int(x) for x in input('ingrese la fecha2 en formato dd,mm,aaaa: ').split(',')]
    print(f'fecha1:{dia}/{mes}/{ano}')
    print(f'fecha2:{dia2}/{mes2}/{ano2}')
    diferencia = dias_entre(dia,mes,ano,dia2,mes2,ano2)
    print(f'la diferencia {diferencia}')
    


def main():
    print('opta por una de las opciones')
    opcion=int(input('1) para sumar dias\n2) diferencia entre fechas'))
    if opcion == 1:
        sumar_dias()
        
    else:
        diferencia_fechas()
    
    print()

    
if __name__=="__main__":
    main()
        