import sys
from collections import deque
 
 
# Función de utilidad para devolver la precedencia del operador dado.
# Tenga en cuenta que mayor es la precedencia, menor es su valor
def prec(c):
 
    # Multiplicación y división
    if c == '*' or c == '/':
        return 3
 
    # Suma y resta
    if c == '+' or c == '-':
        return 4
 
    # Bitwise AND
    if c == '&':
        return 8
 
    # Bitwise XOR (exclusivo o)
    if c == '^':
        return 9
 
    # Bit a bit OR (inclusive o)
    if c == '|':
        return 10
 
    # agregue más operadores si es necesario
    return sys.maxsize        # para paréntesis de apertura '('
 
 
# Función de utilidad para verificar si un token dado es un operando
def isOperand(c):
    return ('a' <= c <= 'z') or ('A' <= c <= 'Z') or ('0' <= c <= '9')
 
 
# Función para convertir una expresión infija en una expresión posfija.
# Esta función espera una expresión infija válida
def infixToPostfix(infix):
 
    # Caja base
    if not infix or not len(infix):
        return True
 
    # crea una stack vacía para almacenar operadores
    s = deque()
 
    # crea una string para almacenar la expresión de sufijo
    postfix = ''
 
    # procesa la expresión infija de izquierda a derecha
    for c in infix:
        # Caso 1. Si el token actual es un corchete de apertura '(', empújelo
        # la stack
        if c == '(':
            s.append(c)
 
        # Caso 2. Si el token actual es un corchete de cierre ')'
        elif c == ')':
            # extrae tokens de la stack hasta el paréntesis de apertura correspondiente '('
            # Se elimina #. Agregue cada operador al final de la expresión de sufijo
            while s[-1] != '(':
                postfix += s.pop()
            s.pop()
 
        # Caso 3. Si el token actual es un operando, añádalo al final del
        # Expresión de sufijo
        elif isOperand(c):
            postfix += c
 
        # Caso 4. Si el token actual es un operador
        else:
            # eliminar operadores de la stack con mayor o igual precedencia
            # y añádalos al final de la expresión de posfijo
            while s and prec(c) >= prec(s[-1]):
                postfix += s.pop()
 
            # finalmente, empuje el operador actual en la parte superior de la stack
            s.append(c)
 
    # agrega cualquier operador restante en la stack al final de la expresión de postfijo
    while s:
        postfix += s.pop()
 
    # devuelve la expresión sufijo
    return postfix
 
 
if __name__ == '__main__':
 
    infix = '((8-())+)'
    postfix = infixToPostfix(infix)
    print(postfix)