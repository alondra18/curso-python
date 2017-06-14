import random
import sys

empate = 0
ganado = 0
perdido = 0

def elige(x):
	return {
	    '1': 'piedra'
	    '2': 'papel'
	    '3': 'tijera'
	    '4': 'salir'
	}


def eligeOpcion():
	print("Presionar 1 para piedar")
	print("Presionar 2 para papel")
	print("Presionar 3 para tijeras")
	print("Presionar 4 para salir")
	print("")


	eleccion = input("Que opcion eliges :)")

	resultado = elige(eleccion)


	if resultado == 'salir':
		print("")
		sys.exit('Saliendo del Juego...')
	else:
		return resultado


def computerEleccion():
	opciones = ["piedra","papel","tijeras"]
	opcionAleatoria = random.randint(0,2)
	return opciones[opcionAleatoria]

def comparacion(humana, computer):
	if humana == computer:
		return "empate"
	if humana == "piedra" and computer == "papel":
		return "computer"
	if humana == "papel" and computer == "tijeras":
		return "computer"	
	if humana == "tijeras" and computer == "piedra":
		return "computer"
	else:
		return "humana"
	pass

while True:
	humana = eligeOpcion()
	computer = computerEleccion()
	print("")
	print("Tu eleccion", humana)
	print("La eleccion de la computadora", computer)


	resultado = comparacion(humana, computer)

	if resultado == "empate":
		empate +=1:

		if empate <= 1:
			print('Has empatado')
		else:
			print('Has empatado' + str(empate) + 'veces')
	else:

		if resultado == "computer":
			perdido += 1

			if perdido <= 1:
				print('Has perdido')
			else:
				print('Has perdido' + str(perdido) + 'veces')
		else:

			ganado += 1
			if ganado <= 1:
				print('Has ganado')
			else:
				print('Has ganado' + str(ganado) + 'veces')

		print("")







	pass