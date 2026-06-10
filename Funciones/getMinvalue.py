print(" getMinValue(): para obtener la temperatura mínima a partir de una matriz de temperaturas." \
" El mínimo valor debe encontrarse entre los valores por encima de una temperatura umbral")

imagen = [[28.5, 31.2, 29.8, 32.1], 
          [34.5, 33.7,31.8,30.2],
          [34.5,32.5,30.1,31.4] 
] # simulacion de la lista que obtendriamos de la imagen termica, cada valor representa la temperatura en esa posicion

temperatura_umbral = 30.0 # se solicta obtener el minimo por encima de una temperatura umbral
def getMinvalue(imagen, temperatura_umbral): # funcion recibe la imagen y la temepratura umbral
    primero = True #
    for fila in imagen: # recorremos filas de la lista
        for temperatura in fila: # recorremos cada temperatura de la fila
            if temperatura > temperatura_umbral: # hacemos la primera comparación para verificar si la temperatura de la lista supera el umbral
                if primero: # cuando aparece la primera temperatura que supera el umbral, se asigna a la variable minimo
                    minimo = temperatura # aqui se asigna el valor
                    primero = False # cambiamos el valor de primero para que no vuelva a entrar en esta condicion
                elif temperatura < minimo: # temperatura es menor que el minimo actual 
                    minimo = temperatura # se asigna el nuevo valor 
    return minimo # se regresa el valor minimo encontrado que supera el umbral


"""tenemos que inicializar el minimo pero no podemos hacer esto
minimo = 0 porque todas la temperaturas mayores al umbral son mayores a 0 por lo que se cumple en todos los casos
generamos la variable auxiliar primero para asignar el primer valor que supere el umbral y apartir del primer valor que cumple
comparamos con las temperaturas siguientes hasta encontrar el minimo"""


if __name__ == "__main__":
    print(getMinvalue(imagen, temperatura_umbral))
