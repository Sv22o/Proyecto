import validation as val
import crypto as encriptado

valInt = val.valInt
print(valInt(4))
print(valInt(4.0))
print(valInt(4, (4,10)))
print(valInt(4, [3,9]))
print(valInt(4, [4,10]))
print(valInt(4, [10,4]))
print(valInt(4,5))
print(valInt(4, [5,10]))
print(valInt(4, ['a',2]))
print(valInt(4, [2,'a']))
print(valInt(4, ('a',2)))

valFloat = val.valFloat
print(valFloat(4.0))
print(valFloat(4))
print(valFloat(4.4, (4.4,10)))
print(valFloat(4.4, (4,10)))
print(valFloat(4.1,[4.1, 9.0]))
print(valFloat(4.2, [4,10]))
print(valFloat(4.4, [10,4]))
print(valFloat(4,5))
print(valFloat(4.0, [5,10]))
print(valFloat(4.0, ['a',2]))
print(valFloat(4.0,[2,'a']))
print(valFloat(4.0,('a',2)))

valComplex = val.valComplex
print(valComplex(3+4j))
print(valComplex(4.0))
print(valComplex(4))
print(valComplex(3+4j, (5,10)))
print(valComplex(3+4j, [5,10]))
print(valComplex(3+4j, [4,10]))
print(valComplex(3+4j, [10,4]))
print(valComplex(3+4j,5))
print(valComplex(3-4j, ['a',2]))
print(valComplex(3+4j, [2, 'a']))
print(valComplex(3+4j, ('a',2)))

valList = val.valList
print(valList([1,8,4]))
print(valList(3))
print(valList([1,8,7,3], [7,1,3,8], 'value'))
print(valList([1,8,7,3], [7,9,6,2], 'value'))
print(valList([1,8,7,3], [7,1], 'value'))
print(valList(6, 'hola', 'value'))
print(valList([1,9,3], 3, 'len'))
print(valList([1,9,3], 8, 'len'))
print(valList('hola', 3, 'len'))
print(valList([1,8,7,3], 'carro', 'value'))
print(valList([1,8,7,3], [7,9,2], 8))
print(valList([1,8,7,3], 7, 9))
print(valList([1,8,7,3], [9, 4, 2], 'azul'))
print(valList([1,8,7,3], 5, 'verde'))


cifrado = encriptado.cifrado
print(cifrado('hola'))
print(cifrado('hola mundo'))
print(cifrado('vamos a sacar veinte'))

descifrado = encriptado.descifrado
print(descifrado('19-53-37-2'))
print(descifrado('19-53-37-2-107-41-79-43-7-53'))
print(descifrado('83-2-41-53-71-107-2-107-71-2-5-2-67-107-83-11-23-43-73-11'))
#Sofía Ochoa, José Camacaro