from UTN_Heroes_Dataset.utn_pp import (
    get_original_matrix, mostrar_matriz_texto_tabla
)

from validaciones import (
    validar_opcion,
)

from funciones_app import (
    mostrar_menu, mostrar_matriz
)

matriz_concesionaria = get_original_matrix()

def concesionaria_app(matriz: list[list]) -> None:

    while True:

        mostrar_menu()
        opcion = validar_opcion(1, 9)

        match opcion:

            case 1:
                pass
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case 6:
                pass
            case 7:
                pass
            case 8:
                pass
            case 9:
                break

if __name__ == "__main__":
    concesionaria_app(matriz_concesionaria)