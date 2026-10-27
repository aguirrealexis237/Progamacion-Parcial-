"""
Modulo de salidas: funciones para formatear e imprimir la informacion en terminal.
"""

from funciones import (
    calcular_total_votos,
    obtener_porcentajes_partidos,
    obtener_indices_menos_porcentaje,
    obtener_indices_mas_votos,
    calcular_promedio_general,
    obtener_indices_encima_promedio,
    obtener_indices_menos_votados,
    requiere_segunda_vuelta,
    obtener_index_ganador
)


def mostrar_encabezado(titulo):
    """
    Imprime un encabezado decorativo para los reportes.

    Args:
        titulo (str): Titulo de la seccion.

    Returns:
        None
    """
    print("\n==================================================")
    print(f"  {titulo}")
    print("==================================================")
    return None


def obtener_nombre_partido(index):
    """
    Retorna la identificacion legible de un partido politico segun su indice.

    Args:
        index (int): Indice del partido (0-indexed).

    Returns:
        str: Identificador del partido (ej. 'Partido A' o 'Partido 1').
    """
    letra = chr(ord('A') + index)
    nombre = f"Partido {letra} (ID: {index + 1})"
    return nombre


def mostrar_todos_los_votos(votos_partidos):
    """
    Muestra la lista completa de partidos con sus votos y porcentaje (Opcion 2).

    Args:
        votos_partidos (list): Lista de votos por partido.

    Returns:
        None
    """
    mostrar_encabezado("LISTADO GENERAL DE ELECCIONES")
    total_votos = calcular_total_votos(votos_partidos)
    porcentajes = obtener_porcentajes_partidos(votos_partidos)
    cantidad_partidos = len(votos_partidos)

    i = 0
    while i < cantidad_partidos:
        nombre = obtener_nombre_partido(i)
        votos = votos_partidos[i]
        pct = porcentajes[i]
        print(f" -> {nombre}: {votos} votos | {pct:.2f}%")
        i = i + 1

    print("--------------------------------------------------")
    print(f" Total de partidos postulados: {cantidad_partidos}")
    print(f" Total general de votos: {total_votos}")
    print("==================================================\n")
    return None


def mostrar_partidos_menos_porcentaje(votos_partidos, porcentaje_limite):
    """
    Muestra los partidos que obtuvieron menos de un porcentaje limite (Opciones 3, 4 y 5).

    Args:
        votos_partidos (list): Lista de votos por partido.
        porcentaje_limite (float): Porcentaje maximo para el filtro.

    Returns:
        None
    """
    mostrar_encabezado(f"PARTIDOS CON MENOS DEL {porcentaje_limite}% DE VOTOS")
    indices = obtener_indices_menos_porcentaje(votos_partidos, porcentaje_limite)
    cantidad_hallados = len(indices)

    if cantidad_hallados == 0:
        print(" [!] ERROR: No se encontraron partidos politicos que cumplan esta condicion.")
    else:
        total_votos = calcular_total_votos(votos_partidos)
        porcentajes = obtener_porcentajes_partidos(votos_partidos)
        porcentaje_acumulado = 0.0

        i = 0
        while i < cantidad_hallados:
            idx = indices[i]
            nombre = obtener_nombre_partido(idx)
            votos = votos_partidos[idx]
            pct = porcentajes[idx]
            porcentaje_acumulado = porcentaje_acumulado + pct
            print(f" -> {nombre}: {votos} votos | {pct:.2f}%")
            i = i + 1

        print("--------------------------------------------------")
        print(f" Porcentaje acumulado del grupo: {porcentaje_acumulado:.2f}%")
    print("==================================================\n")
    return None


def mostrar_partidos_mas_votos(votos_partidos, umbral_votos):
    """
    Muestra los partidos que superaron una cantidad de votos limite (Opciones 6 y 7).

    Args:
        votos_partidos (list): Lista de votos por partido.
        umbral_votos (int): Umbral minimo de votos.

    Returns:
        None
    """
    mostrar_encabezado(f"PARTIDOS CON MAS DE {umbral_votos} VOTOS")
    indices = obtener_indices_mas_votos(votos_partidos, umbral_votos)
    cantidad_hallados = len(indices)

    if cantidad_hallados == 0:
        print(" [!] ERROR: No se encontraron partidos politicos que cumplan esta condicion.")
    else:
        porcentajes = obtener_porcentajes_partidos(votos_partidos)
        suma_votos_grupo = 0

        i = 0
        while i < cantidad_hallados:
            idx = indices[i]
            nombre = obtener_nombre_partido(idx)
            votos = votos_partidos[idx]
            pct = porcentajes[idx]
            suma_votos_grupo = suma_votos_grupo + votos
            print(f" -> {nombre}: {votos} votos | {pct:.2f}%")
            i = i + 1

        promedio_grupo = suma_votos_grupo / cantidad_hallados
        print("--------------------------------------------------")
        print(f" (1) Suma de votos del grupo: {suma_votos_grupo}")
        print(f" (2) Cantidad de partidos en el grupo: {cantidad_hallados}")
        print(f" (3) Promedio de votos del grupo: {promedio_grupo:.2f}")
    print("==================================================\n")
    return None


def mostrar_partidos_encima_promedio(votos_partidos):
    """
    Muestra los partidos por encima del promedio general de la eleccion (Opcion 8).

    Args:
        votos_partidos (list): Lista de votos por partido.

    Returns:
        None
    """
    mostrar_encabezado("PARTIDOS POR ENCIMA DEL PROMEDIO GENERAL")
    promedio_general = calcular_promedio_general(votos_partidos)
    indices = obtener_indices_encima_promedio(votos_partidos)
    cantidad_hallados = len(indices)

    if cantidad_hallados == 0:
        print(" [!] ERROR: Ningun partido supera el promedio general.")
    else:
        porcentajes = obtener_porcentajes_partidos(votos_partidos)
        porcentaje_acumulado = 0.0

        i = 0
        while i < cantidad_hallados:
            idx = indices[i]
            nombre = obtener_nombre_partido(idx)
            votos = votos_partidos[idx]
            pct = porcentajes[idx]
            porcentaje_acumulado = porcentaje_acumulado + pct
            print(f" -> {nombre}: {votos} votos | {pct:.2f}%")
            i = i + 1

        print("--------------------------------------------------")
        print(f" (1) Promedio general de votos: {promedio_general:.2f}")
        print(f" (2) Porcentaje acumulado del grupo: {porcentaje_acumulado:.2f}%")
    print("==================================================\n")
    return None


def mostrar_partido_menos_votado(votos_partidos):
    """
    Muestra el o los partidos con menor cantidad de votos (Opcion 9).

    Args:
        votos_partidos (list): Lista de votos por partido.

    Returns:
        None
    """
    mostrar_encabezado("PARTIDO(S) MENOS VOTADO(S)")
    indices_minimos = obtener_indices_menos_votados(votos_partidos)
    cantidad_minimos = len(indices_minimos)
    porcentajes = obtener_porcentajes_partidos(votos_partidos)

    i = 0
    while i < cantidad_minimos:
        idx = indices_minimos[i]
        nombre = obtener_nombre_partido(idx)
        votos = votos_partidos[idx]
        pct = porcentajes[idx]
        print(f" -> {nombre}: {votos} votos | {pct:.2f}%")
        i = i + 1

    print("==================================================\n")
    return None


def mostrar_verificacion_segunda_vuelta(votos_partidos):
    """
    Evalua y muestra si corresponde o no segunda vuelta electoral (Opcion 10).

    Args:
        votos_partidos (list): Lista de votos por partido.

    Returns:
        None
    """
    mostrar_encabezado("EVALUACION DE SEGUNDA VUELTA ELECTORAL")
    hay_segunda_vuelta = requiere_segunda_vuelta(votos_partidos)

    if hay_segunda_vuelta:
        print(" RESULTADO: Debe realizarse una segunda vuelta electoral.")
    else:
        print(" RESULTADO: No debe realizarse una segunda vuelta electoral.")
        idx_ganador = obtener_index_ganador(votos_partidos)
        if idx_ganador != -1:
            nombre_ganador = obtener_nombre_partido(idx_ganador)
            votos_ganador = votos_partidos[idx_ganador]
            porcentajes = obtener_porcentajes_partidos(votos_partidos)
            pct_ganador = porcentajes[idx_ganador]
            print(f" -> Ganador: {nombre_ganador} con {votos_ganador} votos ({pct_ganador:.2f}%)")

    print("==================================================\n")
    return None
