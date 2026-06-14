
#andrea
from Funciones.cargarImagen import cargarImagen
from Funciones.divideinFour import divideinFour
from Funciones.divideinTwo import divideinTwo
from Funciones.frequencyCounter import frequencyCounter
from Funciones.getMinvalue import getMinvalue
from Funciones.getMaxValue import getMaxValue
from Funciones.getDiffTemp import getDiffTemp
from Funciones.getMean import getMean
from Funciones.getMedian import getMedian
from Funciones.getStd import getStd
from Funciones.getVar import getVar
from Funciones.plotImage import plotImage
from Funciones.plotLine import plotLine
from Funciones.plotSeveralimages import plotSeveralimages

def main():
    umbral = 30
    imagenes_paciente6 =["Imagen_1000 (4).csv", "Imagen_2000 (4).csv","Imagen_3000 (4).csv","Imagen_4000 (4).csv", "Imagen_5000 (4).csv"]
    imagenes_paciente7 = ["Imagen_1000 (5).csv", "Imagen_2000 (5).csv","Imagen_3000 (5).csv","Imagen_4000 (5).csv", "Imagen_5000 (5).csv"]
    imagenes_paciente9 = ["Imagen_1000 (6).csv", "Imagen_2000 (6).csv","Imagen_3000 (6).csv","Imagen_4000 (6).csv", "Imagen_5000 (6).csv"]
    
    def analisisImagen(nombre_paciente,lista_imagen,umbral): 
        mean_izquierda = []
        mean_derecha = []

        minimos_izquierda = []
        minimos_derecha= []

        medianas_izquierda = []
        medianas_derecha = []

        varianza_izquierda = []
        varianza_derecha = []

        desvios_izquierda =[]
        desvios_derecha = []

        maximos_izquierda = []
        maximos_derecha = []
        for archivo in lista_imagen:
            imagen = cargarImagen(nombre_paciente, archivo)

            #dividir imagen en dos
            mitad_izq, mitad_der = divideinTwo(imagen)
            #temperatura media de cada mitad
            temp_media_iz = getMean(mitad_izq,umbral)
            temp_media_de = getMean(mitad_der,umbral)

            #agregamos las medias calculadas en la listas generadas anteriormente
            mean_izquierda.append(temp_media_iz)
            mean_derecha.append(temp_media_de)

     
            mediana_izq = getMedian(mitad_izq, umbral)
            mediana_der = getMedian(mitad_der, umbral)
            medianas_izquierda.append(mediana_izq)
            medianas_derecha.append(mediana_der)

            desvio_izq = getStd(mitad_izq, umbral)
            desvio_der = getStd(mitad_der, umbral)

            desvios_izquierda.append(desvio_izq)
            desvios_derecha.append(desvio_der)

            varianza_izq = getVar(mitad_izq, umbral) 
            varianza_der = getVar(mitad_der, umbral)
            varianza_izquierda.append(varianza_izq)
            varianza_derecha.append(varianza_der)

            minimo_izq = getMinvalue(mitad_izq, umbral) 
            minimo_der = getMinvalue(mitad_der, umbral)
            minimos_izquierda.append(minimo_izq)
            minimos_derecha.append(minimo_der)

            minimos_izquierda.append(minimo_izq)
            minimos_derecha.append(minimo_der)

            maximo_izq = getMaxValue(mitad_izq, umbral) 
            maximo_der = getMaxValue(mitad_der, umbral)

            maximos_izquierda.append(maximo_izq)
            maximos_derecha.append(maximo_der)
         #DIFERENCIAS DE TEMPERATURA
        diferencia = getDiffTemp(mean_izquierda, mean_derecha)

        return{
            "mean_izquierda": mean_izquierda,
            "mean_derecha": mean_derecha,
            "minimos_izquierda": minimos_izquierda,
            "minimos_derecha": minimos_derecha,
            "diferencia": diferencia,
        }
    
     # Ejecutar el análisis
    paciente_6 = analisisImagen("paciente6", imagenes_paciente6, umbral)
    paciente_7 =analisisImagen("paciente7",imagenes_paciente7,umbral)
    paciente_9 = analisisImagen("paciente9", imagenes_paciente9, umbral)
    
    #MOSTRAMOS RESULTADOS
    print("\nPACIENTE 6: ")
    print("Medias del lado izquierdo: ", paciente_6["mean_izquierda"])
    print("Medias del lado derecho: ", paciente_6["mean_derecha"])
    print("Diferencia de temperatura: ", paciente_6["diferencia"])
    print("Temperatura minima del lado izquierdo: ", paciente_6["minimos_izquierda"])
    print("Temperatura minima del lado derecho: ", paciente_6["minimos_derecha"])

    print("\nPACIENTE 7: ")
    print("Medias del lado izquierdo: ", paciente_7["mean_izquierda"])
    print("Medias del lado derecho: ", paciente_7["mean_derecha"])
    print("Diferencia de temperatura: ", paciente_7["diferencia"])
    print("Temperatura minima del lado izquierdo: ", paciente_7["minimos_izquierda"])
    print("Temperatura minima del lado derecho: ", paciente_7["minimos_derecha"])


    print("\nPACIENTE 9: ")
    print("Medias del lado izquierdo: ", paciente_9["mean_izquierda"])
    print("Medias del lado derecho: ", paciente_9["mean_derecha"])
    print("Diferencia de temperatura: ", paciente_9["diferencia"])
    print("Temperatura minima del lado izquierdo: ", paciente_9["minimos_izquierda"])
    print("Temperatura minima del lado derecho: ", paciente_9["minimos_derecha"])

if __name__ == "__main__":
     main()
