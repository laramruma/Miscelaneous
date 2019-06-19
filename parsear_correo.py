import numpy as np
import csv
from email import message_from_file
import os
directory = ".\\"
files = []
import glob

for filepath in glob.iglob(('.\\Correos\\*.txt')):
    files.append(('').join(filepath))

print(files)
for i in range(len(files)):
	#Abrir archivo
	f = open(files[i], "r")
	mensaje = f.read()
	f.close()

	#Parseo del archivo
	mensaje_leido = mensaje.split('--_----------=_MCPart_')
	contenido = mensaje_leido[1].split('--------------------------------------------------')
	contenido.pop(0) #headers e informacion irrelevante para el proyecto
	contenido.pop(-2) #retirar informacion irrelevante para el proyecto
	contenido.pop(-1) #retirar informacion irrelevante para el proyecto

	#Guardar contenido en archivo

	for i in range(len(contenido)):
		seccion =  contenido[i].split('\n')
		seccion_join = ('_').join(seccion)
		seccion_por_paises = seccion_join.split('__')
		seccion_por_paises.pop(-1)
		nombre = seccion_por_paises[0]
		paises_csv_file = open(("Informacion\\"+nombre+".csv"), "a")
		salida = csv.writer(paises_csv_file, delimiter=" ", lineterminator=' ')
		for i in range(1,len(seccion_por_paises)):
			paises = seccion_por_paises[i].split('_')
			salida.writerows([paises])
			salida.writerows('\n')
		
		paises_csv_file.close()
		
	print("data loaded to files. Bye")
