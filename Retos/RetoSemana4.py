
def promedio_facultades(info: dict, contando_externos: bool = True) -> tuple:
    """Funcion para calcular el promedio ponderado por facultad, retorna una tupla, donde
    el primer valor es un diccionario con los promedios de las facultades, y el segundo valor
    es una lista con los correos de los estudiantes utilizados en el calculo.

    """
    facultades = set()
    notas = {}
    promedio = {}
    # guarda la lista de los codigos de estudiantes usados para el calculo
    estudiantesUtilizados = set()
    correosUtilizados = []

    for estudiante in info.values():
        for materia in estudiante["materias"]:
            facultades.add(materia["facultad"])

    facultades = sorted(facultades)

    for facultad in facultades:
        notas[facultad] = [{"sumanotas": 0, "sumacreditos": 0}]

    if contando_externos:
        for codigo, estudiante in info.items():
            for materia in estudiante["materias"]:
                if materia["retirada"] == "No":

                    try:

                        if materia["creditos"] > 0:
                            notas[materia["facultad"]].append((materia["nota"], materia["creditos"]))
                            notas[materia["facultad"]][0]["sumanotas"] += (materia["nota"]*materia["creditos"])
                            notas[materia["facultad"]][0]["sumacreditos"] += materia["creditos"]
                            estudiantesUtilizados.add(codigo)
                    except:
                        return "Error numérico."
    else:
        for codigo, estudiante in info.items():
            codigo = str(codigo)
            if codigo[4:6] != 5:
                for materia in estudiante["materias"]:
                    if materia["retirada"] == "No":
                        try:

                            if materia["creditos"] > 0:
                                if materia["codigo"][:materia["codigo"].find("-")] == estudiante["programa"]:
                                    notas[materia["facultad"]].append((materia["nota"], materia["creditos"]))
                                    notas[materia["facultad"]][0]["sumanotas"] += (materia["nota"]*materia["creditos"])
                                    notas[materia["facultad"]][0]["sumacreditos"] += materia["creditos"]
                                    estudiantesUtilizados.add(int(codigo))
                        except:
                            return "Error numérico."

    for facultad, nota in notas.items():
        promedio[facultad] = round(
            nota[0]["sumanotas"]/nota[0]["sumacreditos"], 2)

    for estudiante in estudiantesUtilizados:
        correosUtilizados.append(generarCorreo(info, estudiante))
    correosUtilizados.sort()
    resultado = (promedio, correosUtilizados)
    return resultado


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