"""Funcion que permite abrir archivos de tipo csv y
 leerlos linea por linea. Almacena cada linea en una lista nueva vacia y transforma los 
 valores alamacenados de un string a un float para poder trabajar y operar con ellos+
 a lo largo del programa """

def cargarImagen(paciente, nombreArchivo):
    ruta_arch = "Imagenes/" + paciente + "/" + nombreArchivo

    imagen = []
    try: #por si el archivo que se ingresa no existe 
        archivo = open(ruta_arch, "r")
    except FileNotFoundError:
        return "No se encontro el archivo ingresado. Favor de volver a intentar"

    for linea in archivo:
        valores = linea.split(",")
        fila = []
        for valor in valores:
            fila.append(float(valor))

        imagen.append(fila)
    archivo.close()

    return imagenGG











