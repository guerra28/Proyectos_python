import numpy as np



def displayInicialTriqui():
    for i in range(0,3):
        for j in range(0,3):
            print("|_",end="")
        print("|")

def displayTriqui(x,y,turno):
    for i in range(0,3):
        for j in range(0,3):
            if x==i and y==j and turno:
                print("|X", end="")
            else:
                if x==i and y==j and turno==False:
                    print("|O",end="")

                else:
                    print("|_",end="")
        print("|")

def jugarTriqui():
    turno=True
    displayInicialTriqui()
    matriz = np.zeros((3,3))   # Crear una matriz de todos los ceros
    
    
    for i in range(1): # iterador provisional
        tupla= tuple(input("Ingrese la casilla a jugar, ej: la casilla superior derecha es 1,3: "))
        x=int(tupla[0])-1
        y=int(tupla[2])-1
        displayTriqui(x,y,turno)
        turno=not(turno)

jugarTriqui()        