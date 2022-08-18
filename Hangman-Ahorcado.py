#=======================================================================
#	Juego del ahorcado
#=======================================================================
import random # Libreria importada.
#=======================================================================
PalabrasBasicas=["facil", "yelmo", "python", "divertido", "promocion", "murcielago", "aleatorio"]
PalabrasAvanzadas=["hipopotomonstrosesquipedaliofobia","electroencefalografista","musculo esternocleidomastoideo", "hidroclorotiazida", "presion hidraulica"]
#=======================================================================
def play_hangman(word, name):
	"""		Juego del ahorcado:
	
	- Su funcionamiento consiste en un bucle while que permanecera activo mientras la cantidad de vidas sea superior a cero.
	Caso contrario el juego finaliza con un mensaje en pantalla indicando su conclusion.
	
	- Se utilizan condicionales if para determinar si una letra se encuentra, o no, dentro de la palabra a descubrir.
	En caso de estar, la misma se agregara (o se desbloqueara) y en caso contrario se restara una vida del total 
	de vidas imprimiendo en la pantalla un mensaje de notificacion. Si se llegaran a consumir todas las vidas
	el programa entregara un mensaje de juego finalizado y el programa concluira.
	
	- play_hangman: [none->none] """
	
	joined="" # Caracter ingresado.
	life=6 # Cantidad de errores permitidos.
	listl=[] #lista de las letras que son erroneas que estan en la palabra.
	while life>0: # Bucle activo si las vidas son mayores a cero.
		
		failure=0 #Cantidad de errores.
		
		for letter in word: # letra en palabra:
			if letter in joined: # En caso de estarlo agregarla.
					print(letter, end="")
			else:
				print("-",end = "") # Caso contrario sumar un error.
				failure+=1 #Se agrega un error a la cantidad de errores.
		
		if failure==0: # Cantidad de errores en caso de ser cero.
			print("\t\t¡¡Felicidades",name.title()+", ganaste!!.\n\n")
			input("Press ENTER to exit.")
			break
		
		ingress=input("\n\tIngresa una letra:\t")
		joined+=ingress #Agrega caracter.
		
		if (ingress not in word): # Si la letra no esta en la palabra.
			if (ingress in listl):  # si la letra ya esta en la lista de errores muestra una advertencia
				print("la letra ya se ingreso,y es incorrecta")
			else:
				life-=1 # Restar una vida, al total de vida.
				listl.append(ingress)
				print("\tLa letra ingresada es incorrecta. Intenta con otra.")
				print("\tVidas restantes: "+str(life))
		
		if life==0:
			print("\t\tJuego finalizado. Te quedaste sin vidas.\n")
			input("Press ENTER to exit.")
	else:
		print("\tGracias por jugar.\n")
#=======================================================================
	# Centinela: (usado en el menu.)
#=======================================================================
def centinela():
	"""		Funcion Utilizado en menu. 
	- centinela: [none->number] 
	la funcion centinela nos permite que el usuario ingrese un numero y esta nos devuelve una opcion(number),
	que nos permitira en la funcion main elegir que modo de dificultad vamos a querer."""
	
	nmb=int(input("\n\tIngrese una opcion valida: (solo numeros)\t"))
	return nmb
#=======================================================================
def main():
	"""		Menu:
	- Interfase utilizada para elegir la dificultad de juego.
	- Consta de tres opciones:
								Opcion 1: Inicio de juego basico.
								Opcion 2: Inicio de juego avanzado.
								Opcion 3: Salir del juego. """
	
	print("\n\tJuego del ahorcado - Proyecto 01, Programacion II.\n")
	wb=PalabrasBasicas[random.randrange(len(PalabrasBasicas))]
	wa=PalabrasAvanzadas[random.randrange(len(PalabrasAvanzadas))]
	name=input("\tPor favor, ingrese su nombre:\t")
	print("\tSaludos",name.title()+". Bienvenido al juego del ahorcado.\n")
	
	print("\tElegir una de estas opciones:\t\n")
	print("\t\t 1. Nivel Basico.")
	print("\t\t 2. Nivel Avanzado.")
	print("\t\t 3. Salir del juego.")
	
	nmb=centinela()
	while nmb>=0:
		if 1==nmb:
			print("\tHaz elegido la dificultad: Basica.\n")
			print("\tConsejos:")
			print("\t\t- Comienza usando vocales.")
			print("\t\t- Recuerda todo el abecedario:")
			print("\tA,B,C,D,E,F,G,H,I,J,K,L,M,O,P,Q,R,S,T,U,V,W,X,Y,Z.\n")
			play_hangman(wb, name)
			break
		if 2==nmb:
			print("\tHaz elegido la dificultad: Avanzado.\n")
			print("\tConsejos:")
			print("\t\t- La incognita a descubrir podria, o no, contener una o mas palabras.")
			print("\t\t- Para descubrir si la incognita contiene mas palabras ingrese un espacio.\n")
			play_hangman(wa, name)
			break
		if 3==nmb:
			print("\tHaz elegido salir del juego. Hasta luego.\n")
			input("\t\t\t\t\tPress ENTER to exit.")
			break
		else:
			print("\n\tOpcion incorrecta vuelva a ingresar una opcion valida. Las opciones son 1,2 o 3.")
		nmb=centinela()
#=======================================================================
main() # Iniciar programa.
