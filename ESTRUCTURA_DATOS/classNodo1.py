# coding: utf8

############################################################################
# Nombre del programa: Clase Nodo                                          #                                          
# Autor del programa: Emilio Guillen                                       #
# Descripción del programa: Se crea la clase Nodo y sus atributos          #                                                                     
# que posteriormente nos serviran para programar listas, pilas y colas.    #                                                                           
############################################################################


"""
Lista de métodos:

setDato(nuevoDato): Cambia el dato del nodo
resetearEnlacheDerecho: Enlace apunta a null
setEnlaceD(Nodo): Recibe el nodo al que apunta  
resetearEnlacheIzquierdo: Enlace apunta a null
setEnlaceI(Nodo): Recibe el nodo al que apunta

"""

# Se crea la clase nodo
class Nodo:
	dato = ""
	enlace_derecho = None 
	enlace_izquierdo = None  

# Metodo constructor para los atributos
	def __init__(self, dato):
		self.dato = dato
		enlace_derecho = None
		enlace_izquierdo = None  

# Metodo que recibe un dato y lo asigna a la variable
	def setDato(self, nuevoDato):
		self.dato = nuevoDato

# Metodo que resetea el enlace derecho
	def resetearEnlaceD(self):
		self.enlace_derecho = None

# Metodo que recibe un nodo y se asigna a un enlace derecho
	def setEnlaceD(self, nuevoNodo):
		self.enlace_derecho = nuevoNodo

# Metodo que devuelve el valor del dato
	def getDato(self):
		return self.dato

# Metodo que devuelve el valor del enlace derecho
	def getEnlaceD(self):
		return self.enlace_derecho


