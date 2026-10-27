"""
Modulo de funciones: logica algoritmica y calculos del sistema electoral.
Cumple estrictamente con no usar sum(), max(), min(), ni retornos multiples.
"""


def limpiar_lista(lista):
    """
    Elimina todos los elementos de una lista utilizando el metodo pop().

    Args:
        lista (list): La lista que se va a vaciar.

    Returns:
        None
    """
    mientras_tenga_elementos = True
    while mientras_tenga_elementos:
        if len(lista) > 0:
            lista.pop()
        else:
            mientras_tenga_elementos = False
    return None


def calcular_total_votos(votos_partidos):
    """
    Calcula la suma total de votos de todos los partidos.
    Reemplaza la funcion predefinida sum().

    Args:
        votos_partidos (list): Lista con los votos de cada partido.

    Returns:
        int: La suma total de los votos.
    """
    total = 0
    i = 0
    cantidad = len(votos_partidos)
    while i < cantidad:
        total = total + votos_partidos[i]
        i = i + 1
    return total


def calcular_porcentaje(votos_partido, total_votos):
    """
    Calcula el porcentaje de votos que representa una cantidad respecto al total.

    Args:
        votos_partido (int): Votos del partido.
        total_votos (int): Total acumulado de votos.

    Returns:
        float: El porcentaje obtenido.
    """
    porcentaje = 0.0
    if total_votos > 0:
        porcentaje = (votos_partido / total_votos) * 100.0
    return porcentaje


def obtener_porcentajes_partidos(votos_partidos):
    """
    Genera una lista con el porcentaje de votos de cada partido.

    Args:
        votos_partidos (list): Lista con los votos por partido.

    Returns:
        list: Lista con los porcentajes de cada partido.
    """
    porcentajes = []
    total_votos = calcular_total_votos(votos_partidos)
    i = 0
    cantidad = len(votos_partidos)
    while i < cantidad:
        p = calcular_porcentaje(votos_partidos[i], total_votos)
        porcentajes.append(p)
        i = i + 1
    return porcentajes


def obtener_indices_menos_porcentaje(votos_partidos, porcentaje_limite):
    """
    Obtiene los indices de los partidos cuyo porcentaje es estrictamente menor al limite.

    Args:
        votos_partidos (list): Lista de votos por partido.
        porcentaje_limite (float): Limite de porcentaje para filtrar.

    Returns:
        list: Lista de indices de los partidos que cumplen la condicion.
    """
    indices_filtrados = []
    porcentajes = obtener_porcentajes_partidos(votos_partidos)
    i = 0
    cantidad = len(votos_partidos)
    while i < cantidad:
        if porcentajes[i] < porcentaje_limite:
            indices_filtrados.append(i)
        i = i + 1
    return indices_filtrados


def obtener_indices_mas_votos(votos_partidos, umbral_votos):
    """
    Obtiene los indices de los partidos cuyos votos superan un umbral determinado.

    Args:
        votos_partidos (list): Lista de votos por partido.
        umbral_votos (int): Cantidad minima de votos requerida.

    Returns:
        list: Lista de indices de los partidos que superan el umbral.
    """
    indices_filtrados = []
    i = 0
    cantidad = len(votos_partidos)
    while i < cantidad:
        if votos_partidos[i] > umbral_votos:
            indices_filtrados.append(i)
        i = i + 1
    return indices_filtrados


def calcular_promedio_general(votos_partidos):
    """
    Calcula el promedio de votos por partido entre todos los postulados.

    Args:
        votos_partidos (list): Lista de votos por partido.

    Returns:
        float: El promedio general de votos.
    """
    promedio = 0.0
    cantidad = len(votos_partidos)
    if cantidad > 0:
        total = calcular_total_votos(votos_partidos)
        promedio = total / cantidad
    return promedio


def obtener_indices_encima_promedio(votos_partidos):
    """
    Obtiene los indices de los partidos cuyos votos superan el promedio general.

    Args:
        votos_partidos (list): Lista de votos por partido.

    Returns:
        list: Lista de indices de los partidos por encima del promedio.
    """
    indices_filtrados = []
    promedio = calcular_promedio_general(votos_partidos)
    i = 0
    cantidad = len(votos_partidos)
    while i < cantidad:
        if votos_partidos[i] > promedio:
            indices_filtrados.append(i)
        i = i + 1
    return indices_filtrados


def obtener_indices_menos_votados(votos_partidos):
    """
    Identifica el o los partidos con la menor cantidad de votos (contempla empates).
    Reemplaza el uso de min().

    Args:
        votos_partidos (list): Lista de votos por partido.

    Returns:
        list: Lista con los indices de los partidos menos votados.
    """
    indices_minimos = []
    cantidad = len(votos_partidos)
    if cantidad > 0:
        minimo_votos = votos_partidos[0]
        i = 1
        while i < cantidad:
            if votos_partidos[i] < minimo_votos:
                minimo_votos = votos_partidos[i]
            i = i + 1

        j = 0
        while j < cantidad:
            if votos_partidos[j] == minimo_votos:
                indices_minimos.append(j)
            j = j + 1
    return indices_minimos


def requiere_segunda_vuelta(votos_partidos):
    """
    Determina si se requiere segunda vuelta electoral.
    Hay segunda vuelta si ningun partido supera el 50% de los votos (es decir, <= 50%).

    Args:
        votos_partidos (list): Lista de votos por partido.

    Returns:
        bool: True si hay segunda vuelta, False si hay un ganador con mas del 50%.
    """
    segunda_vuelta = True
    porcentajes = obtener_porcentajes_partidos(votos_partidos)
    i = 0
    cantidad = len(votos_partidos)
    while i < cantidad:
        if porcentajes[i] > 50.0:
            segunda_vuelta = False
            i = cantidad
        i = i + 1
    return segunda_vuelta


def obtener_index_ganador(votos_partidos):
    """
    Obtiene el indice del partido ganador que supero el 50% de los votos.

    Args:
        votos_partidos (list): Lista de votos por partido.

    Returns:
        int: Indice del ganador, o -1 si no hay ganador directo.
    """
    index_ganador = -1
    porcentajes = obtener_porcentajes_partidos(votos_partidos)
    i = 0
    cantidad = len(votos_partidos)
    while i < cantidad:
        if porcentajes[i] > 50.0:
            index_ganador = i
            i = cantidad
        i = i + 1
    return index_ganador


def cargar_vector_hardcodeado(votos_partidos):
    """
    Reemplaza la lista original de votos por la lista hardcodeada de 10 partidos.
    Utiliza limpiar_lista() para vaciar la lista original.

    Args:
        votos_partidos (list): Lista de votos original.

    Returns:
        None
    """
    limpiar_lista(votos_partidos)
    datos_hardcodeados = [888, 555, 60, 1850, 999, 777, 1400, 180, 2500, 60]
    i = 0
    cantidad = len(datos_hardcodeados)
    while i < cantidad:
        votos_partidos.append(datos_hardcodeados[i])
        i = i + 1
    return None
