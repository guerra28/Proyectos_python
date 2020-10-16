

def prestamo(informacion: dict) -> dict:

    respuesta_prestamo = {
        "id_prestamo": informacion["id_prestamo"], "aprobado": False}

    if validaciones(informacion):

        respuesta_prestamo["aprobado"] = aprobado(informacion)

    else:
        print("Revise los datos ingresados, ha introducido un valor no permitido")

    return respuesta_prestamo


def validaciones(informacion: dict):
    if informacion["casado"] == "Si" or informacion["casado"] == "No":

        if informacion["educacion"] == "Graduado" or informacion["educacion"] == "No Graduado":

            if informacion["independiente"] == "Si" or informacion["independiente"] == "No":

                if informacion["historia_credito"] == 1 or informacion["historia_credito"] == 0:

                    if informacion["tipo_propiedad"] == "Urbano" or informacion["tipo_propiedad"] == "Rural" or informacion["tipo_propiedad"] == "Semiurbano":
                        valido = True
                    else:
                        valido = False
                else:
                    valido = False
            else:
                valido = False
        else:
            valido = False
    else:
        valido = False

    return valido


def aprobado(informacion: dict):

    aprobado = false
    casado = True if informacion["casado"] == "Si" else False
    historia_credito = informacion["historia_credito"]
    ingreso_codeudor = informacion["ingreso_codeudor"]
    ingreso_deudor = informacion["ingreso_deudor"]
    cantidad_prestamo = informacion["cantidad_prestamo"]
    dependientes = 3 if informacion["dependientes"] == "3+" else informacion["dependientes"]
    independiente = True if informacion["independiente"] == "Si" else False
    tipo_propiedad = informacion["tipo_propiedad"]
    graduado = True if informacion["educacion"] == "Graduado" else False

    if historia_credito == 1:
        if ingreso_codeudor > 0 and (ingreso_deudor/9) > cantidad_prestamo:
            aprobado = True
        else:
            if dependientes > 2 and independiente:
                if (ingreso_codeudor/12) > cantidad_prestamo:
                    aprobado = True
            else:
                if cantidad_prestamo < 200:
                    aprobado = True
    else:
        if independiente:

            if not(casado and dependientes > 1):
                if (ingreso_deudor/10) > cantidad_prestamo or (ingreso_codeudor/10) > cantidad_prestamo:
                    if cantidad_prestamo < 180:
                        aprobado = True
                    else:
                        aprobado = False
            else:
                aprobado= False
        else:
            if not(tipo_propiedad == "Semiurbano") and dependientes < 2:
                if graduado:
                    if (ingreso_codeudor/11) > cantidad_prestamo and (ingreso_deudor/11) > cantidad_prestamo:
                        aprobado = True
                else:
                    aprobado = False

            else:
                aprobado = False
    return aprobado


informacion = {
    "id_prestamo": "RETOS2_001",
    "casado": "No",
    "dependientes": 0,
    "educacion": "No Graduado",
    "independiente": "No",
    "ingreso_deudor": 3748,
    "ingreso_codeudor": 1668,
    "cantidad_prestamo": 110,
    "plazo_prestamo": 360,
    "historia_credito": 1,
    "tipo_propiedad": "Semiurbano"

}

informacion2 = {
    "id_prestamo": "RETOS2_002",
    "casado": "Si",
    "dependientes": "3+",
    "educacion": "No Graduado",
    "independiente": "Si",
    "ingreso_deudor": 500,
    "ingreso_codeudor": 2000,
    "cantidad_prestamo": 100,
    "plazo_prestamo": 360,
    "historia_credito": 1,
    "tipo_propiedad": "Semiurbano"

}

print(prestamo(informacion2))
