import random

def operAritmetic(val1, val2, operator):
    try:
        if operator == '+':
            return val1 + val2
        elif operator == '-':
            return val1 - val2
        elif operator == '*':
            return val1 * val2
        elif operator == '/':
            if val2 == 0:
                return 'Error: División por cero'
            else:
                return val1 / val2
        elif operator == 'sqrt':
            if val2 == 0:
                return 'Error: El índice de la raíz no puede ser cero'
            else:
                return val1 ** (1 / val2)
        elif operator == 'rand':
            return random.randint(val1, val2)
        else:
            return 'Error: Operador inválido'
    except Exception as e:
        print(f"Error: {e}")

def calcIva(cifra):
    return cifra * 19 / 100

