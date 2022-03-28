'''Reto 1: Números del revés
Un número del revés es un número entero que aparece igual cuando se gira 180 grados
Debes crear una función capaz de sacar los números de un rango que sean reversibles.
Input: La función recibirá dos valores. Estos dos valores representarán los límites superior e inferior de un rango.
Output: La función debe devolver los números y la cantidad total de números invertidos válidos dentro del rango de los
dos argumentos de entrada, incluidos los límites superior e inferior.
Detalle: El primer argumento siempre será menor que el segundo argumento, el rango siempre deberá ser válido.'''

def Check_Reversible(n):
    reversibleNumbers = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}
    for x, y in enumerate(n):
        if y not in reversibleNumbers:
            return False
        if reversibleNumbers[y] != n[-x-1]:
            return False
    return True
 
def GetReversibleNumbersAndTotal(Value1, Value2):
    res = 0
    arrayNumbers = []
    for i in range(Value1, Value2):
        if Check_Reversible(str(i)):
            arrayNumbers.append(i)
            res += 1
    return arrayNumbers, res
 
Value1 = int(0)
Value2 = int(0)

while Value1 >= Value2:
    Value1 = int(input("Value 1: "))
    Value2 = int(input("Value 2: "))
    if Value1 >= Value2:
        print("Value 1 must be lower than Value 2")
result = GetReversibleNumbersAndTotal(Value1, Value2)
    
print(f"The reversible numbers are: {result[0]}")
print(f"Total reversible numbers: {result[1]}")


'''Reto 2: El rompecabezas
Un rompecabezas deslizante es un rompecabezas combinado que desafía al jugador a deslizar piezas (con frecuencia planas)
a lo largo de ciertas rutas (generalmente en un tablero) para establecer una configuración final determinada.
Su objetivo para este reto es escribir una función que produzca una secuencia de movimientos de fichas que resuelva el
rompecabezas.
Input: Una matriz/lista n x n compuesta por valores enteros que van de 0 a n^2 - 1 (inclusive), que representa una
cuadrícula cuadrada. Ten en cuenta que siempre habrá una ficha vacía (representada por 0) para permitir el movimiento
de fichas adyacentes.
Output del algoritmo: Una matriz/lista compuesta por cualquiera (pero no necesariamente todos) de los números enteros de
1 a n^2 - 1, inclusive. Esto representa la secuencia de movimientos de fichas para una transición exitosa del estado
inicial sin resolver al estado resuelto. Si el rompecabezas no se puede resolver, devolverá None (Python).
Detalle: El input debe ser válido y el rango de valores para n es: 10 >= n >= 3'''



