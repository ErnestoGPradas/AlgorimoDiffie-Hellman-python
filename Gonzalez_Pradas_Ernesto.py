#####################################################################
##Práctica 2:   Software para implementar el algoritmo de Diffie-Hellman
##Nombre:       Ernesto
##Apellidos:    González Pradas
##Asignatura:   Álgebra y Matemática Discreta

#Importamos la libreria random para poder generar nuestros exponentes de ambos usuarios de forma aleatoria como se pide en la práctica
import random
from colorama import Cursor, init, Fore, Back

#Función que nos permite hacer el cálculo mucho más rápido y menos costoso computacionalmente, le tenemos que pasar tres valores por entrada, base, exponente y número primo
def mod_exp(base, exponente, primo):
	x = 1
	y = base % primo
	b = exponente
    #Al estar hecho en python sustituimos el for planteado para el lenguaje C a un while en el que simplemente comprobamos que el exponente sea mayor que 0
	while (b > 0):
		if ((b % 2) == 0):  # Si la base es par 
			y = (y * y) % primo
			b = b / 2
		else:
			x = (x * y) % primo
			b = b - 1
	return x

#Esta función ya es un poco friki pero es para darle un toque un poco más personal. Función que simula un envio de datos cargando un %. Simplemente usamos un bucle para
# contar de 0-100 y la función sleep para que parezca que está precesando los datos cada 0.01 segundos. Como se utiliza tanto para simular el envio de claves como para
# la simulación de la clave final se le pasa también dos parametros que son enviar y generar siendo ambos booleanos (si enviar = 1 significa que estamos enviando claves 
# si generar = 1 las estamos generando). Usamos la libreria colorama para darle color a la salida por consola (carga de porcentaje en amarillo y resultado en verde)
def enviarGenerar_datos(usuario1, usuario2, enviar, generar):
    from time import sleep
    init()
    if enviar == 1:
        print("Enviando Clave del Usuario", usuario1,  "al Usuario", usuario2 )
    if generar == 1:
        print("Generando Clave final para el usuario", usuario1, " ")
    for arch in range(101):
        sleep(0.01)
        print(Cursor.UP(1)+Cursor.FORWARD(42)+Fore.YELLOW+str(arch),"%")
    if enviar == 1:
        print(Cursor.UP(0) +Fore.GREEN + "----------------------> 'Enviado'"+Fore.RESET)
    if generar == 1:
        print(Cursor.UP(0) +Fore.GREEN + "..............'Hecho!'"+Fore.RESET)

#Valores por defecto, nuestro número primo p y la base g
p = 761
b = 6

#Realizamos un pequeño menú interactivo para nuestro simulador del Laborario con colorines
print(Fore.RED + "**********Bienvenido al Simulador del Laboratorio Diffie-Hellman**********"+Fore.RESET)
print()
print(Fore.MAGENTA +"Por favor, seleccione el número de la opción que quiere realizar:")
print()
print("1.- Probar con el número Primo por defecto (761) y la Base (6)")
print()
print("2.- Introduzca su propio número Primo y Base"+Fore.RESET)
print()
valor_Menu = int(input("Introduzca un valor del Menú: "))

#En caso de elegir la opción número 2 del menú, introduccimos por teclado nuestro número primo y nuestra base para realizar los cálculos
if valor_Menu == 2:
    p = int(input("Introduzca un número Primo: "))
    b = int(input("Introduzca una Base: "))

#Generamos de manera aleatoria el exponente para el Usuario A utilizando la libreria anteriormente importado 'random'
print("Generando exponente aleatorio para Usuario A ...")
print()
exponenteA = random.randrange(p-1)
print(exponenteA)
print()
print("Generando exponente aleatorio para Usuario B ...")
print()
exponenteB = random.randrange(p-1)
print(exponenteB)
print()

#Calculamos la Clave del Usuario A, llamando a nuestra función 'mod_exp' previamente definida
print("Calculamos la Clave del Usuario A")
claveUsuarioA = mod_exp(b,exponenteA,p)
print()
print("La Clave del Usuario A es: ", claveUsuarioA)
print()

#Calculamos de la misma forma la Clave del Usuario B
print("Calculamos la Clave del Usuario B ...")
claveUsuarioB = mod_exp(b,exponenteB,p)
print()
print("La Clave del Usuario B es: ", claveUsuarioB)
print()

#Simulamos el intercambio de claves para poder generar la Clave Final que tendrá que ser la misma para ambos usuarios
enviarGenerar_datos("A","B",1,0)
enviarGenerar_datos("B","A",1,0)
print()

#Generamos las claves finales usando de base de nuestro algoritmo las claves generadas previamente
enviarGenerar_datos("A","B",0,1)
claveFinalUsuarioA = mod_exp(claveUsuarioB,exponenteA,p)
enviarGenerar_datos("B","A",0,1)
claveFinalUsuarioB = mod_exp(claveUsuarioA,exponenteB,p)
print()

#Comprobamos que ambas Claves coinciden y las mostramos por pantalla
print("Comprobando que las claves coinciden ...")
print()
print("Clave Final Usuario A: ", claveFinalUsuarioA)
print("Clave Final Usuario B: ", claveFinalUsuarioB)
print()

if claveFinalUsuarioA == claveFinalUsuarioB:
    print(Fore.BLUE + Back.YELLOW + "Enhorabuena!! Las claves coinciden!"+Fore.RESET +Back.RESET)
else:
    print(Fore.RED + "Lo sentimos, algo fué mal."+Fore.RESET)
