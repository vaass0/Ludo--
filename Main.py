import random 

class Ficha:
    def __init__(self, posicion):
        self.posicion = posicion
    def get_posicion(self):
        return self.posicion
    def set_posicion(self,posicion):
        self.posicion = posicion
    def moverFicha(self, pasos):
        posicion = self.get_posicion()
        if posicion != 40 and posicion != 0:
            self.set_posicion(posicion+pasos)
        elif posicion == 0:
             self.set_posicion(1)
    def resetFicha(self):
        self.set_posicion(0)

class Jugador:
    def __init__(self,color,fichas) :
        self.color = color
        self.fichas =  fichas
    def agregar_ficha(self):
        for i in range(4):
            self.fichas.append(Ficha(0))
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
        while(True):
            ficha = int(input("Indique el numero de la ficha a seleccionar: "))
            if ficha>4 or ficha<1:
                print("la ficha seleccionada no existe, seleccionar un numero del 1 al 4...")
            elif dado != 6 and self.fichas(ficha-1).posicion == 0:
                print("la ficha seleccionada no es jugable, seleccione otra por favor...")
            else:
                break
        return   ficha
    def fichas_en_juego(self):
        for i in self.fichas:
            if(i.posicion != 0 ):
                return True
        return False
    def win(self):
        for ficha in self.fichas:
            if ficha.posicion != 40:
                return False
        return True
class Tablero:
    def __init__(self,jugadores):
       self.jugadores = jugadores
    def agregar_jugador(self,cantidad):
        for i in range(cantidad):
            while(True):
                self.mostrar_jugadores()
                color = input("Elija un color entre Rojo/Amarillo/Azul/Verde: ").lower()
                if color == "rojo" or color == "azul" or color == "amarillo" or color == "verde":
                     for  i in self.jugadores:
                        if i.color == color:
                            print("El color seleccionado esta ocupado, intente con otro...")
                            break
                     else:
                        player = Jugador(color,[])
                        player.agregar_ficha()
                        self.jugadores.append(player)
                        break
                else:
                    print("Ingrese un color valido...")
    def mostrar_jugadores(self):
        for i in self.jugadores:
            print(i.color)
            i.mostrar_fichas()
            
    def lanzar_dado(self):
        return random.randint(1,6)
    def turno(self):
        for jugador in self.jugadores:
            if(jugador.win()):
                pass
            dado = self.lanzar_dado()
            print("El numero del dado es: ",dado)
            if(jugador.fichas_en_juego() or dado == 6):
                ficha = jugador.seleccionar_ficha(dado)
                ficha.mover(dado)
            else:
                print("No puedes mover fichas...💀")


tablero = Tablero([])
tablero.agregar_jugador(1)
tablero.mostrar_jugadores()
tablero.turno()

