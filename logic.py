from PyQt6.QtWidgets import *
from gui import *
from random import *


class Logic(QMainWindow, Ui_Maze):
    MAZEHEIGHT=68
    MAZEWIDTH=68
    def maze_generation(self)->list:
        '''
        generates maze
        :return:
        '''
        new_maze=[]
        #first row
        first_row=['X' for i in range(Logic.MAZEWIDTH)]
        new_maze.append(first_row)
        for line in range(Logic.MAZEHEIGHT-2):
            row=[]
            #left side
            row.append('X')
            for cell in range(Logic.MAZEWIDTH-2):
                if random()>.5:
                    row.append('X')
                else:
                    row.append(' ')
            new_maze.append(row)
            #right side
            row.append('X')
        # Last row
        new_maze.append(first_row)
        return new_maze

    def maze_display(self)->None:
        '''
        dispplays maze to table
        :return:
        '''
        maze=self.maze_generation()
        for row in range(len(maze)):
            for cell in range(len(maze[row])):
                self.maze.setItem(row,cell,QTableWidgetItem(maze[row][cell]))


    def __init__(self)->None:
        '''

        '''
        super().__init__()
        self.setupUi(self)
        self.maze_display()
        self.UpButton.clicked.connect(lambda: self.upbutton())

    def upbutton(self)->None:
        '''

        :return:
        '''
        pass

