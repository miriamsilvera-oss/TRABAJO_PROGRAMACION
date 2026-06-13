# función que obtiene la temperatura máxima por encima de un umbral

imagen = [[28.5, 31.2, 29.8, 32.1],
          [34.5, 33.7, 31.8, 30.2],
          [34.5, 32.5, 30.1, 31.4]]

temperatura_umbral = 30.0  # solo consideramos temperaturas por encima de este valor

def getMaxValue(imagen, temperatura_umbral):
    """
    Obtiene la temperatura máxima por encima de un umbral.
    Parámetros:
        imagen (list[list[float]]): Matriz de temperaturas.
        temperatura_umbral (float): Temperatura mínima a considerar.
    Retorna:
        float: Temperatura máxima encontrada.
    """
    primero = True                               # variable para asignar el primer valor válido
    for fila in imagen:                          # recorremos cada fila
        for temperatura in fila:                 # recorremos cada temperatura
            if temperatura > temperatura_umbral: # solo consideramos las que superan el umbral
                if primero:                      # si es el primer valor válido
                    maximo = temperatura         # lo asignamos como máximo
                    primero = False              # ya no es el primero
                elif temperatura > maximo:       # si encontramos uno mayor al máximo actual
                    maximo = temperatura         # actualizamos el máximo
    return maximo                                # retornamos la temperatura máxima

#Prueba de función 
if __name__ == "__main__":
    resultado = getMaxValue(imagen, temperatura_umbral)
    print(f"Temperatura máxima: {resultado}")
    
# jenni