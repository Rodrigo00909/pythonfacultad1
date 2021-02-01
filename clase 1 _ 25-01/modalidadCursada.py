### 
###
###
### Requisitos de aprobación: Primer Parcial 04/02 y un TPO como segundo final que se entrega el . ES PROMOCIONABLE. Fecha final 23 de Febrero o 1 de Marzo
### Se pueden recuperar examenes, más que nada el primer parcial. En caso de recuperación será en una de la fecha de final.
### Todo el material estára en WEBCAMPUS.
### ESCUCHAR ALGO EN MIN 21

### El interprete toma linea por linea, las traduce y la ejecuta. Lee linea por linea.
### Para separar entre primera y segunda imprecion se pone end=" ", en este caso el espacio es el mismo espacio en blanco. De esta manera quedaran ambas lineas imprimidas en el mismo
### renglon

### Variables: Inicializarlas solo con letras, numeros y guion bajo. Nombres con sentido.

### Especificadores de conversion: porcentaje D y porcentaje F. D es para numeros enteros, F es para numeros con decimales:
### %6d, se escriben numeros
### %7.2f,
cant = 10
cant2 = 12.5
print("Cantidad",cant)
print("Cantidad: %5d" %cant)
### Le estamos diciendo a pytjon que queremos imprimir el contenido de la variable cant en 6 columnas. Cada digito en una columna.
print("Cantidad", cant2)
print("Cantidad: %7.2f" %cant2)
### la variable precio tiene 12.5, el .decimal cumple 4 espacios de pantalla en este caso 1=1 2=2 3=. 4=5
### con el 7.2 le decimos que quiero el numero impreso en 7 columnas con 2 decimales. Al hacer esto quedaria 12.50 en pantalla


### Puede escribirse un 0 delante del ancho para rellenar con ceros:
algo = 12
print("%04d" %algo)

### En python hay que convertir el texto enviado por string en numero en caso de que queramos hacer operaciones matematicas: n = int(input("Mnesaje"))

#### + Suma - Resta * Multiplicacion / División Real // División Entera (Diferencia: en entera se descartan los decimales) % Módulo o Resto de una division entera ** Potencias

### Esta resta: -2**2 se le considera - unario. Esto nos daria: -4 porque resuelve PRIMERO la potencia, y en segundo lugar aplica el - unario es decir el negativo en el 2.


### El positivo de un numero: modulo o valor absoluto no se cuanto: var = valor1 if codicion else valor2 => a = b if b >= 0 else -b

### Esta es una forma de devolver un numero positivo. Sirve para yo asegurarme de tener un numero positivo por mas que el usuario introduzca el numero negativo