#Función
def cargarImagen(ruta):
    """
    Carga una imagen termográfica desde un archivo CSV.
    Parámetro:
        ruta (str): Nombre o ruta completa del archivo CSV.
    Retorna:
        list[list[float]]: Matriz de temperaturas (lista de listas).
    """
    matriz = []
    
    archivo = open(ruta,'r')
    
    for linea in archivo:
        filaTexto = linea.strip().split(',')
        filaNumerica = []
        
        for valor in filaTexto:
            filaNumerica.append(float(valor))
            
    matriz.append(filaNumerica)
      
    archivo.close()
    return matriz

# Prueba
from Funciones.cargarImagen import cargarImagen
imagen = cargarImagen("paciente6/Imagen_1000.csv")
print(f"Filas: {len(imagen)}")
print(f"Columnas: {len(imagen[0])}")
print(f"Primer valor: {imagen[0][0]}")