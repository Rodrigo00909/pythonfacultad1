## De que se trata el  ZEN de python y analizarlo. 
### "" he contado 35 cabezas y 94 patas entre las gallinas y los conejos de mi granja. ¿Cuantos conejos y cuantas gallinas tengo?""

conejos = 35
gallinas = 0
resultado = False

while resultado != True:
    if conejos*4 + gallinas*2 == 94:
        resultado = True
    else:
        conejos-=1
        gallinas+=1
print(f"Hay {conejos} conejos y {gallinas} gallinas")

#conejos = 12
#gallinas = 23

## Numero de conejos y gallinas ya sabiendo cuantas cabezas y patas habia. El resultado de la operacion inicia en falso y cambiará cuando el resultado sea verdadero
## Para ser verdadero debe cumplir una condicion
## Condicion: multiplica la cantidad de conejos x4 (4 patas) y la cantidad de gallinas x2 sea igual al total de patas. Luego le resta 1 a los conejos para sumarle 1 a las gallinas
## Y asi mantener a la cantidad de animales en 35