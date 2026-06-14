
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
