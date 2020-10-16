
def nota_quices(codigo: str, nota1: int, nota2:int,nota3:int,nota4:int,nota5:int):
    
    menor=min(nota1,nota2,nota3,nota4,nota5)    
    promedio=(((nota1+nota2+nota3+nota4+nota5-menor)/4)*5)/100
    promedio=round(promedio,2)
    
    return "El promedio ajustado del estudiante "+str(codigo)+ " es: "+ str(promedio)


print(nota_quices("ABC0000",19,90,38,55,68))