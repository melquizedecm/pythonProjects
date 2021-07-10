##################################################################################
# Nombre del programa: Clase Lista                                               #                                          
# Autor del programa: Emilio Guillen                                             #
# Descripcion del programa: Se crea la clase Lista, sus atributos y              #
# metodos que posteriormente nos serviran para programar listas, pilas y colas.  #                                                                           
##################################################################################


# Se importa la clase Nodo para poder acceder a sus metodos y atributos
from classNodo1 import *

# Se crea la clase lista y se inicializan sus atributos
class Lista:
 	nodoCabeza = None 
 	nodoActual = None
 	nodoCola = None

# Metodo constructor que inicia al nodo cabeza
 	def __init__(self):
 		self.nodoCabeza = None 

# Metodo que recibe un dato y permite crear un enlace derecho con ese dato
 	def agregarNodoDerecho(self,dato):
 		nuevoNodo = Nodo(dato)
 		if self.nodoCabeza == None:
 			self.nodoCabeza = nuevoNodo
 		else:
 			self.nodoActual = self.nodoCabeza
 			while self.nodoActual.getEnlaceD() != None:
 				self.nodoActual = self.nodoActual.getEnlaceD()
 			self.nodoActual.setEnlaceD(nuevoNodo)

# Este metodo permite recorrer las listas comenzando 
# por la cabeza y terminando en la cola
 	def recorrerLista(self):
 		self.nodoActual = self.nodoCabeza
 		while self.nodoActual.getEnlaceD() != None:
 			print(self.nodoActual.getDato())
 			self.nodoActual = self.nodoActual.getEnlaceD()
 		print(self.nodoActual.getDato())

# Este metodo nos devuelve la cola
 	def getColaDerecho(self):
 		self.nodoActual = self.nodoCabeza
 		while self.nodoActual.getEnlaceD() != None:
 			self.nodoActual = self.nodoActual.getEnlaceD()
 			return self.nodoActual


# Este metodo recibe un dato para buscar y recorre la lista hasta encontrarlo
 	def buscarNodoDerecho(self, datoABuscar):
 		self.nodoActual = self.nodoCabeza
 		contador_posicion = 1
 		while self.nodoActual.getDato() !=datoABuscar:
 			self.nodoActual = self.nodoActual.getEnlaceD()
 			if self.nodoActual == None:
 				return False
 			contador_posicion += 1
 		return contador_posicion 



# Metodo que recibe un dato a eliminar, lo encuentra en la lista y lo borra
 	def eliminarNodo(self, datoAEliminar):
 		if datoAEliminar == self.nodoCabeza.getDato():
 			self.nodoCabeza = self.nodoCabeza.getEnlaceD()
 			return True 
 		else: 
 			self.nodoActual = self.nodoCabeza
 			while self.nodoActual.getDato() != datoAEliminar:
 				nodoAnterior = self.nodoActual
 				self.nodoActual = self.nodoActual.getEnlaceD()
 				if self.nodoActual == None:
 					return False 	
 			nodoAnterior.setEnlaceD(self.nodoActual.getEnlaceD())
 			self.nodoActual.setEnlaceD(None)
 			return True 

# Metodo que comprueba si una lista esta vacia
 	def ListaVacia(self):
 		if self.nodoCabeza == None:
 			return True









 	