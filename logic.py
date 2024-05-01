from PyQt6.QtWidgets import *
from gui import *
from random import *


class Logic(QMainWindow, Ui_Maze):
    MAZEHEIGHT=68
    MAZEWIDTH=68
    def maze_generation(self)->None:
        '''
        generates maze
        :return:
        '''
        #outter wall
        #top
        for cell in range(Logic.MAZEWIDTH):
            self.maze.setItem(0, cell, QTableWidgetItem('X'))
        #bottom
        for cell in range(Logic.MAZEWIDTH):
            self.maze.setItem(Logic.MAZEWIDTH-1, cell, QTableWidgetItem('X'))
        #left
        for cell in range(Logic.MAZEHEIGHT):
            self.maze.setItem(cell, 0, QTableWidgetItem('X'))
        #right
        for cell in range(Logic.MAZEHEIGHT):
            self.maze.setItem(cell, Logic.MAZEHEIGHT-1, QTableWidgetItem('X'))
        #inner maze
        for height in range(Logic.MAZEHEIGHT-2):
            for cell in range(Logic.MAZEWIDTH-2):
                if random()>.5:
                    self.maze.setItem(height+1, cell+1, QTableWidgetItem('X'))
                else:
                    self.maze.setItem(height+1, cell+1, QTableWidgetItem(''))


    def __init__(self)->None:
        '''

        '''
        super().__init__()
        self.setupUi(self)
        self.maze_generation()
