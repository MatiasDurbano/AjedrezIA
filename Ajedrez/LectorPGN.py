#! /usr/bin/python
import chess.pgn
import chess
import os
from Tablero import Tablero

class LectorPGN(object):

    def __init__(self,dir):
        self.listPGN=os.listdir(dir)
        self.dir=dir
    
    def leerPGN(self):
       for pgn in self.listPGN:
           partida=open(self.dir+"/"+pgn)
           juego=chess.pgn.read_game(partida)
           if juego.headers["Result"] == "1-0" or juego.headers["Result"] == "0-1":
               #enviar a la red los movimientos?
               board = juego.board()
               for mov in juego.mainline_moves():
                   board.push(mov)
                   print(Tablero(board).serialize())

