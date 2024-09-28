import random 

class Ficha:
    def __init__(self, posicion):
        self.posicion = posicion

    def get_posicion(self):
        return self.posicion

    def set_posicion(self,posicion):
        self.posicion = posicion

    def mover_ficha(self,pasos,numCasillas):
        posicion = self.get_posicion()
        if posicion + pasos <= numCasillas and posicion != -1:
            self.set_posicion(posicion+pasos)
        elif posicion + pasos > numCasillas:
            self.set_posicion(numCasillas-(posicion+pasos-numCasillas))
        elif posicion == -1:
             self.set_posicion(0)

    def reset_ficha(self):
        self.set_posicion(0)

class Jugador:
    def __init__(self,color,fichas,numCasillas) :
        self.color = color
        self.fichas =  fichas
        self.numCasillas = numCasillas

    def agregar_ficha(self):
        for i in range(4):
            self.fichas.append(Ficha(-1))

    def mostrar_fichas(self):
        numCasillas = self.numCasillas
        for i in self.fichas:
            if i.posicion == -1:
                print("Ficha ", self.fichas.index(i) + 1 ,"en spawn")
            elif i.posicion < numCasillas:
                print("Ficha ", self.fichas.index(i) + 1 ,"en juego en la posicion:",i.posicion)
            elif i.posicion == numCasillas:
                print("Ficha ", self.fichas.index(i) + 1 , "en la meta")

    def seleccionar_ficha(self,dado):
        self.mostrar_fichas()
        while(True):
            ficha = int(input("Indique el numero de la ficha a seleccionar: "))
            if ficha>4 or ficha<1:
                print("la ficha seleccionada no existe, seleccionar un numero del 1 al 4...")
            elif dado != 6 and self.fichas[ficha-1].posicion == -1 or self.fichas[ficha-1].posicion == self.numCasillas:
                print("la ficha seleccionada no es jugable, seleccione otra por favor...")
            else:
                break
        return self.fichas[ficha-1]

    def fichas_en_juego(self):
        for i in self.fichas:
            if(i.posicion != -1 and i.posicion != self.numCasillas):
                return True
        return False

    def win(self,numCasillas):
        for ficha in self.fichas:
            if ficha.posicion != numCasillas:
                return False
        return True

    def posiciones_fichas(self):                    #Retorna una lista con las posiciones de las fichas
        posiciones = []
        for i in self.fichas:
            posiciones.append(i.posicion)
        return posiciones

class Tablero:
    def __init__(self,jugadores,casillasBlancas,casillasColor):
        self.jugadores = jugadores
        self.casillasBlancas = casillasBlancas
        self.casillasColor = casillasColor

    def num_de_casillas(self):                      #Retorna la cantidad total de casillas    
        return self.casillasBlancas + self.casillasColor

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
                        player = Jugador(color,[],self.num_de_casillas())
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
        numCasillas = self.num_de_casillas()
        for jugador in self.jugadores:
            print("Turno de",jugador.color)
            if(jugador.win(numCasillas)):
                pass
            dado = self.lanzar_dado()
            print("El numero del dado es: ",dado)
            if(jugador.fichas_en_juego() or dado == 6):
                ficha = jugador.seleccionar_ficha(dado)
                ficha.mover_ficha(dado,numCasillas)
                jugador.mostrar_fichas()
            else:
                print("No puedes mover fichas...💀")

    def posicion_relativa_al_indice(self,jugador):  #Retorna las posiciones relativas respecto al primer jugador
        distJug = int(self.casillasBlancas / 4)          #Distancia en casillas, que hay entre cada jugador 
        indice = self.jugadores.index(jugador)      #Numero que representa la distancia con el origen, el origen esta en el primer jugador
        posFichJug= jugador.posiciones_fichas()     #Posiciones de las fichas del jugador al que se analiza
        posRel = []                                 #Posiciones relativas al origen
        for i in posFichJug:                        #La variable Pos corresponde a la posicion relativa lineal de la ficha
            pos = i+indice*distJug                  
            if i == -1:
                posRel.append(-1)
            elif i >= self.casillasBlancas:
                posRel.append(i - self.casillasBlancas + 100)
            elif pos > self.casillasBlancas:
                posRel.append(pos - self.casillasBlancas)
            else:
                posRel.append(pos)

        return posRel

tablero = Tablero([],40,6)
tablero.agregar_jugador(4)
tablero.mostrar_jugadores()
while(True):
    for i in tablero.jugadores:
        print(i.color)
        print(i.posiciones_fichas())
        print(tablero.posicion_relativa_al_indice(i))
    tablero.turno()
