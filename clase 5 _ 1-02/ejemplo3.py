# Leer una frase, invertir las palabras que contiene (sin invertir las letras)
# y mostrarla cadena invertida 
frase = input("Ingrese una frase: ")

#Dividimos la frase en una lista de palabras
palabras = frase.split() # Con el método split la frase ingresada sera una lista, con cada palabra un elemento independiente de la lista

#Invertimos la lista con reverse()
palabras.reverse()

#Construimos la cadena a partir de la lista
frase = " ".join(palabras) # Tengo que volver a poner en forma de string a la lista invertida, para eso uso el join,y lo guardaré en la variable frase ya que no la volvi a usar mas
# el separador es un espacio
print(frase)
# Hay otra forma que seria sin usar join, pero con un for. 
#Tambien se puede usar un ciclo para concatenar
frase2 = "" # Cadena vacia
for palabra in palabras: # para cada palabra en la lista de palabras:
    frase2 = frase2 + palabra + " " #concatena de dicha palabra a fase 2 y le agregamos un espacio en blanco como separador
print(frase2) 
# Es un método parecido pero no es el mismo, ya que el for estaría dejando un espacio al final