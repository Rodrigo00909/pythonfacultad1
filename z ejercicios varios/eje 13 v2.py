#Funciones
def numerosaletras(numero):
    millon=0
    numero=numero.zfill(12)
    numero=[int(x) for x in numero]
    letras=[]
    for i in range(0, 12,3):
        if numero[i]==1 and (numero[i+1]==0 and numero[i+2]==0):
            letras.append("cien")
        elif numero[i]>0:
            letras.append(listapalabras4[numero[i]-1])
        if numero[i+1]>1:
            if numero[i+1]==2 and numero[i+2]==0:
                letras.append("veinte")
            elif numero[i+2]>0 and numero[i+1]==2:
                letras.append("veinti"+listapalabras[numero[i+2]-1])
            else:  
                letras.append(listapalabras3[numero[i+1]-2])
                if numero[i+2]>0:
                    letras.append("y "+listapalabras[numero[i+2]-1])
                
        elif numero[i+1]==1:
            if numero[i+2]==0:
                letras.append("diez")
            elif numero[i+2]<6:
                letras.append(listapalabras2[numero[i+2]])
            elif numero[i+2]>0:
                letras.append("diez y "+listapalabras[numero[i+2]-1])
        elif numero[i+1]==0 and numero[i+2]==1 and i!=9:
            letras.append("un"+ " ")
        elif numero[i+1]==0 and numero[i+2]!=0:
            letras.append(listapalabras[numero[i+2]-1])
        
        if (numero[i+1]+numero[i+2]+numero[i])>0 and i==0:
            letras.append("mil")
            millon=1
        if (numero[i+1]+numero[i+2]+numero[i])>0 and i==3:
            letras.append("millones")
            millon=0
        if (numero[i+1]+numero[i+2]+numero[i])>0 and i==6 :
            letras.append("mil")
                  
        
    if millon==1:
        letras.insert(letras.index("mil")+1, "millones")
                
                
    letras=" ".join(letras)
    
    if letras=="":
        letras="Cero"
            
        
        
                
            
        
    return letras

def imprimir(numero):
    numeroimpreso=list(numero)
    i=-3
    while i>-1*len(numeroimpreso):
        numeroimpreso.insert(i, ".")
        i-=4
    print(*numeroimpreso, sep="")
        
#Programa principal
listapalabras=["uno", "dos", "tres", "cuatro", "cinco", "seis",
               "siete", "ocho", "nueve", "un"]

listapalabras2=["diez", "once", "doce", "trece", "catorce",
                "quince"]

listapalabras3=["veinti", "treinta", "cuarenta", "cincuenta", "sesenta",
                "setenta", "ochenta", "noventa"]

listapalabras4=["ciento", "doscientos", "trescientos", "cuatrocientos", "quinientos", "seicientos",
                "setecientos", "ochocientos", "novecientos"]

decimal=input("introduzca el número en decimal a ser convertido: ")

imprimir(decimal)
      
      
      
decimal=numerosaletras(decimal)

print(decimal.title())
