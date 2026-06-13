#andrea
# función que obtiene la varianza de temperaturas por encima de un umbral
from getMean import getMean 

"""La varianza mide en este caso cuanto se alejan las temperaturas de la media
para calcularla necesitamos conocer:
* las temperaturas
* la media de las temperaturas
* la cantidad de temperaturas """

imagen = [[28.5, 31.2, 29.8, 32.1],
          [34.5, 33.7, 31.8, 30.2],
          [34.5, 32.5, 30.1, 31.4]]

temperatura_umbral = 30.0  # solo consideramos temperaturas por encima de este valor

def getVar(imagen, temperatura_umbral):
    """
    Obtiene la varianza de temperaturas por encima de un umbral.
    Parámetros:
        imagen (list[list[float]]): Matriz de temperaturas.
        temperatura_umbral (float): Temperatura mínima a considerar.
    Retorna:
        float: Varianza de las temperaturas encontradas.
        Se reutiliza la funcion para calcular la media
    """

    suma_cuadrados = 0
    contador = 0

    media = getMean(imagen, temperatura_umbral)
    # como media tiene una cadena de texto en su interior para CASO DEPURACION
    if isinstance(media,str):
        return media
# esto garantiza que si getMean ingresa al caso depuracion, el programa no ingresa al bucle y manda mensaje error 
# si getMean es un numero entonces ingresa al bucle for a continuacion 
    for fila in imagen:
        for temperatura in fila:
            if temperatura > temperatura_umbral:
                suma_cuadrados += (temperatura - media)**2
                contador += 1
    if contador == 0:
        return "Ninguna temperatura supero el umbral establecido, favor de cambiar el umbral "
    
    varianza = suma_cuadrados// contador

    return varianza
    
#Prueba de función 
if __name__ == "__main__":
    resultado = getVar(imagen, temperatura_umbral)
    print(f"Varianza: {resultado}")

