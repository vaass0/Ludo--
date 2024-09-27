import random 
import tkinter as tk

class Ficha:
    def __init__(self, posicion, color):
        self.color = color
        self.posicion = posicion
    def get_posicion(self):
        return self.posicion
    def set_posicion(self,posicion):
        self.posicion = posicion
    def moverFicha(self, pasos):
        posicion = self.get_posicion()
        if posicion != 40 and posicion != 0:
            self.set_posicion(posicion+pasos)
    def resetFicha(self):
        self.set_posicion(0)

class Jugador:
    def __init__(self,color,fichas) :
        self.color = color
        self.fichas =  fichas
    def agregar_ficha(self):
        for i in range(4):
            self.fichas.append(Ficha(0,self.color))
    def mostrar_fichas(self):
        for i in self.fichas:
            if i.posicion == 0:
                print("Ficha ", self.fichas.index(i) + 1 ,"en spawn")
            elif i<40:
                print("Ficha ", self.fichas.index(i) + 1 ,"en juego en la posicion:",i.posicion)
            elif i == 40:
                print("Ficha ", self.fichas.index(i) + 1 , "en la meta")
    def seleccionaFicha(self,dado):
        self.mostrar_fichas()
        ficha = int(input("Indique el numero de la ficha a seleccionar: "))
        if ficha>4 or ficha<1:
            print("la ficha seleccionada no existe, seleccionar un numero del 1 al 4...")
            self.seleccionarFicha(dado)
        if dado != 6 and self.fichas(ficha-1).posicion == 0:
            print("la ficha seleccionada no es jugable, seleccione otra por favor...")
            self.seleccionarFicha(dado)
        return ficha

class Tablero:
    def __init__(self,jugadores,casillas):
       self.casillas = casillas
       self.jugadores = jugadores
    def agregar_jugador(self,cantidad):
        for i in range(cantidad):
            color = str(input("Elija un color entre Rojo/Amarillo/Azul/Verde: "))
            if color == "Rojo" or "rojo" or "Azul" or "azul" or "Amarillo" or "amarillo" or "Verde" or "verde":
                for i in self.jugadores:
                    if i.color == color:
                        print("El color seleccionado esta ocupado, intente con otro...")
                        self.agregar_jugador(cantidad)
                player = Jugador(color,[])
                player.agregar_ficha()
                self.jugadores.append(player)
            else:
                print("Ingrese un color valido...")
                self.agregar_jugador(cantidad)
    def mostrar_jugadores(self):
        for i in self.jugadores:
            print(i.color)
            i.mostrar_fichas()
            
    def lanzar_dado():
        return random.randint(1,6)
    def turno_jugador(self):
         self.lanzar_dado()
     
tablero = Tablero([])
tablero.agregar_jugador(3)
tablero.mostrar_jugadores()

faker = Jugador("Rojo",[])
faker.mostrar_fichas()
faker.agregar_ficha()
faker.mostrar_fichas()

            
ficha = Ficha(0,"Azul")
print(ficha.get_posicion())
print(ficha.color)

ficha.moverFicha(6)
print(ficha.posicion)
ficha.resetFicha()
print(ficha.posicion)