
dominios = []
mail = input("Ingrese la direccion de correo electronico: ").lower()
while len(mail) > 0:
    mail_valido = False
    if mail.count("@") == 1:
        dom = mail.split("@")
        if dom[0].isalnum() == True and dom[1][-7:] == ".com.ar" and len(dom[1])-7 > 0:
            if dom[1][:-7] not in dominios:
                dominios.append(dom[1][:-7])
            mail_valido = True
    
    if mail_valido == False:
        print("El mail es invalido")
    mail = input("Ingrese la direccion de correo electronico: ").lower()

dominios.sort()
print("Los siguientes dominios fueron los ingresados: ")

for i in range(len(dominios)):
    print(f"- {dominios[i]}")

        
    
        
    