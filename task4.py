from abc import ABC, abstractmethod

class GAME(ABC):
    @abstractmethod
    def play(self):
        pass
class Chess(GAME):
    def play(self):
        print("Playing Chess")
class TicTacToe(GAME):
    def play(self):
        print("TicTacToe")

