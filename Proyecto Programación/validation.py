def valInt(*args):
    if len(args) == 1 and type(args[0]) == int:
        return True
    elif len(args) == 2:
        if type(args[0]) == int and isinstance(args[1], (list, tuple)):
            #Verifica que en la tupla o lista no se agreguen str
            if type(args[1][0]) == str or type(args[1][1]) == str: 
                raise TypeError('El dato ingresado no es un número')
            elif len(args[1]) == 2 and args[1][0] < args[1][1]:
                if type(args[1]) == list:
                    #verifica que arg0 esté en el rango incluyendo los extremos
                    if args[1][0] <= args[0] <= args[1][1]: 
                        return True
                elif type(args[1]) == tuple:
                    #verifica que arg0 esté en el rango sin incluir los extremos
                    if args[1][0] < args[0] < args[1][1]: 
                        return True
            #verifica el orden del rango
            elif len(args[1]) != 2 or args[1][0] >= args[1][1]: 
                raise ValueError('El rango no está ordenado de forma creciente o tiene un tamaño desconsiderado')
        #verifica que args1 sea lista o tupla
        elif not isinstance(args[1], (list, tuple)): 
            raise TypeError('El rango no es una lista o tupla') 
    return False

def valFloat(*args):
    if len(args) == 1 and type(args[0]) == float:
        return True
    elif len(args) == 2:
        if type(args[0]) == float and isinstance(args[1], (list, tuple)):
            #Verifica que en la tupla o lista no se agreguen str
            if type(args[1][0]) == str or type(args[1][1]) == str:  
                raise TypeError('El dato ingresado no es un número') 
            elif len(args[1]) == 2 and args[1][0] < args[1][1]:
                if type(args[1]) == list:
                    #verifica que arg0 esté en el rango incluyendo los extremos
                    if args[1][0] <= args[0] <= args[1][1]: 
                        return True
                elif type(args[1]) == tuple:
                    #verifica que arg0 esté en el rango sin incluir los extremos
                    if args[1][0] < args[0] < args[1][1]:
                        return True 
            #verifica el orden del rango
            elif len(args[1]) != 2 or args[1][0] >= args[1][1]:
                raise ValueError('El rango no está ordenado de forma creciente o tiene un tamaño desconsiderado')
        #verifica que args1 sea lista o tupla
        elif not isinstance(args[1], (list, tuple)): 
            raise TypeError('El rango no es una lista o tupla') 
    return False

def valComplex(*args):
    if len(args) == 1 and type(args[0]) == complex:
        return True
    elif len(args) == 2:
        if type(args[0]) == complex and isinstance(args[1], (list, tuple)):
            #Verifica que en la tupla o lista no se agreguen str
            if type(args[1][0]) == str or type(args[1][1]) == str:
                raise TypeError('El dato ingresado no es un número') 
            elif len(args[1]) == 2 and args[1][0] < args[1][1]:
                if type(args[1]) == list:
                    #verifica que el modulo del argumento 1 esté en el rango
                    if args[1][0] <= ((args[0].real**2 + args[0].imag**2) ** (1/2)) <= args[1][1]:
                        return True
                elif type(args[1]) == tuple:
                    if args[1][0] < ((args[0].real**2 + args[0].imag**2) ** (1/2)) < args[1][1]:
                        return True
            #verifica el tamaño y el orden del rango
            elif len(args[1]) != 2 or args[1][0] >= args[1][1]:
                raise ValueError('El rango no está ordenado de forma creciente o tiene un tamaño desconsiderado')
        #verifica que el segundo argumento sea lista o tupla
        elif not isinstance(args[1], (list, tuple)):
            raise TypeError('El rango no es una lista o tupla')
    return False

#para la validacion del arg[2] == "value"
def bubbleSort(lista):
  for i in range(len(lista)):
    for j in range(0, len(lista) - i - 1):
        if lista[j] > lista[j+1]:
            lista[j],lista[j+1] = lista[j+1],lista[j]
  return lista

def valList(*args):
    if len(args) == 1 and type(args[0]) == list:
        return True
    elif len(args) == 3:
        if type(args[0]) == list and isinstance(args[1], (list, int)) and type(args[2]) == str:
            if args[2] == 'value':
                #primero verifica que la lista 1 y 2 tengan la misma cantidad de elementos
                if len(args[0]) == len(args[1]):
                    #ordena las listas con un bubble sort y luego verifica que tengan los mismos elementos
                    if bubbleSort(args[0]) == bubbleSort(args[1]):
                        return True
            elif args[2] == 'len':
                if len(args[0]) == args[1]:
                    return True
            else:
                raise ValueError('El tercer argumento debe ser "value" o "len"')   
        else:
            raise TypeError('El segundo argumento debe ser de tipo "int" o "list", el tercer argumento debe ser de tipo "str"')   
    return False
#Sofía Ochoa, José Camacaro