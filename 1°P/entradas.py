"""
Modulo de entradas: funciones de ingreso y validacion de datos por teclado.
Cumple con las restricciones de no usar metodos de str ni excepciones.
"""


def es_numero_entero(cadena):
    """
    Verifica si una cadena representa un numero entero valido.
    Sin utilizar metodos de la clase str ni excepciones.

    Args:
        cadena (str): La cadena a evaluar.

    Returns:
        bool: True si es un numero entero valido, False en caso contrario.
    """
    resultado = True
    largo = len(cadena)

    if largo == 0:
        resultado = False
    else:
        inicio = 0
        if cadena[0] == '-':
            if largo == 1:
                resultado = False
            else:
                inicio = 1

        if resultado:
            i = inicio
            while i < largo:
                caracter = cadena[i]
                if caracter < '0' or caracter > '9':
                    resultado = False
                    i = largo
                i += 1

    return resultado


def convertir_a_entero(cadena):
    """
    Convierte una cadena que representa un entero valido a un tipo int.
    Asume que la cadena ya fue validada previamente.

    Args:
        cadena (str): Cadena validada.

    Returns:
        int: El numero entero convertido.
    """
    es_negativo = False
    inicio = 0
    if cadena[0] == '-':
        es_negativo = True
        inicio = 1

    numero = 0
    i = inicio
    largo = len(cadena)
    while i < largo:
        digito = ord(cadena[i]) - ord('0')
        numero = numero * 10 + digito
        i += 1

    if es_negativo:
        numero = -numero

    return numero


def ingresar_entero_valido(mensaje):
    """
    Solicita al usuario un numero entero no negativo por teclado y lo valida.
    No permite cadenas invalidas ni numeros negativos.

    Args:
        mensaje (str): Mensaje para solicitar el dato.

    Returns:
        int: Numero entero valido no negativo.
    """
    ingreso_valido = False
    numero_resultante = 0

    while not ingreso_valido:
        entrada = input(mensaje)
        if es_numero_entero(entrada):
            valor = convertir_a_entero(entrada)
            if valor >= 0:
                numero_resultante = valor
                ingreso_valido = True
            else:
                print("Error: No se permiten numeros negativos. Ingrese nuevamente.")
        else:
            print("Error: Ingrese un numero entero valido (ej. 150).")

    return numero_resultante
