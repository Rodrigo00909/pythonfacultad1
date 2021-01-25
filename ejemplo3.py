## Imprimir los valores 1/x entre -3 y 3
x=-4
while x<3:
    x = x + 1
    if x == 0:
        continue
    print("%2d: %5.2f" %(x,1/x))

### x vale -4 y luego escribimos el while. Como x vale -4 la condicion es verdadera.
## Lo primero q hacemos es sumarle 1 a x, que sera -3. Preguntamos si es igual a 0. Como no lo es primimimos lo que dice el print. En la prox interaccion ese -3
### se convierte en -2 y asi, no pasara nada. Pero cuando se convierte en 0 no puedo llegar a la linea del print xq se me rompe el programa por intentar dividir por 0.
### El continue imprime que se ejecute el print(osea antes de que se rompa) y me devuelve al inicio del programa ignorando este ultimo error por 0. Ejecutaria el pint
### en todos los numeros menos el 0. 
## Vamos a imprimir 2 columnas: IZ: -3-2-1 y la columna de la DER: -0.33 -0.5 -1 Y Asi. A la IZ los valores de X y a la DER los valores de 1/x