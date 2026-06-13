# función dividir imagen en dos partes iguales
imagen = [[28.5, 31.2, 29.8, 32.1],
          [34.5, 33.7, 31.8, 30.2],
          [34.5, 32.5, 30.1, 31.4]]

def divideInTwo(imagen):
    """Divide la imagen en dos mitades iguales a la mitad de las columnas.
    Retorna dos matrices: cuadrante derecho y cuadrante izquierdo."""
    mitad = len(imagen[0]) // 2       # calculamos la mitad de las columnas
    mitad_derecha = []                       # lista vacía para el cuadrante derecho
    mitad_izquierda = []                     # lista vacía para el cuadrante izquierdo
    for fila in imagen:                # recorremos cada fila de la imagen
        mitad_derecha.append(fila[:mitad])   # tomamos la primera mitad de la fila
        mitad_izquierda.append(fila[mitad:]) # tomamos la segunda mitad de la fila
    return mitad_derecha, mitad_izquierda          # retornamos los dos cuadrantes

# prueba función
if __name__ == "__main__":
    derecha, izquierda = divideInTwo(imagen)  # llamamos la función
    print("Izquierda\t\tDerecha")
    for i in range (len(izquierda)):
        print(izquierda[i], "\t", derecha[i])          # imprimimos cuadrante izquierdo y derecho

#andrea