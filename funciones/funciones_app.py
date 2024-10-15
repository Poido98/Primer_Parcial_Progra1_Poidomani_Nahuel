from UTN_Heroes_Dataset.utn_pp import (
    get_original_matrix, mostrar_matriz_texto_tabla
)

from app_main import matriz_concesionaria


def mostrar_menu() -> None:
    
    texto =\
    """
    1- Obtener existencias: para ello deberá crear una función que cargue la existencia de cada vehículo en todos 
    los garajes y mostrarlos.
    2- Calcular por cada garaje la cantidad total de unidades almacenadas entre todos los vehículos de la concesionaria.
    3- Datos completos del garaje que almacena menos unidades de vehículos.
    4- Máxima cantidad de unidades almacenadas entre todos los garajes.
    5- Obtener recaudación: para ello deberás crear una función que calcule la recaudación de cada garaje, teniendo en 
    cuenta su precio unitario y cantidad de unidades almacenadas en cada garaje.
    6- Cantidad de garajes que hayan almacenado 6 o más unidades de vehículos.
    7- Porcentaje de unidades de cada marca de vehículo sobre el total de vehículos almacenados entre todos los garajes
    de la sede matriz. Además mostrar todos los datos del garaje con el máximo porcentaje de vehículos almacenados.
    8- Generar un informe con la recaudación de cada garaje, ordenada de mayor a menor.
    9- Salir
    """
    print(texto)

def mostrar_matriz(matriz: list[list]) -> list[list]:
    for fila in matriz:
        for elemento in fila:
            print(elemento, end = "|")


def obtener_existencias(matriz: list[list]) -> None:
    mostrar_matriz(matriz_concesionaria)
