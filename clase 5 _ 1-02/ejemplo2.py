# Reemplazar las vocales con tilde en una cadena de caracteres por sus equivalentes sin tilde

contilde = "áéíóúÁÉÍÓÚ"
sintilde = "aeiouAEIOU"
# Dos strings que tienen las vocales con tilde tanto em mayus como en minus, una con y otra sin tilde.
frase = input("Ingrese una frase: ")
nueva = ""
#Como los strings son inmutables no puedo guardar el nuevo dato en frase, para eso creo una nueva
for caracter in frase: #Recorremos laf rase con un for y como es un iterable no necesito subindices
   # Cada letra de la frase que ingreso el usuario irá a parar en caracter del for. 
    if caracter in contilde: # Preguntamos si el caracter introducido está dentro de la cadena contilde
        #En ese caso, significa que es una vocal con tilde q debe ser reemplazada por su equivalente
        #sin tilde.
        posicion = contilde.index(caracter) # averiguamos en q lugar de la cadena contilde se encuentra la letra (de caracter) y lo guardamos en esta variable.
        nueva = nueva + sintilde[posicion] # En nueva guardamos lo mismo que ya tenia + el contneido de la cadena sin tilde en el lugar q me indica el subindice posicion
        # Hemos reemplazado la o(x ejemplo) con tilde x la o sin tilde
    else: #En este caso significa que el caracter no está en la cadena con tilde por tanto no es una vocal con tilde
        nueva = nueva + caracter #Se agrega a la cadena nueva sin modificar su valor
print(nueva)