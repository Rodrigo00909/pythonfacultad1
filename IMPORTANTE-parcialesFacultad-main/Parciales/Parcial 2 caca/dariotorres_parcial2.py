"""
El examen consiste en escribir un programa para imprimir un listado con las calles de CABA y los códigos postales que pertenecen a cada una, sin repetir 
ninguna calle ni ningún código dentro de la misma calle. El listado debe ordenarse alfabéticamente por calle, y los códigos postales de cada una deberán 
ordenarse de menor a mayor.
Formato CSV
Campos: Código Postal | Nombre de la calle o localidad | Altura inicial | Altura final | Localidad
Orden: Calle (alfabeticamente) - Cód postal (menor a mayor)
11 de septiembre: 1111, 2222, 3333
"""

#Programa principal
print("Bienvenido.")
print()
r = input("Quiere comenzar el programa? (S/N)")
if r.upper() == "S":
    try:
        listado = open("codpos.txt", "rt")
        for linea in listado:
            codp, calle, alti, altf, loc = linea.split(';')
            loc = loc.rstrip('\n')
            print(f"Calle: {calle:>5}: {codp}")
        print("La lectura del archivo ha sido exitosa.")
    except FileNotFoundError as mensaje:
        print("No se puede abrir el archivo:", mensaje)
    except OSError as mensaje:
        print("No se puede abrir el archivo:", mensaje)
    finally:
        try:
            listado.close()
        except NameError:
            pass
else:
    print("No iniciar programa.")

# Disculpe por el parcial profe: no estoy preparado y tampoco queria no entregar nada. Estudiaré el doble para el recuperatorio

