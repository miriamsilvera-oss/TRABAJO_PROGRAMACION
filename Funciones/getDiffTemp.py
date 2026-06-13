# andrea
# función que obtiene las diferencias de temperatura entre dos listas

temps1 = [31.2, 32.5, 30.1, 34.5]  # primera lista de temperaturas
temps2 = [30.1, 31.4, 29.8, 33.7]  # segunda lista de temperaturas

def getDiffs(temps1, temps2):
    """
    Obtiene las diferencias de temperatura entre dos listas.
    Parámetros:
        temps1 (list[float]): Primera lista de temperaturas.
        temps2 (list[float]): Segunda lista de temperaturas.
    Retorna:
        list[float]: Lista con las diferencias de temperatura.
        0: Si las listas no tienen la misma longitud.
    """
    # paso 1: verificamos que las dos listas tengan la misma longitud
    if len(temps1) != len(temps2):              # si las longitudes son distintas
        print("Error: las listas no tienen la misma longitud")  # imprimimos el error
        return 0                                # retornamos 0 como indica el profe

    # paso 2: calculamos las diferencias entre cada par de valores
    diferencias = []                            # lista vacía para guardar las diferencias
    for i in range(len(temps1)):                # recorremos cada posición de las listas
        diff = temps1[i] - temps2[i]            # calculamos la diferencia entre los dos valores
        diferencias.append(diff)                # agregamos la diferencia a la lista

    return diferencias                          # retornamos la lista de diferencias

if __name__ == "__main__":
    # prueba con listas de igual longitud
    resultado = getDiffs(temps1, temps2)
    print(f"Diferencias: {resultado}")

    # prueba con listas de distinta longitud
    temps3 = [31.2, 32.5]                       # lista más corta para probar el error
    resultado2 = getDiffs(temps1, temps3)
    print(f"Resultado con error: {resultado2}")