#==================================================================================[a]=====
# Función cuenta regresiva:
#==================================================================================[a]=====
def cuentaregresiva(n):
    """ Diseño:
            Número: Natural.
        Signatura:
            Nat->None
        Propósito:
            Realiza una cuenta regresiva a partir de un numero
            natural dado, imprimiendo en pantalla un mensaje al llegar al valor cero.
    """
    if n==0:
        print ("Achis!!")
    else:
        print(n)
        cuentaregresiva(n-1)
#---------------------------------------------Invocacion de funcion------------------------
cuentaregresiva(5)
#==================================================================================[b]=====
# Función factorial:
#==================================================================================[b]=====
def factorial(n):
    """
        Diseño:
            Número: Natural.
        Signatura:
            Nat->Nat
        Propósito:
            Calcular en forma recursiva el factorial de un número natural dado.
        Ejemplos:
            factorial_pasos(5) = 120
            factorial_pasos(0) = 1
    """
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)
#---------------------------------------------Invocacion de funcion------------------------
factorial(5)
#==================================================================================[c]=====
# Función Fibonacci:
#==================================================================================[c]=====
def fibonacci(n):
    """
        Diseño:
            Número: Natural.
        Signatura:
            Nat->Nat
        Propósito:
            Calcular en forma recursiva el número de fibonacci de un número natural dado.
        Ejemplos:
            fibonacci(0) = 0
            fibonacci(1) = 1
            fibonacci(2) = 1
            fibonacci(8) = 21
    """
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
#---------------------------------------------Invocacion de funcion------------------------
fibonacci(5)
#==================================================================================[d]=====
# Función factorial con pasos intermedios para debugging:
#==================================================================================[d]=====
def factorial_pasos(n):
    """
        Diseño:
            Número: Natural.
        Signatura:
            Nat->Nat
        Propósito:
            Calcular el factorial de un número natural dado en forma recursiva, e imprimir
            los pasos intermedios en el proceso de cómputo a modo de debugging.
        Ejemplos:
            factorial_pasos(5) = 120
            factorial_pasos(0) = 1
    """
    print("La función factorial se invocó con n = ", n )
    if n == 0:
        return 1
    else:
        resultado = n*factorial_pasos(n-1)
        print("El resultado intermedio para ", n, " * factorial  -(", n-1, "): ", resultado)
        return resultado
#---------------------------------------------Invocacion de funcion------------------------
factorial_pasos(5)
#==========================================================================================    
