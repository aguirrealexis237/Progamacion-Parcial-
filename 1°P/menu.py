"""
Modulo de menu: controlador del flujo principal de opciones del programa.
"""

from entradas import ingresar_entero_valido, es_numero_entero, convertir_a_entero
from funciones import cargar_vector_hardcodeado, limpiar_lista
from salidas import (
    mostrar_todos_los_votos,
    mostrar_partidos_menos_porcentaje,
    mostrar_partidos_mas_votos,
    mostrar_partidos_encima_promedio,
    mostrar_partido_menos_votado,
    mostrar_verificacion_segunda_vuelta
)


def mostrar_menu_opciones():
    """
    Imprime en pantalla las opciones del menu principal.

    Returns:
        None
    """
    print("\n==================================================")
    print("      SISTEMA DE ELECCIONES - UTN FRA")
    print("==================================================")
    print(" 1. Cargar votos (5 partidos)")
    print(" 2. Mostrar listado general de votos")
    print(" 3. Partidos con menos del 10% de votos")
    print(" 4. Partidos con menos del 15% de votos")
    print(" 5. Partidos con menos del 20% de votos")
    print(" 6. Partidos con mas de 500 votos")
    print(" 7. Partidos con mas de 1000 votos")
    print(" 8. Partidos por encima del promedio general")
    print(" 9. Partido(s) menos votado(s)")
    print(" 10. Verificar segunda vuelta electoral (balotaje)")
    print(" 11. Cargar vector hardcodeado (10 partidos)")
    print(" 0. Salir")
    print("==================================================")
    return None


def ejecutar_menu():
    """
    Ejecuta la logica del menu principal y controla el flujo de la aplicacion.

    Returns:
        None
    """
    votos_partidos = []
    datos_cargados = False
    ejecutando = True

    while ejecutando:
        mostrar_menu_opciones()
        entrada_opcion = input(" Seleccione una opcion (0-11): ")

        if es_numero_entero(entrada_opcion):
            opcion = convertir_a_entero(entrada_opcion)

            if opcion == 0:
                print("\n Gracias por utilizar el sistema de elecciones. ¡Hasta luego!\n")
                ejecutando = False

            elif opcion == 1:
                limpiar_lista(votos_partidos)
                print("\n--- CARGA DE VOTOS DE ELECCIONES (5 PARTIDOS) ---")
                j = 0
                while j < 5:
                    letra = chr(ord('A') + j)
                    mensaje_prompt = f" Ingrese la cantidad de votos para el Partido {letra}: "
                    votos = ingresar_entero_valido(mensaje_prompt)
                    votos_partidos.append(votos)
                    j = j + 1

                datos_cargados = True
                print("\n [✓] Votos cargados exitosamente.")
                input("\n Presione ENTER para regresar al menu principal...")

            elif opcion == 11:
                cargar_vector_hardcodeado(votos_partidos)
                datos_cargados = True
                print(f"\n [✓] Vector hardcodeado cargado exitosamente ({len(votos_partidos)} partidos).")
                input("\n Presione ENTER para regresar al menu principal...")

            else:
                if opcion >= 2 and opcion <= 10:
                    if not datos_cargados:
                        print("\n [!] ACCESO DENEGADO: Debe cargar los votos primero usando la Opcion 1 o la Opcion 11.")
                        input("\n Presione ENTER para regresar al menu principal...")
                    else:
                        if opcion == 2:
                            mostrar_todos_los_votos(votos_partidos)
                        elif opcion == 3:
                            mostrar_partidos_menos_porcentaje(votos_partidos, 10.0)
                        elif opcion == 4:
                            mostrar_partidos_menos_porcentaje(votos_partidos, 15.0)
                        elif opcion == 5:
                            mostrar_partidos_menos_porcentaje(votos_partidos, 20.0)
                        elif opcion == 6:
                            mostrar_partidos_mas_votos(votos_partidos, 500)
                        elif opcion == 7:
                            mostrar_partidos_mas_votos(votos_partidos, 1000)
                        elif opcion == 8:
                            mostrar_partidos_encima_promedio(votos_partidos)
                        elif opcion == 9:
                            mostrar_partido_menos_votado(votos_partidos)
                        elif opcion == 10:
                            mostrar_verificacion_segunda_vuelta(votos_partidos)

                        input(" Presione ENTER para regresar al menu principal...")
                else:
                    print("\n [!] ERROR: Opcion fuera de rango. Ingrese un numero entre 0 y 11.")
                    input("\n Presione ENTER para continuar...")
        else:
            print("\n [!] ERROR: Entrada invalida. Debe ingresar un numero entero.")
            input("\n Presione ENTER para continuar...")

    return None
