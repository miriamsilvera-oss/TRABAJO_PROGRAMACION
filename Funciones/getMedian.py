# función que obtiene la mediana de temperaturas por encima de un umbral

imagen = [[28.5, 31.2, 29.8, 32.1],
          [34.5, 33.7, 31.8, 30.2],
          [34.5, 32.5, 30.1, 31.4]]

temperatura_umbral = 30.0  # solo consideramos temperaturas por encima de este valor

def getMedian(imagen, temperatura_umbral):
    """
    Obtiene la mediana de temperaturas por encima de un umbral.
    Parámetros:
        imagen (list[list[float]]): Matriz de temperaturas.
        temperatura_umbral (float): Temperatura mínima a considerar.
    Retorna:
        float: Mediana de las temperaturas encontradas.
    """
    # paso 1: juntamos todas las temperaturas que superan el umbral
    valores = []
    for fila in imagen:                          # recorremos cada fila
        for temperatura in fila:                 # recorremos cada temperatura
            if temperatura > temperatura_umbral: # solo tomamos las que superan el umbral
                valores.append(temperatura)      # la agregamos a la lista

    # paso 2: ordenamos la lista de menor a mayor sin usar sorted()
    for i in range(len(valores)):
        for j in range(i + 1, len(valores)):
            if valores[i] > valores[j]:                          # si el actual es mayor al siguiente
                valores[i], valores[j] = valores[j], valores[i] # los intercambiamos

    # paso 3: calculamos la mediana
    n = len(valores)               # cantidad total de valores
    mitad = n // 2                 # posición del medio

    if n % 2 == 0:                 # si la cantidad es par
        mediana = (valores[mitad - 1] + valores[mitad]) / 2  # promedio de los dos del medio
    else:                          # si la cantidad es impar
        mediana = valores[mitad]   # el valor del medio exacto

    return mediana                 # retornamos la mediana

#Prueba de función 
if __name__ == "__main__":
    resultado = getMedian(imagen, temperatura_umbral)
    print(f"Mediana: {resultado}")
    
# jenni