# funcion dividir imagen en dos parte iguales Implementar una función que divida una imagen termográfica en dos mitades o cuadrantes iguales a la
#  mitad de las columnas. La figura 1 muestra un ejemplo.
imagen = [[28.5, 31.2, 29.8, 32.1], 
          [34.5, 33.7,31.8,30.2],
          [34.5,32.5,30.1,31.4,] ]

def divideinTwo(imagen):
    """Divide la imagen en dos partes iguales a la mitad"""
    #fila y columna de la imagen
    filas = len(imagen[0]) # filas  de la image
    columnas = len(imagen[0]) # columnas de la imagen

