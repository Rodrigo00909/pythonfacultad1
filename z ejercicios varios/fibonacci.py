### Una sucesión normal significa 2*n o 2n. Es seria multiplicar un numero determinado por 2.
### Una sucesión fibonacci es un poco distinto. Consiste en que una serie de numeros naturales se suman de a 2 a partir de 0 y 1. Se realiza sumando siempre los ultimos 2 numeros
## Ejemplo tengo una serie de numeros dentro de un array. Para ir llenandolo como si fuera una sucesión fibonacci deberia crear un nuevo espacio en el array sumando los 2 ultimos lugares.
## Ejemplo: [0,1], para el tercer termino deberia sumar el indice 1 y 2: [0,1,1] para un cuarto termino deberia sumar el indice 2 y 3 xq son los ultimos [0,1,1,2] y asi.
## es INFINITO.

## Entonces: supongamos que tenemos esta sucesión fibonacci:
fib = [0,1,1,2,3,5,8,13,21,34]
## Y como puedo saber cual es el fibonacci del indice 4? Se construye sumando indice 3 y 2
if fib[3] + fib[2] == fib[4]:
    print(True)

fib[4] = fib[3] + fib[2]
print(fib[4])

## Fib de 3? Se construye sumando indice 2 y 1
fib[3] = fib[2] + fib[1]

### Un ejemplo de fibonacci en la vida real seria un árbol: Comienza con un tronco que se divide en ramas y las ramas en ramitas. Desde la punta, arriba de todo, del árbol
## tendré 2 ramitas, osea 1 y 1. Se unen, o salen, de una rama mas grande (1+1=2). Alado de esta rama normalmente hay otra ramita chiquita y entonces 
### 1(ramita chiquita) + 2(la rama sumada de recien) = 3(una nueva rama un poco mas gruesa). Y asi sucesivamente. Puedo buscar el ejemplo en google, hay una foto detallada.
### El sentido de esto: En la imagen del arbol, si me paro desde la posicion por ejemplo del 5: Esto me dira que tengo algunos caminos distintos: tengo 2 caminos para un lado y 
### 3 caminos para el otro lado. Este 2 y 3 son la suma de 5. Ahora si me paro en el 8 me dira que tengo 5 caminos para un lado y 3 caminos para el otro. Por otro lado 3+5 es 8.
### Entonces asi se forma, siempre con caminos varios y siempre de a 2, xq son 2 los terminos que se usan para dar el ultimo termino.
### Todo este proceso es una sucesión de fibonacci. La sucesión esta por todos lados. Los petalos de la margarita tb están formados por una sucesión fibonacci. Es decir tienen una
## Cantidad de petalos dados por la sucesión de fibonacci. Una margarita peude tener 21 o 34 petalos, y justamente estos numeros son dados en una sucesión de fibonacci.
## En los caracoles tambien esta la sucesión fibonacci. 