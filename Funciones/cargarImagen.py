#SUGERENCIA QUE PUSO EL PROFE PARA LA PARTE DE CARGAR IMAGEN








"""def makeTable(datos:list, separador = " ", columnas_a_int = []):
    datos es una lista que contiene listas de un archivo con estructura
    separador es un string que sirve para separar los datos de cada fila y generar columnas
    
    Retorna una lista de lista. Convierte a numeros los dator que sean numericos
    columnas_a_int lista con las columnas a convertir en entero. Cada elemento de la lista es un entero indicando 
    que columna convertir
    tabla = []
    for fila in datos:
        datos_fila = fila.strip().split(separador)
        if len(columnas_a_int) > 0:
            for columna in columnas_a_int:
                datos_fila[columna-1] = int[datos_fila[columna -1]] if datos_fila[columna-1].isnumeric() else datos_fila[columna-1]

        tabla.append(datos_fila)
    return tabla
makeTable(datos,separador = " ,", columnas_a_int=[1,4,5]) """
