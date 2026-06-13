# función dividir imagen en cuatro cuadrantes iguales
imagen = [[28.5, 31.2, 29.8, 32.1],
          [34.5, 33.7, 31.8, 30.2],
          [34.5, 32.5, 30.1, 31.4],
          [33.1, 32.0, 31.5, 30.8]]

def divideInFour(imagen):
    """Divide la imagen en cuatro cuadrantes iguales.
    Retorna cuatro matrices: C1 (superior derecha), C2 (superior izquierda),
    C3 (inferior derecha), C4 (inferior izquierda)."""
    
    mitadCol = len(imagen[0]) // 2  # calculamos la mitad de las columnas
    mitadFil = len(imagen) // 2     # calculamos la mitad de las filas

    C1 = []  # cuadrante superior izquierdo
    C2 = []  # cuadrante superior derecho
    C3 = []  # cuadrante inferior izquierdo
    C4 = []  # cuadrante inferior derecho

    for i in range(mitadFil):           # recorremos la mitad superior de filas
        C1.append(imagen[i][:mitadCol]) # tomamos la mitad izquierda de cada fila
        C2.append(imagen[i][mitadCol:]) # tomamos la mitad derecha de cada fila

    for i in range(mitadFil, len(imagen)):  # recorremos la mitad inferior de filas
        C3.append(imagen[i][:mitadCol])     # tomamos la mitad izquierda de cada fila
        C4.append(imagen[i][mitadCol:])     # tomamos la mitad derecha de cada fila

    return C1, C2, C3, C4  # retornamos los cuatro cuadrantes

# prueba funcion
if __name__ == "__main__":
    C1, C2, C3, C4 = divideInFour(imagen)  # llamamos la función
    print("C1:", C1)                         # imprimimos cuadrante 1
    print("C2:", C2)                         # imprimimos cuadrante 2
    print("C3:", C3)                         # imprimimos cuadrante 3
    print("C4:", C4)                         # imprimimos cuadrante 4

#jenni

#filas = len(imagen[0]) # filas  de la imagen  por si te sirve