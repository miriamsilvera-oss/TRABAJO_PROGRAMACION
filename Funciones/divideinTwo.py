# función dividir imagen en dos partes iguales
imagen = [[28.5, 31.2, 29.8, 32.1],
          [34.5, 33.7, 31.8, 30.2],
          [34.5, 32.5, 30.1, 31.4]]

def divideInTwo(imagen):
    """Divide la imagen en dos mitades iguales a la mitad de las columnas.
    Retorna dos matrices: cuadrante derecho y cuadrante izquierdo."""
    mitad = len(imagen[0]) // 2       # calculamos la mitad de las columnas
    derecha = []                       # lista vacía para el cuadrante derecho
    izquierda = []                     # lista vacía para el cuadrante izquierdo
    for fila in imagen:                # recorremos cada fila de la imagen
        derecha.append(fila[:mitad])   # tomamos la primera mitad de la fila
        izquierda.append(fila[mitad:]) # tomamos la segunda mitad de la fila
    return derecha, izquierda          # retornamos los dos cuadrantes

# prueba función
if __name__ == "__main__":
    derecha, izquierda = divideInTwo(imagen)  # llamamos la función
    print("Derecha:", derecha)                # imprimimos cuadrante derecho
    print("Izquierda:", izquierda)            # imprimimos cuadrante izquierdo

#andrea