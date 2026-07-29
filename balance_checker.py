from stack import Stack
from tokenizer import tokenizar_basico

# simbolo de cierre -> simbolo de apertura que le corresponde
PARES = {")": "(", "]": "[", "}": "{"}
APERTURAS = set(PARES.values())
CIERRES = set(PARES.keys())


def validar_balanceo(expresion):
    """Valida el balanceo de parentesis/corchetes/llaves de una expresion.

    Devuelve una tupla (esta_balanceada, pasos), donde pasos es una lista
    de strings que describe, en orden, que se hizo con la pila.
    """
    pila = Stack()
    tokens = tokenizar_basico(expresion)
    pasos = []

    for token in tokens:
        if token in APERTURAS:
            pila.push(token)
            pasos.append(f"push '{token}' -> pila: {pila.to_list()}")

        elif token in CIERRES:
            if pila.is_empty():
                pasos.append(f"'{token}' no tiene apertura que lo espere -> pila vacia")
                return False, pasos

            tope = pila.pop()
            if tope != PARES[token]:
                pasos.append(f"'{token}' no hace match con '{tope}' -> pila: {pila.to_list()}")
                return False, pasos

            pasos.append(f"pop '{tope}' por '{token}' -> pila: {pila.to_list()}")

    esta_balanceada = pila.is_empty()
    if not esta_balanceada:
        pasos.append(f"quedaron simbolos sin cerrar en la pila: {pila.to_list()}")

    return esta_balanceada, pasos
