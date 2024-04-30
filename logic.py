from PyQt6.QtWidgets import *
from gui import *
from random import *


class Logic(QMainWindow, Ui_Maze):
    MAZEHEIGHT=140
    MAZEWIDTH=68
    def maze_generation(self):
        xs = QTableWidgetItem('X')
        spaces = QTableWidgetItem('')
        for height in range(Logic.MAZEHEIGHT):
            for cell in range(Logic.MAZEWIDTH):
                if random()>.5:
                    self.maze.setItem(height, cell, xs)
                else:
                    self.maze.setItem(height, cell, spaces)

    def __init__(self)->None:
        '''

        '''
        super().__init__()
        self.setupUi(self)
        self.maze_generation()
