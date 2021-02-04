# Funciónes
def replacetext(string, word, replace):
  splitedString = string.split()
  replaced = 0
  i = 0
  for value in splitedString:
    if value == word:
      splitedString[i] = replace
      replaced += 1
    i += 1

  return [' '.join(splitedString), replaced]

# Programa principal

string = input('Ingrese una frase: ')
word = input('Ingrese la palabra que desea replazar: ')
replace = input('Ingrese una palabra para replazar la anterior: ')

repText = replacetext(string, word, replace);

print("Se remplazaron", str(repText[1]), "palabras")
print("El string resultante es:")
print(repText[0])