from PyQt6.QtWidgets import *
from gui import *
from random import *


class Logic(QMainWindow, Ui_Maze):
    MAZEHEIGHT=68
    MAZEWIDTH=68
    def maze_generation(self)->list:
        '''
        generates maze
        :return: the maze generated
        '''
        new_maze=[]
        #first row
        first_row=['XXX' for i in range(Logic.MAZEWIDTH)]
        new_maze.append(first_row)

        for line in range(1,Logic.MAZEHEIGHT-1):
            row=[]
            #left side
            row.append('XXX')
            for cell in range(1,Logic.MAZEWIDTH-1):
                # #checking if top middle top right and left above are X's then it has to be a space
                # # X X 0
                # # X ''
                # if new_maze[line-1][cell-1]==new_maze[line-1][cell]==row[cell-1]=='XXX':
                #     row.append(' ')
                # checking if top middle top right and left above are ' 's then it has to be a X
                # '' '' 0
                # '' X
                if new_maze[line - 1][cell - 1] == new_maze[line - 1][cell] == row[cell - 1] == ' ':
                    row.append('XXX')
                #checking if top and left is '' and top left is X then current is ''
                # X '' 0
                # '' ''
                elif new_maze[line-1][cell]==row[cell - 1]==' ' and new_maze[line-1][cell-1]=='XXX':
                    row.append(' ')
                #checking if top and left are X and top left is '' then current is X'
                # '' X 0
                # X X
                elif new_maze[line-1][cell]==row[cell - 1]=='XXX' and new_maze[line-1][cell-1]==' ':
                    row.append('XXX')
                elif random()>.5:
                    row.append(' ')
                else:
                    row.append('XXX')
            new_maze.append(row)
            #right side
            row.append('XXX')
        # Last row
        new_maze.append(first_row)
        return new_maze

    def maze_display(self,maze:list)->None:
        '''
        displays maze to table
        :return:
        '''
        for row in range(len(maze)):
            for cell in range(len(maze[row])):
                self.maze.setItem(row,cell,QTableWidgetItem(maze[row][cell]))


    def __init__(self)->None:
        '''

        '''
        super().__init__()
        self.setupUi(self)
        maze=self.maze_generation()
        self.maze_display(maze)
        self.UpButton.clicked.connect(lambda: self.upbutton())

    def upbutton(self)->None:
        '''

        :return:
        '''
        pass

