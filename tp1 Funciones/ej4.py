# 4. Un comercio de electrodomésticos necesita para su línea de cajas un programa que
# le indique al cajero el cambio que debe entregarle al cliente. Para eso se ingresan
# dos números enteros, correspondientes al total de la compra y al dinero recibido.
# Informar cuántos billetes de cada denominación deben ser entregados al cliente
# como vuelto, de tal forma que se minimice la cantidad de billetes. Considerar que
# existen billetes de $500, $100, $50, $20, $10, $5 y $1. Emitir un mensaje de error
# si el dinero recibido fuera insuficiente. Ejemplo: Si la compra es de $317 y se abona con $500, el vuelto debe contener 1 billete de $100, 1 billete de $50, 1 billete
# de $20, 1 billete de $10 y 3 billetes de $1.

def alcanza(total,pago):
    return pago>=total

def cambio(total,pago,denominacion):
    #uno por cada denominacion de billete solicitada... faltarian los horneros de 1000
    billete = [0,0,0,0,0,0,0]
    resto = pago-total
    
    for i in range(len(billete)):
        billete[i]= resto // denominacion[i]
        resto%=denominacion[i]
    return billete


def main():
        total = int(input('monto a cobrar: '))
        pago = int(input('monto de pago: '))
        
        if alcanza(total,pago):
            denominacion =[500,100,50,20,10,5,1]
            billete = cambio(total,pago,denominacion)
            
            print(f'El vuelto es de ${pago-total}')
            print('El cambio se recibe de la siguiente forma: ')
            for i in range(len(billete)):
                if billete[i]>0:
                    print(f'{billete[i]} billetes de ${denominacion[i]}')
                    
        else:
            print('el monto recibido no es suficiente...')
                    
if __name__=="__main__":
    main()