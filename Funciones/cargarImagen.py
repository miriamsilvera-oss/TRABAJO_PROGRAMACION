# %%
#Función
def cargarImagen(ruta):
    """
    Carga una imagen termográfica desde un archivo CSV.
    Parámetro:
        ruta (str): Nombre o ruta completa del archivo CSV.
    Retorna:
        list[list[float]]: Matriz de temperaturas (lista de listas).
    """
    matriz = []                               # creamos una lista vacía para guardar todas las filas
    archivo = open(ruta, 'r')                 # abrimos el archivo CSV para leerlo
    for linea in archivo:                     # recorremos el archivo línea por línea
        filaTexto = linea.strip().split(',')  # sacamos espacios/saltos de línea y separamos por coma
        filaNumerica = []                     # lista vacía para guardar los números de esta fila
        for valor in filaTexto:               # recorremos cada valor de texto de la fila
            filaNumerica.append(float(valor)) # convertimos el texto a número y lo agregamos
        matriz.append(filaNumerica)           # agregamos la fila numérica a la matriz
    archivo.close()                           # cerramos el archivo
    return matriz                             # retornamos la matriz completa

# %%
#Prueba función
imagen = cargarImagen("paciente6/Imagen_0.csv") # cargamos la imagen del paciente 6
print(f"Filas: {len(imagen)}")                   # imprimimos cuántas filas tiene
print(f"Columnas: {len(imagen[0])}")             # imprimimos cuántas columnas tiene
print(f"Primer valor: {imagen[0][0]}")           # imprimimos el primer valor
print(f"Primera fila completa: {imagen[0]}")     # imprimimos toda la primera fila

#jenni