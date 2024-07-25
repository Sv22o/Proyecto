def cifrado(palabra):
    #el espacio al final del abecedario permite asignarle un numero al caracter de espacio
    abc = 'abcdefghijklmnñopqrstuvwxyz '
    lista_numeros = []
    for i in range(1,110):
        acumulador = 0
        for j in range(1,i+1):
            if i % j == 0:
                acumulador += 1
        if acumulador == 2:
            lista_numeros.append(i)

    cifrado=''
    for letra in palabra:
        for letrilla in range(len(abc)):
            if letra == abc[letrilla]:
                letra = str(lista_numeros[abc.index(letra)])
                cifrado= cifrado  + ("-") + (letra)
        if cifrado and cifrado[0] == '-':
            cifrado = cifrado[1:]
    return cifrado

def descifrado(numeros):
    abc = 'abcdefghijklmnñopqrstuvwxyz '
    lista_numeros = []
    for i in range(1,110):
        acumulador = 0
        for j in range(1,i+1):
            if i % j == 0:
                acumulador += 1
        if acumulador == 2:
            lista_numeros.append(i)

    descifrado=''
    lista_numeros2=list(numeros.split("-"))
    for numero in lista_numeros2:
        for numerito in lista_numeros:
            if numero==str(numerito):
                letra=abc[lista_numeros.index(int(numero))]
                descifrado= descifrado+letra
    return (descifrado)
#Sofía Ochoa, José Camacaro