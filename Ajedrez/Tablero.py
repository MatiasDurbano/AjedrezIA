import chess
import numpy as np


class Tablero(object):
    
    def __init__(self,board ):
        self.tablero=board

    def serialize(self):
        
        assert self.tablero.is_valid()

        tableroEstado = np.zeros(64,np.uint8)
        for i in range(64):
            pp = self.tablero.piece_at(i)
            if pp is not None:
                 #print(i, pp.symbol())
                tableroEstado[i] = {"P": 1, "N": 2, "B": 3, "R": 4, "Q": 5, "K": 6, \
                                "p": 9, "n":10, "b":11, "r":12, "q":13, "k": 14}[pp.symbol()]
        if self.tablero.has_queenside_castling_rights(chess.WHITE):
            assert tableroEstado[0] == 4
            tableroEstado[0] = 7
        if self.tablero.has_kingside_castling_rights(chess.WHITE):
            assert tableroEstado[7] == 4
            tableroEstado[7] = 7
        if self.tablero.has_queenside_castling_rights(chess.BLACK):
            assert tableroEstado[56] == 8+4
            tableroEstado[56] = 8+7
        if self.tablero.has_kingside_castling_rights(chess.BLACK):
            assert tableroEstado[63] == 8+4
            tableroEstado[63] = 8+7

        if self.tablero.ep_square is not None:
            assert tableroEstado[self.tablero.ep_square] == 0
            tableroEstado[self.tablero.ep_square] = 8
        tableroEstado = tableroEstado.reshape(8,8)

        # binary state
        tablero = np.zeros((5,8,8), np.uint8)

        # 0-3 columns to binary
        tablero[0] = (tableroEstado>>3)&1
        tablero[1] = (tableroEstado>>2)&1
        tablero[2] = (tableroEstado>>1)&1
        tablero[3] = (tableroEstado>>0)&1

        # 4th column is who's turn it is
        tablero[4] = (self.tablero.turn*1.0)

        # 257 bits according to readme
        return tablero

    def mostrar(self):
        print(self.tablero)

    def mostrarJugadas(self):
        return list(self.tablero.generate_legal_moves())

#convierto el tablero en formato de FEN
        #tablero = np.zeros((8*8,5))
        #tablero[:,:,4]=self.tablero.turn*1.0
        #print (tablero)
        
        #fen= self.tablero.shredder_fen()
        #return fen