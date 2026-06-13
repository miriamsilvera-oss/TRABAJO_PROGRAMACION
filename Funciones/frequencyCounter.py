# función que cuenta la frecuencia de cada temperatura en la imagen

imagen = [[31, 32, 32, 31],
          [30, 32, 32, 32],
          [30, 32, 32, 32],
          [30, 33, 33, 33]]

def frequencyCounter(imagen):
    """
    Cuenta la frecuencia de cada temperatura en la imagen termográfica.
    Parámetro:
        imagen (list[list[float]]): Matriz de temperaturas.
    Retorna:
        tempsValues (list): Temperaturas únicas ordenadas de menor a mayor.
        frequencyValues (list): Cantidad de veces que aparece cada temperatura.
    """
    tempsValues = []      # lista para guardar temperaturas únicas
    frequencyValues = []  # lista para guardar la frecuencia de cada temperatura

    for fila in imagen:               # recorremos cada fila de la imagen
        for temp in fila:             # recorremos cada temperatura de la fila
            if temp not in tempsValues:   # si la temperatura no está en la lista
                tempsValues.append(temp)  # la agregamos
                frequencyValues.append(1) # y su frecuencia empieza en 1
            else:
                # si ya está, buscamos su posición y sumamos 1 a su frecuencia
                indice = tempsValues.index(temp)
                frequencyValues[indice] += 1

    # ordenamos ambas listas de menor a mayor temperatura
    for i in range(len(tempsValues)):
        for j in range(i + 1, len(tempsValues)):
            if tempsValues[i] > tempsValues[j]:
                # intercambiamos temperaturas
                tempsValues[i], tempsValues[j] = tempsValues[j], tempsValues[i]
                # intercambiamos frecuencias también
                frequencyValues[i], frequencyValues[j] = frequencyValues[j], frequencyValues[i]

    return tempsValues, frequencyValues  # retornamos las dos listas

# prueba función
if __name__ == "__main__":
    tempsValues, frequencyValues = frequencyCounter(imagen)
    print("Temperaturas:", tempsValues)   # debería dar [30, 31, 32, 33]
    print("Frecuencias:", frequencyValues) # debería dar [3, 2, 8, 3]
    
    # jenni