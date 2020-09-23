import math

def Nota_quices(codigo: str, nota1: int, nota2:int,nota3:int,nota4:int,nota5:int):
    """ Nota Quices

    :Parámetros:
    codigo (str): codigo único alfanumérico del estudiante
    nota1 (int): Nota del primer quiz reto semestre (0 - 100)
    nota2 (int): Nota del segundo quiz del semestre (0 - 100)
    nota3 (int): Nota del tercer quiz del semestre (0 - 100)
    nota4 (int): Nota del cuarto quiz del semestre (0 - 100)
    nota5 (int): Nota del quinto quiz del semestre (0 - 100)
    Retorno:
    String: de la forma "El promedio ajustado del estudiante {codigo} es: {promedio}" dónde, el promedio se
    calcula eliminando la peor nota y se reporta con dos decimales utilizando la escala numérica de 0 a 5

    """
    tupla=(nota1,nota2,nota3,nota4,nota5)
    listaNotas= list(tupla)    #{nota1,nota2,nota3,nota4,nota5}
    
    menor=nota1

    if menor>nota2:
        menor=nota2
    if menor>nota3:
        menor=nota3
    if menor>nota4:
        menor=nota4
    if menor>nota5:
        menor=nota5

    listaNotas.remove(menor)
    
    promedio=sum(listaNotas)/4

    promedio=(5*promedio)/100

    promedioAjustado=redondear(promedio)

    print("El promedio ajustado del estudiante",codigo, "es:", promedioAjustado)
      
 
def redondear(numero):
    """ Redondear
    Recibe un numero flotante y lo redondea a dos decimales

    """
    numero=str(round(numero,3))
    
    entero,punto,decimal1,decimal2,decimal3 = numero[0], numero[1], numero[2], numero[3], numero[4]

    decimal3=int(decimal3)
    decimal2=int(decimal2)

    if decimal3>=5:
        decimal2+=1
    

    decimal3=str(decimal3)
    decimal2=str(decimal2)
    promedioAjustado=(entero+punto+decimal1+decimal2)

    return promedioAjustado




Nota_quices("ABC0000",5,14,76,91,5)