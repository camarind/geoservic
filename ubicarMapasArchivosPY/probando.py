import os
import sys
from string import templates

#abriendo archivo archivos
filein = open('templates/probandopy.html')

#leyendo el archivos
src = templates(filein.read())

#inteccion de los datos del documento
nombreLugar = input(" Ingrece su un Lugar: ")
doc = input(" Ingrece Documento")

#Diccionario de datosd=
d={'nombreLugar':nombreLugar,'documento':doc,}

#sustituir valores en el html
result = src.substitute(d)

try:
    os.mkdir("probando")
    filein2= open('probando/'+str(doc)+'.html','w')
    filein2.writelines(result)
    print("Creando carpeta")
    print("Guardando archivo")
except OSError:
    if os.path.exists("probando"):
            filein2= open('probando/'+str(doc)+'.html','w')
            filein2.writelines(result)
            print("Guardando archivo")
while True:
    pregunta = input("presion N si quiere continuar y S si quiere salir")
if pregunta == "N":
    os.system(r"probando.py")
elif pregunta == "S":
    sys.exit()
