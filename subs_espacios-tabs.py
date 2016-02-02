# -*- coding: utf-8 -*-

import sys

try:
	arquivo = sys.argv[1]
	arquivo = open(arquivo,"r").read()
except:
	print(u"Necesitas introducir de argumento un documento de texto")
	sys.exit()
	
print(u"Substituir:")
opcion = raw_input(u"[1] - Espacios por Tabs\n[2] - Tabs por Espacios\n>>> ")

if opcion == "1":
	num_espacios = raw_input(u">>> Numero de espacios a subtituir por cada Tabulacion: ")
else:
	num_espacios = raw_input(u">>> Numero de espacios a introducir por cada Tabulacion: ")
	
def substituir(text,opc,num_esp):
	if opc == "1":
		lista_separador = text.split(" "*int(num_esp))
		texto_salida = [lista_separador[0]]+["\t"+x for x in lista_separador[1:len(lista_separador)]]
		texto_salida = "".join(texto_salida)
	elif opc == "2":
		lista_separador = text.split("\t")
		texto_salida = [lista_separador[0]]+[" "*int(num_esp)+x for x in lista_separador[1:len(lista_separador)]]
		texto_salida = "".join(texto_salida)
	return texto_salida
	
arquivo_a_crear = open("Subs_"+sys.argv[1],"w")
arquivo_a_crear.write(substituir(arquivo,opcion,num_espacios))
arquivo_a_crear.close()