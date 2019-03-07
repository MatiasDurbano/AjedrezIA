import chess

class Tablero(object):
    
    def __init__(self):
        self.tablero=chess.Board()

    def mostrar(self):
        print(self.tablero)

    def mostrarJugadas(self):
        return list(self.tablero.generate_legal_moves())
