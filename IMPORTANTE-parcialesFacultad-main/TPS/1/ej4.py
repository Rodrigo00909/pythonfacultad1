"""
4. Un comercio de electrodomésticos necesita para su línea de cajas un programa que
le indique al cajero el cambio que debe entregarle al cliente. Para eso se ingresan
dos números enteros, correspondientes al total de la compra y al dinero recibido.
Informar cuántos billetes de cada denominación deben ser entregados al cliente
como vuelto, de tal forma que se minimice la cantidad de billetes. Considerar que
existen billetes de $500, $100, $50, $20, $10, $5 y $1. Emitir un mensaje de error
si el dinero recibido fuera insuficiente. Ejemplo: Si la compra es de $317 y se abona con $500, 
el vuelto debe contener 1 billete de $100, 1 billete de $50, 1 billete
de $20, 1 billete de $10 y 3 billetes de $1.

"""
def calcularvuelto(total,recibido):
    quinientos = 500
    cien = 100
    cincuenta = 50
    veinte = 20
    diez = 10
    cinco = 5
    uno = 1
    cambio = recibido - total
    faltante = total - recibido
    if cambio > 0:
        print(f"El cambio a dar es {cambio}")
    elif cambio == 0:
        print(f"No es necesario vuelto. El cliente ha pagado el total del producto")
    else:
        print(f"FALTA DINERO. El cliente no ha pagado el total del producto, le faltan {faltante} ")

#Programa Principal
totalcompra = int(input("Ingrese el precio de los articulos: "))
dinerorecibido = int(input("Ingrese el dinero pagado por el cliente: "))
calcularvuelto(totalcompra, dinerorecibido)