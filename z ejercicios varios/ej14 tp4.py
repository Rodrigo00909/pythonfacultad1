#EJ14 TP4
#Funciones
def validar_correo(mail):
    b=True
    if (mail.count("@")!=1) or ("." not in mail):
        b=False
    else:
        posa=mail.index("@")
        pospp=mail.rfind(".",0,-4)
        if (mail[ :posa].isalnum()==False)or(len(mail[posa+1:pospp])<1)or(mail[pospp: ].lower()!=".com.ar"):
            b=False    
    return b
def agregar_dominio(dom, mail):
    posa=mail.index("@")
    d=mail[posa+1: ].lower()
    if d not in dom:
        dom.append(d)
#PP
dominios=[]
m=str(input("Ingrese un correo electrónico: "))
while len(m)>0:
    if validar_correo(m):
        print("CORREO VALIDO")
        agregar_dominio(dominios,m)
    else:
        print("CORREO INVALIDO")
    m=str(input("Ingrese un correo electrónico: "))
dominios.sort()
print("_"*20)
print()
print("DOMINIOS:")
for i in range(len(dominios)):
    print("-",dominios[i])
    
    
                
                 
            

        