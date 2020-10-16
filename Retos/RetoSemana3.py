def ruteo(distancias: dict, ruta_inicial: list) -> dict:
    """
    Funcion que retorna un dicionario con la mejor ruta y distancia a partir de una
    ruta_inicial dada y un diccionario de distancias
    """
    if(esValido(distancias)):
        rutaActual = ruta_inicial[1:-1]
        mejora = True
        home=ruta_inicial[0]
        distancia = calcularDistancia(distancias, rutaActual,home)
        
        rutaIntercambiada = rutaActual[:]
        # loop que se ejecuta hasta que no se encuntren mejores rutas
        while mejora:
            # se establece mejora a false ya que aun no se sabe si habrá una mejor ruta
            mejora = False
            # iteracion de las filas y columnas de la matriz
            for i in range(0, len(rutaActual)-1):
                for j in range(i+1, len(rutaActual)):
                    pareja = (rutaActual[i], rutaActual[j])
                    rutaIntercambiada = rutaActual[:]
                    rutaIntercambiada[j], rutaIntercambiada[i] = pareja

                    distanciaIntercambio = calcularDistancia(
                        distancias, rutaIntercambiada,home)

                    # Si encuentra una distancia menor, se actualiza mejorRutaTemporal
                    if distanciaIntercambio < distancia:
                        distancia = distanciaIntercambio
                        mejorRutaTemporal = rutaIntercambiada[:]
                        mejora = True
            # Si se encuentra una mejor ruta, se asigna a rutaActual
            # y esta sera la ruta de la siguiente iteracion
            if mejora:
                rutaActual = mejorRutaTemporal[:]

        # Se agregan los tramos iniciales y finales a la ruta
        # se asigna a ruta y distancia encontrados al diccionario de salida
        rutaActual.insert(0, home)
        rutaActual.append(home)
        ruta="-".join(rutaActual)
        mejorRuta = {"ruta": ruta, "distancia": distancia}

        return mejorRuta
    else:
        mensaje="Por favor revisar los datos de entrada."
        return mensaje

    

def calcularDistancia(distancias, ruta,home):
    """Funcion que retorna la distancia de una ruta, a partir de un diccionario de distancias
    """
    trayectos = []
    distancia = 0
    #se crea una lista de tuplas con los trayectos de la ruta
    for i in range(0, len(ruta)-1):
        trayectos.append((ruta[i], ruta[i+1]))

    #se recorre la ista de trayectos y se obtiene la distancia del diccionario a partir de la llave
    for i in trayectos:
        d = distancias[i]
        distancia += d
    #se sumas las distancias del primer y ultimo trayecto    
    distancia += distancias[(home, trayectos[0][0])]
    distancia += distancias[(trayectos[len(trayectos)-1][1], home)]

    return distancia

def esValido(distancias):
    """Funcion que valida si los valores de un diccionario dado sean todos positivos
    """
    for llave,valor in distancias.items():
        if llave[0]!=llave[1] and valor>0:
            valido=True
        elif valor==0 and llave[0]==llave[1]:
            valido=True                
        else:
            valido=False
            break
    return valido            

distancias = {('H', 'H'): 0, ('H', 'A'): 21, ('H', 'B'): 57, ('H', 'C'): 58, ('H', 'D'): 195, ('H', 'E'): 245, ('H', 'F'): 241,
              ('A', 'H'): 127, ('A', 'A'): 0, ('A', 'B'): 231, ('A', 'C'): 113, ('A', 'D'): 254, ('A', 'E'): 179, ('A', 'F'): 41,
              ('B', 'H'): 153, ('B', 'A'): 252, ('B', 'B'): 0, ('B', 'C'): 56, ('B', 'D'): 126, ('B', 'E'): 160, ('B', 'F'): 269,
              ('C', 'H'): 196, ('C', 'A'): 128, ('C', 'B'): 80, ('C', 'C'): 0, ('C', 'D'): 136, ('C', 'E'): 37, ('C', 'F'): 180,
              ('D', 'H'): 30, ('D', 'A'): 40, ('D', 'B'): 256, ('D', 'C'): 121, ('D', 'D'): 0, ('D', 'E'): 194, ('D', 'F'): 109,
              ('E', 'H'): 33, ('E', 'A'): 144, ('E', 'B'): 179, ('E', 'C'): 114, ('E', 'D'): 237, ('E', 'E'): 0, ('E', 'F'): 119,
              ('F', 'H'): 267, ('F', 'A'): 61, ('F', 'B'): 79, ('F', 'C'): 39, ('F', 'D'): 135, ('F', 'E'): 55, ('F', 'F'): 0}

ruta_inicial = ['H', 'A', 'B', 'C', 'D', 'E', 'F', 'H']

distancias2 = {('H', 'H'): 0, ('H', 'A'): 60, ('H', 'B'): 202, ('H', 'C'): 206, ('H', 'D'): 40, ('H', 'E'): 27,
               ('A', 'H'): 72, ('A', 'A'): 0, ('A', 'B'): 135, ('A', 'C'): 150, ('A', 'D'): 240, ('A', 'E'): 117,
               ('B', 'H'): 188, ('B', 'A'): 166, ('B', 'B'): 0, ('B', 'C'): 149, ('B', 'D'): 126, ('B', 'E'): 199,
               ('C', 'H'): 39, ('C', 'A'): 19, ('C', 'B'): 123, ('C', 'C'): 0, ('C', 'D'): 206, ('C', 'E'): 19,
               ('D', 'H'): 45, ('D', 'A'): 14, ('D', 'B'): 110, ('D', 'C'): 95, ('D', 'D'): 0, ('D', 'E'): 31,
               ('E', 'H'): 36, ('E', 'A'): 179, ('E', 'B'): 235, ('E', 'C'): 106, ('E', 'D'): 25, ('E', 'E'): 0}

ruta2 = ['H', 'B', 'E', 'A', 'C', 'D', 'H']

lista = ruta_inicial[1:-1]
# print(lista)
# print(calcularDistancia(distancias,lista))
#print(ruteo(distancias2, ruta2))
#print(ruteo(distancias, ruta_inicial))

#print(esValido(distancias))
print(ruteo({('BOG', 'BOG'): 0, ('BOG', 'MDE'): 21, ('BOG', 'PEI'): 57, ('BOG', 'SMR'): 58, ('BOG', 'CTG'): 195, ('MDE',
'BOG'): 127, ('MDE', 'MDE'): 0, ('MDE', 'PEI'): 231, ('MDE', 'SMR'): 113, ('MDE', 'CTG'): 254, ('PEI', 'BOG'): 153, ('PEI',
'MDE'): 252, ('PEI', 'PEI'): 0, ('PEI', 'SMR'): 56, ('PEI', 'CTG'): 126, ('SMR', 'BOG'): 196, ('SMR', 'MDE'): 128, ('SMR',
'PEI'): 80, ('SMR', 'SMR'): 0, ('SMR', 'CTG'): 136, ('CTG', 'BOG'): 30, ('CTG', 'MDE'): 40, ('CTG', 'PEI'): 256, ('CTG',
'SMR'): 121, ('CTG', 'CTG'): 0},['MDE', 'PEI', 'BOG', 'CTG', 'SMR', 'MDE']))