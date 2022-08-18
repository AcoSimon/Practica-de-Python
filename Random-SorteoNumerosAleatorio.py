#==========================================================================================|
# Bibliotecas importadas.                                               <<<<<<<<<<<<<<<<<<<|
#==========================================================================================V
import random # Biblioteca con funciones de aleatoriedad.
import time   # Biblioteca con funciones de control de tiempo.
#==========================================================================================|
# Centinela usado en la funcion random.                                 <<<<<<<<<<<<<<<<<<<|
#==========================================================================================V
def centinel_storage():
	"""Dato centinela usado en funcion RandomChoise."""
	#===================================================================
	nmb=len("\tPor favor, ingrese un dato:\t")-2
	#===================================================================
	print("\n\t"+"="*nmb)
	data=input("\tPor favor, ingrese un dato:\t-> ")
	print("\t"+"="*nmb,"\n")
	#===================================================================
	return str(data)
#==========================================================================================|
# Centinela usado en la funcion de menu.                                <<<<<<<<<<<<<<<<<<<|
#==========================================================================================V
def centinel_main():
	"""Dato centinela usado en funcion main."""
	#===================================================================
	nmb1=len("\n\t¿Quieres ingresar un dato?")-3
	#===================================================================
	print("\n\t"+"="*nmb1)
	questions=input("\t¿Quieres ingresar un dato?\n\t\t(y/n)\n\tIngrese su respuesta:\t-> ")
	print("\t"+"="*nmb1,"\n")
	#===================================================================
	return str(questions)
#=======================================================================
# Finalizar ejecucion de codigo activo.
#=======================================================================
def salir():
	"""Funcion usada para finalizar la ejecucion de codigo.
	salir: none->none"""
	#===================================================================
	input("\n\t\t\t\t\t\t\t\t\tPress ENTER to exit.")
#==========================================================================================|
# Borrar Informacion y souffle con elementos de la lista restantes.     <<<<<<<<<<<<<<<<<<<|
#==========================================================================================V
def delete_shuffle_info(listdata, result):
	#===================================================================
	delete=listdata.remove(result)
	#===================================================================
	RandomList=random.shuffle(listdata)
	#===================================================================
	return RandomList
#==========================================================================================|
# Funcion de aleatoriedad.                                              <<<<<<<<<<<<<<<<<<<|
#==========================================================================================V
def RandomChoise(data):
	#===================================================================
	return str(random.choice(data))
#==========================================================================================|
# Funcion de almacenamiento de informacion.                             <<<<<<<<<<<<<<<<<<<|
#==========================================================================================V
def storage():
	"""El trabajo de storage es almacenar los datos que el usuario
	ingresa para luego poder destinarlos a otra funcion.
	storage: none->list"""
	listdata=[]
	questions="y"
#=======================================================================
	while questions!="n" or questions!="N":
	#===================================================================
		if questions=="y" or questions=="Y":
			data=centinel_storage()
			listdata.append(data)
			print("\t\t",listdata)
			
	#===================================================================
		if questions=="n" or questions=="N":
			print(" ")
			print("\t\t"+"="*28)
			print("\t\tListado de datos ingresados:",listdata)
			print("\t\t"+"="*28)
			result=RandomChoise(listdata)
			delete=delete_shuffle_info(listdata, result)
			mix=random.shuffle(listdata)
			ccR=len(result)
			ccM1=len("\t\t|||||Resultado principal de la aleatoriedad: .|||||")
			ccMI=len("\n\t")
			cF=ccR+ccM1-ccMI
			F="="*cF
			print("\n\t\t"+F)
			print("\t\t|||||Resultado principal de la aleatoriedad: "+result+".|||||")
			print("\t\t"+F)
			print("\n\n\t\t"+"="*39)
			print("\t\t>>>>En caso de necesitar mas datos:<<<<")
			print("")
			print("\t\tSouffle de datos:",listdata)
			print("\t\t"+"="*17)
			print("\n\t\t\t\t  Gracias por su visita!!!!")
			print("\t\t\t\t\tVuelva pronto!")
			print("\n\n\n\t\t\t\t\t  V1.1.F0618.AS")
			salir()
			break
	#===================================================================
		if questions!="n" or questions!="N" and questions!="y" or questions!="Y":
			questions=centinel_main()
#==========================================================================================|
# Funcion principal, para inicio y ejecucion.                           <<<<<<<<<<<<<<<<<<<|
#==========================================================================================V
def body_main():
	"""Su utilidad es interrogar al usuario para saber si debe o no 
	invocar la funcion storage. Caso contrario finaliza el codigo.
	body_main: none->none"""
	questions=centinel_main()
#=======================================================================
	while questions!="n" or questions!="N":
	#===================================================================
		if questions=="y" or questions=="Y":
			storage()
			questions
			break
	#===================================================================
		if questions=="n" or questions=="N":
			print("\n\t\t\t\t  Gracias por su visita!!!!")
			print("\t\t\t\t\tVuelva pronto!")
			print("\n\n\n\t\t\t\t\t  V1.1.F0618.AS")
			salir()
			break
	#===================================================================
		else:
			questions=centinel_main()
#=======================================================================
def main():
	"""Funcion principal, se utiliza como inicio del codigo, de la misma
	 se deriva la funcion body_main.
	 main: none->none"""
	print("\t"+"="*85)
	print("\t|\t\t\tBienvenidos a \"opcion random\".\t\t\t\t    |\n\t|\t\t\t\t\t\t\t\t\t\t    |")
	print("\t|\tMi funcion es entregar un resultado usando la aleatoriedad como formula.    |")
	print("\t|Una vez entregados todos los datos comenzare con el \"sorteo\", en donde seleccionare|")
	print("\t|un dato aleatorio principal y, luego, con los demas datos me encargare de hacer un |")
	print("\t|souffle y mostrare una lista mezclada con todos esos datos restantes.              |")
	print("\t"+"="*85)
	body_main()
#==========================================================================================^
main()   # Ejecucion del codigo.                                        <<<<<<<<<<<<<<<<<<<|
#==========================================================================================|
