from abc import ABC, abstractmethod

class Solver(ABC):
    @abstractmethod
    def solve(self):
        print("Solve unimplemented in this class")
        exit(-1)

class RecursiveSolution(Solver):
    def __init__(self, board):
        self.board = board.get_numpy()
        self.quads = {0:((0,3), (0,3)),
                      1:((0,3), (3,6)),
                      2:((0,3), (6,9)),
                      3:((3,6), (0,3)),
                      4:((3,6), (3,6)),
                      5:((3,6), (6,9)),
                      6:((6,9), (0,3)),
                      7:((6,9), (3,6)),
                      8:((6,9), (6,9))}

    def is_in_row(self, row_num, value):
        return value in self.board[row_num,:]

    def is_in_col(self, col_num, value):
        return value in self.board[:,col_num]

    def is_in_quad(self, row_num, col_num, value):
        quad_num = int(row_num / 3) + int(col_num / 3) * 3
        first, second = self.quads[quad_num]
        return value in self.board[first[0]:first[1],second[0]:second[1]]

    def can_place(self, row_num, col_num, value):
        return not (self.is_in_col(col_num, value) or self.is_in_row(row_num, value)
                    or self.is_in_quad(row_num, col_num, value))

    def recurse(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    for val in range(9):
                        if self.can_place(i,j,val):
                            self.board[i][j] = val
                            if self.recurse():
                                return True
                            else:
                                self.board[i][j] = 0
                    return False
        return True


    def solve(self):
        if self.recurse():
            return self.board
        else:
            raise

