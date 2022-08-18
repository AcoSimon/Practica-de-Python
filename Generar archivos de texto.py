#-*-coding: utf-8-*-
#Clase ARCHIVOS
import codecs;

fout=open("prueba1.txt","w")
linea1= "Mas vale pájaro en mano, que cien volando!\n"
fout.write(linea1)
linea2= "El que no corre, vuela!\n"
fout.write(linea2)
linea3= "Pájaro que comió voló!\n"
fout.write(linea3)
fout.close()

listaDichos=["Mas vale pájaro en mano, que cien volando!\n","El que no corre, vuela!\n", "Pájaro que comió voló!\n", "Al mejor cazador, se le escapa la liebre!\n", "Aunque la  mona se vista de seda, mona queda!\n", "A buen entendedor, pocas palabras!\n"]

fout= open("prueba2.txt", "w")
for dicho in listaDichos:
	fout.write(dicho)
fout.close()

#El formato del dato para guardarlo en un archivo tiene que ser texto, es decir, <string> no se pueden guardar datos como tipo <int>.

fout= open("prueba3.txt", "w")
fout.write(str(45))
listaNumeros=[1,5,3,0,-1,0,100,-45]
for num in listaNumeros:
	fout.write(str(num))
fout.close()

#Separados por un espacio
fout= open("prueba4.txt", "w")
fout.write(str(45) + " ")
listaNumeros=[1,5,3,0,-1,0,100,-45]
for num in listaNumeros:
	fout.write(str(num)+ " ")
fout.close()

#Separados por un espacio
fout= open("prueba4.txt", "w")
fout.write(str(45) + " ")
listaNumeros=[1,5,3,0,-1,0,100,-45]
long=len(listaNumeros)
for i in range(long-1):
	fout.write(str(listaNumeros[i])+ " ")
fout.write(str(listaNumeros[long-1]))# separado para no insertar un delimitador innecesario
fout.close()



#Separados por comas

fout= open("prueba5.txt", "w")
fout.write(str(45)+ ",")
listaNumeros=[1,5,3,0,-1,0,100,-45]
long=len(listaNumeros)
for i in range(long-1):
	fout.write(str(listaNumeros[i])+ ",")
fout.write(str(listaNumeros[long-1]))# separado para no insertar un delimitador innecesario
fout.close()

#Uno por linea
fout= open("prueba6.txt", "w")
fout.write(str(45)+"\n")
listaNumeros=[1,5,3,0,-1,0,100,-45]
long=len(listaNumeros)
for i in range(long-1):
	fout.write(str(listaNumeros[i])+ "\n")
fout.write(str(listaNumeros[long-1]))# separado para no insertar un delimitador innecesario
fout.close()


## LECTURA

# Versión while
fin = codecs.open("martin-fierro.txt", "r", "utf8") #almacenado en utf-8
linea = fin.readline()
print(linea.rstrip())
while linea != '':
   # procesar linea
   linea = fin.readline()
   print(linea.rstrip())# para eliminar los espacios en blancos, incluídos los saltos de lineas
fin.close()

espera=input("")

# Versión for
fin = codecs.open("martin-fierro.txt", "r", "utf8")
#almacenado en utf-8
for linea in fin:
    print(linea.rstrip("\n"))# para eliminar los salto de linea
fin.close()

espera=input("")

# Imprimir número de linea y la linea del archivo
# Versión 1:
#almacenado en utf-8
fin = codecs.open("martin-fierro.txt", "r", "utf8")
i=1
for linea in fin:
    linea= linea.rstrip("\n") # para eliminar los salto de linea
    print("Linea ", i, ":", linea)
    i+=1
fin.close()
espera = input("")

#Versión 2: usando enumerate
fin = codecs.open("martin-fierro.txt", "r", "utf8")
for i, linea in enumerate(fin):
    linea= linea.rstrip("\n") # para eliminar los salto de linea
    print("Linea ", i, ":", linea)
fin.close()
espera = input("")

fout.close()
