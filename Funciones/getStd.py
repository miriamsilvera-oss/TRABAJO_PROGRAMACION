# función que obtiene el desvío estándar de temperaturas por encima de un umbral

imagen = [[28.5, 31.2, 29.8, 32.1],
          [34.5, 33.7, 31.8, 30.2],
          [34.5, 32.5, 30.1, 31.4]]

temperatura_umbral = 30.0  # solo consideramos temperaturas por encima de este valor

def getStd(imagen, temperatura_umbral):
    """
    Obtiene el desvío estándar de temperaturas por encima de un umbral.
    Parámetros:
        imagen (list[list[float]]): Matriz de temperaturas.
        temperatura_umbral (float): Temperatura mínima a considerar.
    Retorna:
        float: Desvío estándar de las temperaturas encontradas.
    """
    # paso 1: juntamos todas las temperaturas que superan el umbral
    valores = []
    for fila in imagen:                          # recorremos cada fila
        for temperatura in fila:                 # recorremos cada temperatura
            if temperatura > temperatura_umbral: # solo tomamos las que superan el umbral
                valores.append(temperatura)      # la agregamos a la lista

    # paso 2: calculamos la media sin usar sum()
    sumatoria = 0
    for v in valores:                # recorremos cada valor
        sumatoria = sumatoria + v    # sumamos cada temperatura
    media = sumatoria / len(valores) # dividimos por la cantidad de valores

    # paso 3: calculamos la varianza
    sumatoria_dif = 0                                    # empezamos en 0
    for v in valores:                                    # recorremos cada valor
        diferencia = v - media                           # calculamos la diferencia con la media
        sumatoria_dif = sumatoria_dif + diferencia ** 2  # la elevamos al cuadrado y sumamos
    varianza = sumatoria_dif / len(valores)              # dividimos por la cantidad de valores

    # paso 4: el desvío estándar es la raíz cuadrada de la varianza
    std = varianza ** 0.5            # ** 0.5 es la raíz cuadrada sin usar numpy

    return std                       # retornamos el desvío estándar

#Prueba de función 
if __name__ == "__main__":
    resultado = getStd(imagen, temperatura_umbral)
    print(f"Desvío estándar: {resultado}")
    
# jenni