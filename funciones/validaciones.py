def validar_opcion(minimo: int, maximo: int) -> int:
    """La funcion valida entre dos numeros

    Args:
        minimo (int): El numero minimo
        maximo (int): El numero maximo

    Returns:
        Retorna la seleccion de dicho numero establecido entre los valores minimo y maximo
    """
    numero = input(f"Seleccione un numero entre [{minimo} y {maximo}]: ")
    if not numero.isdigit() or minimo > int(numero) or maximo < int(numero):
        return validar_opcion(minimo, maximo)
    return int(numero)