# funcion dividir imagen en dos parte iguales Implementar una función que divida una imagen termográfica en dos mitades o cuadrantes iguales a la
#  mitad de las columnas. La figura 1 muestra un ejemplo.

imagen = [[28.5, 31.2, 29.8, 32.1], 
          [34.5, 33.7,31.8,30.2],
          [34.5,32.5,30.1,31.4,] ]

def divideinTwo(imagen):
    """Divide la imagen en dos partes iguales a la mitad"""
    #fila y columna de la imagen
    columnas = len(imagen[0]) # columnas de la imagen
    # mitad de las columnas de la imagen 
    mitad = columnas// 2
    #matriz izquierda y derecha vacia
    mitad_izq = []
    mitad_der = []
    for fila in imagen:
        mitad_izq.append(fila[:mitad]) # mitad izquierda de la imagen partida
        mitad_der.append(fila[mitad:]) # mitad derecha de la imagen partida


    return mitad_izq, mitad_der 

# prueba funcion
imagen_izq,imagen_der = divideinTwo(imagen)
print("Izquierda\t\tDerecha")
for i in range (len(imagen_izq)):
    print(imagen_izq[i], "\t", imagen_der[i])



