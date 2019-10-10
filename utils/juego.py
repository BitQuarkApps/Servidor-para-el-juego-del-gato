# Clase que contiene un tablero para el juego del gato
# Así como el turno actual, determinar al ganador y brindar el tablero
import numpy as np

class Juego:
    """
    Clase que prepara el juego
    """

    def __init__(self):
        self.tablero = [[None for _ in range(3)] for _ in range(3)]
        print(self.tablero)
        self.player1 = None
        self.player2 = None
        self.turnoActual = 0# 0 para el turno del player1, 1 para el turno del player2
    
    def getBoard(self):
        """
        Regresa el tablero actual.
        """
        return self.tablero
    
    def tirar(self, x, y):
        """
        El jugador (quien sea) realiza un tiro.

        Recibe:

        x: (int) => Posición X en donde tirar.

        y: (int) => Posición Y en donde tirar.

        Regresa:

        Boolean, String => True si pudo tirar y un mensaje de 'OK'.

        False si la casilla está ocupada y un mensaje indicando que no puede tirar ahí.
        """
        if self.tablero[x][y] != 'X' and self.tablero[x][y] != 'O':
            if self.turnoActual == 0:
                self.tablero[x][y] = 'X'
                return True, 'OK'
            else:
                self.tablero[x][y] = 'O'
        else:
            return False, 'No puedes tirar aqui'

    def cambiarTurno(self):
        """
        Realizar el cambio del turno.
        Por defecto tira el player 1 [ 0 ].
        
        Regresa (turno actual):
        
        1 ó 0 dependiendo del turno que sigue, siendo:
        
        0 = Turno del jugador 1.

        1 = Turno del jugador 2.
        """
        if self.turnoActual == 0:
            self.turnoActual = 1
            return self.turnoActual
        else:
            self.turnoActual = 0
            return self.turnoActual
    
    def setPlayer1(self):
        """
        Establecer al jugador uno.

        Regresa:

        True, 'X' => True indica que el player uno no está ocupado, 'X' el caracter que se le asignó

        ó

        False, None => False indica que el player no se puede tomar, None el caracter que no puede jugar.
        """
        if self.player1 == None:
            self.player1 = 'X'
            return True, 'X'
        return False, None
    
    def setPlayer2(self):
        """
        Establecer al jugador dos.

        Regresa:

        True, 'O' => True indica que el player dos no está ocupado, 'O' el caracter que se le asignó

        ó

        False, None => False indica que el player no se puede tomar, None el caracter que no puede jugar.
        """
        if self.player1 == None:
            self.player2 = 'O'
            return True, 'O'
        return False, None
    
    def determinarGanador(self, turno):
        """

        Analizar las 8 combinaciones de determinar el ganador para X u O

        Parámetros:

        turno: (String) = 'X' u 'O'

        Regresa:

        True / False Ganó?
        """
        if self.tablero[0][0] == turno and self.tablero[0][1] == turno and self.tablero[0][2] == turno:
            return True
        if self.tablero[1][3] == turno and self.tablero[1][4] == turno and self.tablero[1][5] == turno:
            return True
        if self.tablero[2][6] == turno and self.tablero[2][7] == turno and self.tablero[2][8] == turno:
            return True
        if self.tablero[0][0] == turno and self.tablero[1][3] == turno and self.tablero[2][6] == turno:
            return True
        if self.tablero[0][1] == turno and self.tablero[1][4] == turno and self.tablero[2][7] == turno:
            return True
        if self.tablero[0][2] == turno and self.tablero[1][5] == turno and self.tablero[2][8] == turno:
            return True
        if self.tablero[0][0] == turno and self.tablero[1][4] == turno and self.tablero[2][8] == turno:
            return True
        if self.tablero[0][2] == turno and self.tablero[1][4] == turno and self.tablero[2][4] == turno:
            return True
        return False
        