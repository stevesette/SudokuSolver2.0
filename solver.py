import abc

class Solver(abc.ABC):
    @abc.abstractmethod
    def solve(self, board):
        print("Solve unimplemented in this class")
        exit(-1)