import sys
import os

def parse_instructions():
	instructions = []
	user_input = input('Ingresa el nombre (PATH) del archivo de instrucciones: ')
	file_path = user_input.rstrip('\r')
	if not os.path.isfile(file_path):
		print('El archivo no existe, revisa el nombre ingresado')
		print('Terminando ejecucion por error de input')

		exit()
	
	with open(file_path.rstrip('\r')) as file:
		lines = file.read().splitlines()
		"""
			Possible options
			A - 3 args, all numbers
			P - 2 args, all numbers
			L - 1 arg, number
			F - 0 args
			E - 0 args
			C - all comments
		"""
		for i, line in enumerate(lines):
			words = line.split(' ')
			if words[0] == 'A':
				if(len(words) < 4):
					print('Cantidad invalida de argumentos en linea ', i+1)
					print('Terminando ejecucion por error de input')
					exit()
				instruction = [words[0]]
				try:
					instruction.append(int(words[1]))
					instruction.append(int(words[2]))
					instruction.append(int(words[3]))
				except ValueError:
					print("Uno de los argumentos en la linea ", i+1, "no es valido")
					print('Terminando ejecucion por error de input')
					exit()
			elif words[0]== 'P':
				if(len(words) < 3):
					print('Cantidad invalida de argumentos en linea ', i+1)
					print('Terminando ejecucion por error de input')
					exit()
				instruction = [words[0]]
				try:
					instruction.append(int(words[1]))
					instruction.append(int(words[2]))
				except ValueError:
					print("Uno de los argumentos en la linea ", i+1, "no es valido")
					print('Terminando ejecucion por error de input')
					exit()
			elif words[0] == 'L':
				if(len(words) < 2):
					print('Cantidad invalida de argumentos en linea ', i+1)
					print('Terminando ejecucion por error de input')
					exit()
				instruction = [words[0]]
				try:
					instruction.append(int(words[1]))
				except ValueError:
					print("Uno de los argumentos en la linea ", i+1, "no es valido")
					print('Terminando ejecucion por error de input')
					exit()
			elif words[0] == 'C':
				instruction = [words[0]]
				instruction.append(' '.join(words[1::]))
			elif words[0]== 'E':
				instruction = [words[0]]
			elif words[0] == 'F':
				instruction = [words[0]]
			else: 
				print("Instruccion invalida")
				print('Terminando ejecucion por error de input')
				exit()
			instructions.append(instruction)
		return instructions