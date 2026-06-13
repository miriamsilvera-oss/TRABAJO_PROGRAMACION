# andrea
# función que obtiene la temperatura media por encima de un umbral

imagen = [[28.5, 31.2, 29.8, 32.1],
          [34.5, 33.7, 31.8, 30.2],
          [34.5, 32.5, 30.1, 31.4]]

temperatura_umbral = 30.0  # solo consideramos temperaturas por encima de este valor

def getMean(imagen, temperatura_umbral):
    """
    Obtiene la temperatura media por encima de un umbral.
    Parámetros:
        imagen (list[list[float]]): Matriz de temperaturas.
        temperatura_umbral (float): Temperatura mínima a considerar.
    Retorna:
        float: Temperatura media encontrada.
    """
    sumatoria = 0                                # acumulador para sumar las temperaturas
    cantidad = 0                                 # contador de valores válidos
    for fila in imagen:                          # recorremos cada fila
        for temperatura in fila:                 # recorremos cada temperatura
            if temperatura > temperatura_umbral: # solo consideramos las que superan el umbral
                sumatoria = sumatoria + temperatura  # sumamos la temperatura
                cantidad = cantidad + 1              # contamos el valor
    media = sumatoria / cantidad                 # dividimos la suma por la cantidad
    return media                                 # retornamos la media

#Prueba de función 
if __name__ == "__main__":
    resultado = getMean(imagen, temperatura_umbral)
    print(f"Temperatura media: {resultado}")