

from RetoSemana4 import *

'''
CONSIDERACIONES IMPORTANTES PARA LOS CORREOS ELECTRÓNICOS:
* No debe tener duplicados
* Debe estar completamente en minúsculas
* No debe tener acentos

EL PROMEDIO DE LA FACULTAD: 
* Debe reportarse redondeado a dos decimales
* No debe considerar las materias retiradas
* Si contando_externos es False, no debe considerar materias electivas ni vacacionales
'''

# Prueba 1:
'''
print(promedio_facultades({
					20170136837:{
								"nombres" : "Jorge Juan",
								"apellidos" : "Moreno, López",
								"documento" : 88481595,
								"programa" : "ARQU",
								"materias" : [
												{
												"facultad" : "Arquitectura",
												"codigo" : "ARQU-8218",
												"nota" : 4.49,
												"creditos": 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Arquitectura",
												"codigo" : "ARQU-2113",
												"nota" : 2.97,
												"creditos" : 2,
												"retirada" : "Si",
												},
												{
												"facultad" : "Arquitectura",
												"codigo" : "ARQU-5048",
												"nota" : 4.26,
												"creditos" : 0,
												"retirada" : "No",
												},
											]
								},
					20130225137:{
								"nombres" : "Sara Carolina",
								"apellidos" : "Gómez, Fernández",
								"documento" : 58770043,
								"programa" : "ARQD",
								"materias" : [
												{
												"facultad" : "Arquitectura",
												"codigo" : "ARQD-7738",
												"nota" : 3.36,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Arquitectura",
												"codigo" : "ARQD-9115",
												"nota" : 2.62,
												"creditos" : 1,
												"retirada" : "No",
												},
												{
												"facultad" : "Arquitectura",
												"codigo" : "ARQD-7698",
												"nota" : 1.59,
												"creditos" : 4,
												"retirada" : "Si",
												},
											]
								},
					20110274333:{
								"nombres" : "Carolina Paula",
								"apellidos" : "Ochoa, López",
								"documento" : 82364435,
								"programa" : "DIMD",
								"materias" : [
												{
												"facultad" : "Diseño",
												"codigo" : "DIMD-7972",
												"nota" : 3.15,
												"creditos" : 1,
												"retirada" : "No",
												},
											]
								},
					20200116062:{
								"nombres" : "Sara Camila",
								"apellidos" : "Martínez, Gómez",
								"documento" : 40079000,
								"programa" : "DIGR",
								"materias" : [
												{
												"facultad" : "Diseño",
												"codigo" : "DIGR-9331",
												"nota" : 4.0,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Diseño",
												"codigo" : "DIGR-3530",
												"nota" : 3.4,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Medicina",
												"codigo" : "MEDI-8548",
												"nota" : 3.1,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Medicina",
												"codigo" : "MEDI-9771",
												"nota" : 3.91,
												"creditos" : 2,
												"retirada" : "No",
												},
											]
								},
					20100379147:{
								"nombres" : "Jorge Juan",
								"apellidos" : "Romero, López",
								"documento" : 39344921,
								"programa" : "DIGR",
								"materias" : [
												{
												"facultad" : "Diseño",
												"codigo" : "DIGR-9511",
												"nota" : 2.38,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Diseño",
												"codigo" : "DIGR-6043",
												"nota" : 3.71,
												"creditos" : 0,
												"retirada" : "No",
												},
												{
												"facultad" : "Medicina",
												"codigo" : "MENF-1720",
												"nota" : 2.5,
												"creditos" : 3,
												"retirada" : "No",
												},
											]
								},
					20200126220:{
								"nombres" : "Sofia",
								"apellidos" : "Cordoba, Romero",
								"documento" : 90333325,
								"programa" : "IQUI",
								"materias" : [
												{
												"facultad" : "Ingenieria",
												"codigo" : "IQUI-4982",
												"nota" : 4.57,
												"creditos" : 4,
												"retirada" : "No",
												},
												{
												"facultad" : "Ingenieria",
												"codigo" : "IQUI-4982",
												"nota" : 2.8,
												"creditos" : 4,
												"retirada" : "No",
												},
												{
												"facultad" : "Ingenieria",
												"codigo" : "IQUI-6947",
												"nota" : 2.47,
												"creditos" : 3,
												"retirada" : "Si",
												},
												{
												"facultad" : "Ingenieria",
												"codigo" : "IQUI-2248",
												"nota" : 3.43,
												"creditos" : 3,
												"retirada" : "No",
												},
											]
								},
					20130271126:{
								"nombres" : "Gabriela",
								"apellidos" : "Alvarez, García",
								"documento" : 72857337,
								"programa" : "ARQU",
								"materias" : [
												{
												"facultad" : "Arquitectura",
												"codigo" : "ARQD-4963",
												"nota" : 3.15,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Arquitectura",
												"codigo" : "ARQU-2113",
												"nota" : 3.9,
												"creditos" : 2,
												"retirada" : "No",
												},
												{
												"facultad" : "Arquitectura",
												"codigo" : "ARQU-1221",
												"nota" : 4.37,
												"creditos" : 4,
												"retirada" : "No",
												},
											]
								},
					20160219974:{
								"nombres" : "Daniela Sara",
								"apellidos" : "Cuellar, Guitiérrez",
								"documento" : 80398132,
								"programa" : "IIND",
								"materias" : [
												{
												"facultad" : "Ingenieria",
												"codigo" : "IIND-3557",
												"nota" : 3.91,
												"creditos" : 1,
												"retirada" : "No",
												},
												{
												"facultad" : "Ingenieria",
												"codigo" : "IIND-5158",
												"nota" : 3.83,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Ingenieria",
												"codigo" : "IIND-7543",
												"nota" : 3.41,
												"creditos" : 3,
												"retirada" : "No",
												},
											]
								},
					20190264705:{
								"nombres" : "Julio Nicolas",
								"apellidos" : "Fernández, Ramírez",
								"documento" : 42697671,
								"programa" : "DIIN",
								"materias" : [
												{
												"facultad" : "Diseño",
												"codigo" : "DIIN-7888",
												"nota" : 4.68,
												"creditos" : 2,
												"retirada" : "No",
												},
											]
								},
					20150222512:{
								"nombres" : "Mateo Gabriel",
								"apellidos" : "Niño, Romero",
								"documento" : 12964051,
								"programa" : "DIMD",
								"materias" : [
												{
												"facultad" : "Diseño",
												"codigo" : "DIMD-3683",
												"nota" : 3.6,
												"creditos" : 2,
												"retirada" : "No",
												},
												{
												"facultad" : "Diseño",
												"codigo" : "DIMD-4014",
												"nota" : 3.15,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Diseño",
												"codigo" : "DIMD-1670",
												"nota" : 4.75,
												"creditos" : 2,
												"retirada" : "No",
												},
											]
								},
					}))
# Expected return:
# ({'Arquitectura': 3.81, 'Diseño': 3.58, 'Ingenieria': 3.63, 'Medicina': 3.08}, ['cp.lopez35', 'ds.guitierrez32', 'gg.alvarez37', 'jj.lopez21', 'jj.lopez95', 'jn.ramirez71', 'mg.romero51', 'sc.fernandez43', 'sc.gomez00', 'sr.cordoba25'])
'''
# Prueba 2:

print(promedio_facultades({
					20170116008:{
								"nombres" : "Sofia Natalia",
								"apellidos" : "Martinez, Alvarez",
								"documento" : 86056697,
								"programa" : "HAMO",
								"materias" : [
												{
												"facultad" : "Historia del Arte",
												"codigo" : "HAMO-3145",
												"nota" : 3.79,
												"creditos" : 4,
												"retirada" : "No",
												},
												{
												"facultad" : "Historia del Arte",
												"codigo" : "HAMO-1882",
												"nota" : 3.02,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Historia del Arte",
												"codigo" : "HAMO-4916",
												"nota" : 3.99,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Historia del Arte",
												"codigo" : "HAMO-9576",
												"nota" : 3.2,
												"creditos" : 1,
												"retirada" : "No",
												},
												{
												"facultad" : "Ingenieria",
												"codigo" : "IIND-7401",
												"nota" : 4.08,
												"creditos" : 2,
												"retirada" : "No",
												},
											]
								},
					20180181912:{
								"nombres" : "Julian Andres",
								"apellidos" : "Fernández, Gómez",
								"documento" : 38203099,
								"programa" : "ARQD",
								"materias" : [
												{
												"facultad" : "Diseño",
												"codigo" : "DIIN-4822",
												"nota" : 3.99,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Medicina",
												"codigo" : "MEDI-6559",
												"nota" : 3.09,
												"creditos" : 1,
												"retirada" : "No",
												},
											]
								},
					20170131506:{
								"nombres" : "Laura Camila",
								"apellidos" : "Cuellar, Pérez",
								"documento" : 15755411,
								"programa" : "MENF",
								"materias" : [
												{
												"facultad" : "Medicina",
												"codigo" : "MENF-7857",
												"nota" : 3.19,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Medicina",
												"codigo" : "MENF-1857",
												"nota" : 2.62,
												"creditos" : 1,
												"retirada" : "No",
												},
												{
												"facultad" : "Medicina",
												"codigo" : "MENF-1415",
												"nota" : 2.83,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Medicina",
												"codigo" : "MENF-1720",
												"nota" : 2.58,
												"creditos" : 3,
												"retirada" : "No",
												},
											]
								},
					20100240601:{
								"nombres" : "Andres Julian",
								"apellidos" : "Ochoa, Romero",
								"documento" : 81959788,
								"programa" : "IBIO",
								"materias" : [
												{
												"facultad" : "Medicina",
												"codigo" : "MEDI-7472",
												"nota" : 3.6,
												"creditos" : 0,
												"retirada" : "No",
												},
												{
												"facultad" : "Ingenieria",
												"codigo" : "IBIO-5465",
												"nota" : 2.58,
												"creditos" : 2,
												"retirada" : "Si",
												},
												{
												"facultad" : "Ingenieria",
												"codigo" : "IBIO-8357",
												"nota" : 4.69,
												"creditos" : 0,
												"retirada" : "No",
												},
												{
												"facultad" : "Diseño",
												"codigo" : "DIGR-9511",
												"nota" : 2.51,
												"creditos" : 3,
												"retirada" : "Si",
												},
												{
												"facultad" : "Ingenieria",
												"codigo" : "IBIO-3379",
												"nota" : 4.31,
												"creditos" : 3,
												"retirada" : "No",
												},
											]
								},
					20160386484:{
								"nombres" : "Julio",
								"apellidos" : "Sánchez, Fernández",
								"documento" : 95423746,
								"programa" : "HART",
								"materias" : [
												{
												"facultad" : "Historia del Arte",
												"codigo" : "HART-3008",
												"nota" : 2.83,
												"creditos" : 2,
												"retirada" : "No",
												},
												{
												"facultad" : "Historia del Arte",
												"codigo" : "HART-3008",
												"nota" : 2.53,
												"creditos" : 2,
												"retirada" : "No",
												},
												{
												"facultad" : "Historia del Arte",
												"codigo" : "HART-2620",
												"nota" : 4.06,
												"creditos" : 2,
												"retirada" : "No",
												},
											]
								},
					20190365550:{
								"nombres" : "Catalina Valentina",
								"apellidos" : "García, López",
								"documento" : 88933669,
								"programa" : "MENF",
								"materias" : [
												{
												"facultad" : "Medicina",
												"codigo" : "MENF-5278",
												"nota" : 3.45,
												"creditos" : 1,
												"retirada" : "No",
												},
												{
												"facultad" : "Medicina",
												"codigo" : "MENF-1857",
												"nota" : 4.56,
												"creditos" : 1,
												"retirada" : "No",
												},
												{
												"facultad" : "Medicina",
												"codigo" : "MENF-9835",
												"nota" : 3.93,
												"creditos" : 0,
												"retirada" : "No",
												},
												{
												"facultad" : "Medicina",
												"codigo" : "MENF-9442",
												"nota" : 4.46,
												"creditos" : 0,
												"retirada" : "No",
												},
											]
								},
					20150173830:{
								"nombres" : "Catalina Valentina",
								"apellidos" : "Fernández, Guitiérrez",
								"documento" : 36216549,
								"programa" : "DISE",
								"materias" : [
												{
												"facultad" : "Ingenieria",
												"codigo" : "ISIS-3520",
												"nota" : 2.71,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Diseño",
												"codigo" : "DISE-5596",
												"nota" : 4.7,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Diseño",
												"codigo" : "DISE-6981",
												"nota" : 2.79,
												"creditos" : 0,
												"retirada" : "No",
												},
												{
												"facultad" : "Diseño",
												"codigo" : "DISE-5596",
												"nota" : 2.51,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Diseño",
												"codigo" : "DISE-5161",
												"nota" : 2.36,
												"creditos" : 3,
												"retirada" : "No",
												},
											]
								},
					20100383099:{
								"nombres" : "Juan Pablo",
								"apellidos" : "Moreno, Cordoba",
								"documento" : 17911136,
								"programa" : "ARQD",
								"materias" : [
												{
												"facultad" : "Arquitectura",
												"codigo" : "ARQD-9115",
												"nota" : 4.18,
												"creditos" : 1,
												"retirada" : "No",
												},
												{
												"facultad" : "Arquitectura",
												"codigo" : "ARQD-6074",
												"nota" : 3.73,
												"creditos" : 3,
												"retirada" : "No",
												},
											]
								},
					20090198116:{
								"nombres" : "Sofia Gabriela",
								"apellidos" : "Diaz, Moreno",
								"documento" : 62587112,
								"programa" : "ICIV",
								"materias" : [
												{
												"facultad" : "Ingenieria",
												"codigo" : "ICIV-1157",
												"nota" : 2.45,
												"creditos" : 0,
												"retirada" : "No",
												},
												{
												"facultad" : "Ingenieria",
												"codigo" : "ICIV-7915",
												"nota" : 4.17,
												"creditos" : 1,
												"retirada" : "No",
												},
												{
												"facultad" : "Ingenieria",
												"codigo" : "ICIV-5962",
												"nota" : 4.49,
												"creditos" : 3,
												"retirada" : "No",
												},
											]
								},
					20190262931:{
								"nombres" : "Paula Natalia",
								"apellidos" : "Torres, Jiménez",
								"documento" : 18534577,
								"programa" : "HART",
								"materias" : [
												{
												"facultad" : "Historia del Arte",
												"codigo" : "HART-2081",
												"nota" : 4.43,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Historia del Arte",
												"codigo" : "HART-8458",
												"nota" : 4.77,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Historia del Arte",
												"codigo" : "HART-1258",
												"nota" : 3.15,
												"creditos" : 3,
												"retirada" : "No",
												},
											]
								},
					20190299456:{
								"nombres" : "Natalia Paula",
								"apellidos" : "Moreno, Alvarez",
								"documento" : 89771722,
								"programa" : "DIMD",
								"materias" : [
												{
												"facultad" : "Diseño",
												"codigo" : "DIMD-7322",
												"nota" : 4.27,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Diseño",
												"codigo" : "DIMD-5808",
												"nota" : 3.19,
												"creditos" : 0,
												"retirada" : "No",
												},
												{
												"facultad" : "Diseño",
												"codigo" : "DIMD-4470",
												"nota" : 2.26,
												"creditos" : 4,
												"retirada" : "Si",
												},
												{
												"facultad" : "Diseño",
												"codigo" : "DIMD-7972",
												"nota" : 3.66,
												"creditos" : 1,
												"retirada" : "No",
												},
											]
								},
					20150172603:{
								"nombres" : "Catalina Paula",
								"apellidos" : "Pérez, Diaz",
								"documento" : 59641117,
								"programa" : "IBIO",
								"materias" : [
												{
												"facultad" : "Ingenieria",
												"codigo" : "IBIO-8636",
												"nota" : 4.65,
												"creditos" : 1,
												"retirada" : "No",
												},
												{
												"facultad" : "Ingenieria",
												"codigo" : "IBIO-1999",
												"nota" : 2.52,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Ingenieria",
												"codigo" : "IBIO-3063",
												"nota" : 2.95,
												"creditos" : 4,
												"retirada" : "No",
												},
											]
								},
					20160197253:{
								"nombres" : "Julian Mateo",
								"apellidos" : "Jiménez, Fernández",
								"documento" : 41016120,
								"programa" : "MEDI",
								"materias" : [
												{
												"facultad" : "Medicina",
												"codigo" : "MEDI-9348",
												"nota" : 4.55,
												"creditos" : 4,
												"retirada" : "No",
												},
												{
												"facultad" : "Medicina",
												"codigo" : "MENF-9306",
												"nota" : 2.77,
												"creditos" : 2,
												"retirada" : "No",
												},
												{
												"facultad" : "Medicina",
												"codigo" : "MEDI-1836",
												"nota" : 3.66,
												"creditos" : 3,
												"retirada" : "No",
												},
											]
								},
					20160174103:{
								"nombres" : "Mateo Julio",
								"apellidos" : "Diaz, López",
								"documento" : 88132707,
								"programa" : "IBIO",
								"materias" : [
												{
												"facultad" : "Ingenieria",
												"codigo" : "IBIO-2104",
												"nota" : 4.55,
												"creditos" : 0,
												"retirada" : "No",
												},
												{
												"facultad" : "Ingenieria",
												"codigo" : "IBIO-3425",
												"nota" : 3.98,
												"creditos" : 4,
												"retirada" : "No",
												},
												{
												"facultad" : "Ingenieria",
												"codigo" : "IBIO-4686",
												"nota" : 4.97,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Ingenieria",
												"codigo" : "IBIO-9455",
												"nota" : 2.43,
												"creditos" : 0,
												"retirada" : "Si",
												},
											]
								},
					20150384070:{
								"nombres" : "Carolina Natalia",
								"apellidos" : "López, Gómez",
								"documento" : 33424549,
								"programa" : "DIMD",
								"materias" : [
												{
												"facultad" : "Diseño",
												"codigo" : "DIMD-7322",
												"nota" : 2.49,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Medicina",
												"codigo" : "MEDI-4101",
												"nota" : 3.14,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Diseño",
												"codigo" : "DIMD-8021",
												"nota" : 2.97,
												"creditos" : 4,
												"retirada" : "No",
												},
												{
												"facultad" : "Diseño",
												"codigo" : "DIMD-7470",
												"nota" : 4.77,
												"creditos" : 2,
												"retirada" : "No",
												},
											]
								},
					}, False ))
# Expected return:
# ({'Arquitectura': 3.84, 'Diseño': 3.37, 'Historia del Arte': 3.66, 'Ingenieria': 3.88, 'Medicina': 3.45}, ['aj.romero88', 'cn.gomez49', 'cp.diaz17', 'cv.guitierrez49', 'cv.lopez69', 'jf.sanchez46', 'jm.fernandez20', 'jp.cordoba36', 'lc.perez11', 'mj.lopez07', 'np.alvarez22', 'pn.jimenez77', 'sg.moreno12', 'sn.alvarez97'])


