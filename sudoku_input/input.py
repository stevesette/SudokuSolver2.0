from abc import ABC, abstractmethod
import numpy as np

"""
This is an abstract class module for sudoku board input.
"""
class Input(ABC):
    """
    This class is abstract for all input methods
    """
    @abstractmethod
    def take_input(self):
        """
        This method takes in input for the sudoku board
        :return: the sudoku board data in Numpy Array format
        """
        pass

class CsvInput(Input):
    """
    This class is for taking input from CSV files.
    """
    def take_input(self):
        pass

class ExcelInput(Input):
    """
    This class is for taking input from Excel files.
    """
    def take_input(self):
        pass

class ManualInput(Input):
    """
    This class is for taking input manually through the "input" keyword.
    """
    def take_input(self):
        pass

class PythonInput(Input):
    """
    This class is for taking input from some Python object.
    """
    def take_input(self):
        pass

class GenerateInput(Input):
    """
    This class is for taking input from an in house generated sudoku puzzle.
    """
    def take_input(self):
        pass
