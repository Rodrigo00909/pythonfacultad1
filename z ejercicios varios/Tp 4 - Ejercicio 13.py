#Tp 4 - Ejercicio 13
#El programa funciona correctamente, pero si el número que queremos convertir es mayor a 999.999, el dígito del 100.000 es 0, el dígito del 10.000 es 0 y el dígito del 1.000 es mayor a 1, el programa se confunde y no escribe el dígito del 1000. 
#Funciones
#Las variables que tienen nombres que empiezan por 'DEF' son las variables que se utilizan en las funciones, para evitar la repetición de los nombres de las variables en el programa principal.
def EscribirNúmero(DEFNúmero):
    if DEFNúmero > 999999999:
        print("El número ingresado es demasiado grande. El programa no puede transformarlo a palabras.")
    elif DEFNúmero < 0:
        print("El número ingresado es negativo. El programa no puede transformarlo a palabras.")
    else:
        NumerosEscritos1Al10 = []
        NumerosEscritos1Al10.append("cero"), NumerosEscritos1Al10.append("uno"), NumerosEscritos1Al10.append("dos"), NumerosEscritos1Al10.append("tres"), NumerosEscritos1Al10.append("cuatro"), NumerosEscritos1Al10.append("cinco"), NumerosEscritos1Al10.append("seis"), NumerosEscritos1Al10.append("siete"), NumerosEscritos1Al10.append("ocho"), NumerosEscritos1Al10.append("nueve")
        NumerosEscritos10Al100 = []
        NumerosEscritos10Al100.append("diez"), NumerosEscritos10Al100.append("once"), NumerosEscritos10Al100.append("doce"), NumerosEscritos10Al100.append("trece"), NumerosEscritos10Al100.append("coatorce"), NumerosEscritos10Al100.append("quince"), NumerosEscritos10Al100.append("dieci"), NumerosEscritos10Al100.append("veinte"), NumerosEscritos10Al100.append("veinti"), NumerosEscritos10Al100.append("treinta"), NumerosEscritos10Al100.append("cuarenta"), NumerosEscritos10Al100.append("cincuenta"), NumerosEscritos10Al100.append("sesenta"), NumerosEscritos10Al100.append("setenta"), NumerosEscritos10Al100.append("ochenta"), NumerosEscritos10Al100.append("noventa")
        NumerosEscritos100Al1000 = []
        NumerosEscritos100Al1000.append("cien"), NumerosEscritos100Al1000.append("doscientos"), NumerosEscritos100Al1000.append("trescientos"), NumerosEscritos100Al1000.append("cuatrocientos"), NumerosEscritos100Al1000.append("quinientos"), NumerosEscritos100Al1000.append("seiscientos"), NumerosEscritos100Al1000.append("setecientos"), NumerosEscritos100Al1000.append("ochocientos"), NumerosEscritos100Al1000.append("novecientos")
        DEFDígitos = 1
        DEFNúmeroCopia = DEFNúmero
        while DEFNúmeroCopia > 10:
            DEFNúmeroCopia //= 10
            DEFDígitos += 1
        DEFNúmeroCopia = DEFNúmero
        DEFNúmeroEnLista = []
        for x in range(DEFDígitos):
            DEFNúmeroEnLista.append(DEFNúmeroCopia % 10)
            DEFNúmeroCopia //= 10
        DEFNúmeroEscrito1 = []
        
    #------------------------------INICIO PRIMEROS TRES DÍGITOS------------------------------------------------ 
        
        if len(DEFNúmeroEnLista) >= 3:
            DEFNúmeroEscrito1.append(NumerosEscritos100Al1000[DEFNúmeroEnLista[2] - 1])
        if len(DEFNúmeroEnLista) >= 2:
            if DEFNúmeroEnLista[1] > 2 and DEFNúmeroEnLista[0] == 0:
                DEFNúmeroEscrito1.append(NumerosEscritos10Al100[DEFNúmeroEnLista[1] + 6])
            elif DEFNúmeroEnLista[1] == 2 and DEFNúmeroEnLista[0] == 0:
                DEFNúmeroEscrito1.append(NumerosEscritos10Al100[7])
            elif DEFNúmeroEnLista[1] == 1 and DEFNúmeroEnLista[0] == 0:
                DEFNúmeroEscrito1.append(NumerosEscritos10Al100[8])
            elif DEFNúmeroEnLista[1] == 2 and DEFNúmeroEnLista[0] != 0:
                DEFNúmeroEscrito1.append(NumerosEscritos10Al100[8] + NumerosEscritos1Al10[DEFNúmeroEnLista[0]])
            elif DEFNúmeroEnLista[1] == 1 and (DEFNúmeroEnLista[0] == 1 or DEFNúmeroEnLista[0] == 2 or DEFNúmeroEnLista[0] == 3 or DEFNúmeroEnLista[0] == 4 or DEFNúmeroEnLista[0] == 5):
                DEFNúmeroEscrito1.append(NumerosEscritos10Al100[DEFNúmeroEnLista[0]])
            elif DEFNúmeroEnLista[1] == 1 and DEFNúmeroEnLista[0] > 5:
                DEFNúmeroEscrito1.append(NumerosEscritos10Al100[6] + NumerosEscritos1Al10[DEFNúmeroEnLista[0]])
            elif DEFNúmeroEnLista[1] > 2 and DEFNúmeroEnLista[0] > 0:
                DEFNúmeroEscrito1.append(NumerosEscritos10Al100[DEFNúmeroEnLista[1] + 6] + " y " + NumerosEscritos1Al10[DEFNúmeroEnLista[0]])
        else:
            DEFNúmeroEscrito1.append(NumerosEscritos1Al10[DEFNúmeroEnLista[0]])
        
    #------------------------------FIN PRIMEROS TRES DÍGITOS---------------------------------------------------
    #------------------------------INICIO SEGUNDOS TRES DÍGITOS------------------------------------------------
            
        DEFNúmeroEscrito2 = []
        if len(DEFNúmeroEnLista) >= 6:
            if DEFNúmeroEnLista[5] != 0:
                DEFNúmeroEscrito2.append(NumerosEscritos100Al1000[DEFNúmeroEnLista[5] - 1])
        if len(DEFNúmeroEnLista) >= 5:
            if DEFNúmeroEnLista[4] != 0:
                if DEFNúmeroEnLista[4] > 2 and DEFNúmeroEnLista[3] == 0:
                    DEFNúmeroEscrito2.append(NumerosEscritos10Al100[DEFNúmeroEnLista[4] + 6])
                elif DEFNúmeroEnLista[4] == 2 and DEFNúmeroEnLista[3] == 0:
                    DEFNúmeroEscrito2.append(NumerosEscritos10Al100[7])
                elif DEFNúmeroEnLista[4] == 1 and DEFNúmeroEnLista[3] == 0:
                    DEFNúmeroEscrito2.append(NumerosEscritos10Al100[8])
                elif DEFNúmeroEnLista[4] == 2 and DEFNúmeroEnLista[3] != 0:
                    DEFNúmeroEscrito2.append(NumerosEscritos10Al100[8] + NumerosEscritos1Al10[DEFNúmeroEnLista[3]])
                elif DEFNúmeroEnLista[4] == 1 and (DEFNúmeroEnLista[3] == 1 or DEFNúmeroEnLista[3] == 2 or DEFNúmeroEnLista[3] == 3 or DEFNúmeroEnLista[3] == 4 or DEFNúmeroEnLista[3] == 5):
                    DEFNúmeroEscrito2.append(NumerosEscritos10Al100[DEFNúmeroEnLista[3]])
                elif DEFNúmeroEnLista[4] == 1 and DEFNúmeroEnLista[3] > 5:
                    DEFNúmeroEscrito2.append(NumerosEscritos10Al100[6] + NumerosEscritos1Al10[DEFNúmeroEnLista[3]])
                elif DEFNúmeroEnLista[4] > 2 and DEFNúmeroEnLista[3] > 0:
                    DEFNúmeroEscrito2.append(NumerosEscritos10Al100[DEFNúmeroEnLista[4] + 6] + " y " + NumerosEscritos1Al10[DEFNúmeroEnLista[3]])
            DEFNúmeroEscrito2.append("mil")
        elif len(DEFNúmeroEnLista) == 4:
            DEFNúmeroEscrito2.append(NumerosEscritos1Al10[DEFNúmeroEnLista[3]])
            DEFNúmeroEscrito2.append("mil")
        elif len(DEFNúmeroEnLista) == 5 and DEFNúmeroEnLista[5] == 0:
            DEFNúmeroEscrito2.append(NumerosEscritos1Al10[DEFNúmeroEnLista[3]])
            DEFNúmeroEscrito2.append("mil")
        elif len(DEFNúmeroEnLista) == 5 and DEFNúmeroEnLista[5] == 0 and DEFNúmeroEnLista[6] == 0:
            DEFNúmeroEscrito2.append(NumerosEscritos1Al10[DEFNúmeroEnLista[3]])
            DEFNúmeroEscrito2.append("mil")
        
    #------------------------------FIN SEGUNDOS TRES DÍGITOS---------------------------------------------------
    #------------------------------INICIO TERCEROS TRES DÍGITOS------------------------------------------------
            
        DEFNúmeroEscrito3 = []
        if len(DEFNúmeroEnLista) >= 9:
            DEFNúmeroEscrito3.append(NumerosEscritos100Al1000[DEFNúmeroEnLista[8] - 1])
        if len(DEFNúmeroEnLista) >= 8:
            if DEFNúmeroEnLista[7] > 2 and DEFNúmeroEnLista[6] == 0:
                DEFNúmeroEscrito3.append(NumerosEscritos10Al100[DEFNúmeroEnLista[7] + 6])
            elif DEFNúmeroEnLista[7] == 2 and DEFNúmeroEnLista[6] == 0:
                DEFNúmeroEscrito3.append(NumerosEscritos10Al100[7])
            elif DEFNúmeroEnLista[7] == 1 and DEFNúmeroEnLista[6] == 0:
                DEFNúmeroEscrito3.append(NumerosEscritos10Al100[8])
            elif DEFNúmeroEnLista[7] == 2 and DEFNúmeroEnLista[6] != 0:
                DEFNúmeroEscrito3.append(NumerosEscritos10Al100[8] + NumerosEscritos1Al10[DEFNúmeroEnLista[6]])
            elif DEFNúmeroEnLista[7] == 1 and (DEFNúmeroEnLista[6] == 1 or DEFNúmeroEnLista[6] == 2 or DEFNúmeroEnLista[6] == 3 or DEFNúmeroEnLista[3] == 4 or DEFNúmeroEnLista[6] == 5):
                DEFNúmeroEscrito3.append(NumerosEscritos10Al100[DEFNúmeroEnLista[6]])
            elif DEFNúmeroEnLista[7] == 1 and DEFNúmeroEnLista[6] > 5:
                DEFNúmeroEscrito3.append(NumerosEscritos10Al100[6] + NumerosEscritos1Al10[DEFNúmeroEnLista[6]])
            elif DEFNúmeroEnLista[7] > 2 and DEFNúmeroEnLista[6] > 0:
                DEFNúmeroEscrito3.append(NumerosEscritos10Al100[DEFNúmeroEnLista[7] + 6] + " y " + NumerosEscritos1Al10[DEFNúmeroEnLista[6]])
            DEFNúmeroEscrito3.append("millones")
        elif len(DEFNúmeroEnLista) == 7:
            DEFNúmeroEscrito3.append(NumerosEscritos1Al10[DEFNúmeroEnLista[6]])
            if DEFNúmeroEnLista[6] == 1:
                DEFNúmeroEscrito3.append("millón")
            else:
                DEFNúmeroEscrito3.append("millones")
            
    #------------------------------FIN TERCEROS TRES DÍGITOS------------------------------------------------
            
        print("El número ingresado se escribe: ", end=" ")
        for y in range(len(DEFNúmeroEscrito3)):
            print(DEFNúmeroEscrito3[y], end=" ")
        for a in range(len(DEFNúmeroEscrito2)):
            print(DEFNúmeroEscrito2[a], end=" ")
        for b in range(len(DEFNúmeroEscrito1)):
            print(DEFNúmeroEscrito1[b], end=" ")
        print(".")

#Programa Principal
Número = int(input("Ingrese un número: "))
NúmeroEscrito = EscribirNúmero(Número)