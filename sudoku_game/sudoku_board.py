import numpy as np
import sudoku_input

'''
This module stores the data for a given sudoku board found by the input module.
'''
class SudokuBoard:
    '''
    Representation of the sudoku board data as a numpy square array
    '''

    def __init__(self, input):
        self.board = input.take_input()


    def get_numpy(self, as_cell=True):
        if as_cell:
            return self.board.apply()
        return self.board

    def get_list_of_list(self):
        return self.board.tolist()