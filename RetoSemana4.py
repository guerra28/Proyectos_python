

def promedio_facultades(info: dict, contando_externos: bool = True) -> tuple:
    facultades = set()
    notas = {}
    # guarda la lista de los codigos de estudiantes usados para el calculo
    estudiantesUtilizados = set()
    correosUtilizados = []

    for estudiante in info.values():
        for materia in estudiante["materias"]:
            facultades.add(materia["facultad"])

    facultades = sorted(facultades)

    for facultad in facultades:
        notas[facultad] = []

    if contando_externos:
        for codigo, estudiante in info.items():
            for materia in estudiante["materias"]:
                if materia["retirada"] == "No":
                    try:
                        if materia["creditos"] >= 0:
                            notas[materia["facultad"]].append(
                                (materia["nota"], materia["creditos"]))
                            estudiantesUtilizados.add(int(codigo))
                    except:
                        return "Error numérico."
    else:
        for codigo, estudiante in info.items():
            codigo = str(codigo)
            if codigo[4:6] != 5:

                for materia in estudiante["materias"]:
                    try:

                        if materia["creditos"] != 0:
                            if materia["retirada"] == "No":

                                if materia["codigo"][:materia["codigo"].find("-")] == estudiante["programa"]:
                                    notas[materia["facultad"]].append(
                                        (materia["nota"], materia["creditos"]))
                                    estudiantesUtilizados.add(int(codigo))
                    except:
                        return "Error numérico."
                        

    for estudiante in estudiantesUtilizados:
        correosUtilizados.append(generarCorreo(info, estudiante))
    correosUtilizados.sort()

    promedio = calcularPromedio(notas)

    resultado = (promedio, correosUtilizados)
    return resultado


def calcularPromedio(notasTotales: dict):
    sumanotas = 0
    sumacreditos = 0
    promedios = {}
    for facultad, notas in notasTotales.items():
        try:
            for i in notas:
                sumanotas += i[0]*i[1]
                sumacreditos += i[1]

            promedios[facultad] = round(sumanotas/sumacreditos, 2)
            sumanotas = 0
            sumacreditos = 0
        except:
            return "Error numérico."

    return promedios


def generarCorreo(info: dict, codigo):
    # Funcion para generar el correo de los estudiantes
    nombres = info[codigo]["nombres"].split()
    apellidos = info[codigo]["apellidos"].split(", ")
    documento = str(info[codigo]["documento"])
    

    if len(nombres) == 1:
        correo = nombres[0][0]+apellidos[1][0]+"."+apellidos[0]+documento[-2:]
    else:
        correo = nombres[0][0]+nombres[1][0]+"."+apellidos[1]+documento[-2:]
    correo = quitarTildes(correo)
    return correo


def quitarTildes(cadena: str) -> str:
    # Funcion para quitar acentos y mayusculas
    a, b = 'áéíóúüñÁÉÍÓÚÜÑ', 'aeiouunAEIOUUN'
    sinTildes = cadena.translate(cadena.maketrans(a, b))
    return sinTildes.lower()
