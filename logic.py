from PyQt6.QtWidgets import *
from gui import *
from random import *

class Logic(QMainWindow, Ui_Maze):
    MAZEHEIGHT=68
    MAZEWIDTH=68
    STARTPOS=(0,0)
    ENDPOS=(0,0)
    ENDSTARTRANG=25
    TEMP=(0,0)

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
        self.select_start_end(new_maze)
        return new_maze
    def select_start_end(self,new_maze:list)->list:
        '''
        chooses start and end and carves a path between
        :param new_maze: maze
        :return:
        '''
        start_chance=1
        end_chance=1
        endin=False
        startin=False
        #end select
        for line in range(1,Logic.ENDSTARTRANG+1):
            for cell in range(Logic.MAZEWIDTH-Logic.ENDSTARTRANG-1,Logic.MAZEWIDTH-1):
                if new_maze[line][cell]==' ':
                    if randrange(Logic.ENDSTARTRANG**2)<end_chance:
                        new_maze[line][cell]='END'
                        Logic.ENDPOS = (line, cell)
                        endin=True
                        break
                    end_chance += 1
                else:
                    end_chance+=1
            if endin:
                break
        #start select
        for line in range(Logic.MAZEHEIGHT-Logic.ENDSTARTRANG-1,Logic.MAZEHEIGHT-1):
            for cell in range(1,Logic.ENDSTARTRANG+1):
                if new_maze[line][cell]==' ':
                    if randrange(Logic.ENDSTARTRANG**2)<end_chance:
                        new_maze[line][cell]='Start'
                        Logic.STARTPOS=(line,cell)
                        startin=True
                        break
                    start_chance += 1
                else:
                    start_chance+=1
            if startin:
                break
        self.carve_path(new_maze)
        return new_maze

    def carve_path(self,new_maze)->list:
        '''
        carves path from start to end
        :param new_maze:
        :return: new_maze with path made
        '''
        #logic is goes to nearest space checking for
        temp_start_pos=Logic.STARTPOS
        poslist=[]
        while temp_start_pos!=Logic.ENDPOS:

            if temp_start_pos[0]<0 or temp_start_pos[1]<0 or temp_start_pos[1]>Logic.MAZEWIDTH or temp_start_pos[0]>Logic.MAZEHEIGHT or temp_start_pos==Logic.ENDPOS:
                break
            #end around check
            if new_maze[temp_start_pos[0]-1][temp_start_pos[1]]=='END' or  new_maze[temp_start_pos[0]][temp_start_pos[1]+1]=='END' or new_maze[temp_start_pos[0]][temp_start_pos[1]-1]=='END' or new_maze[temp_start_pos[0]+1][temp_start_pos[1]]=='END':
                break
            #check all sides for spaces
            # top check
            if new_maze[temp_start_pos[0]-1][temp_start_pos[1]]==' ':
                poslist.append(temp_start_pos)
                temp_start_pos=(temp_start_pos[0]-1,temp_start_pos[1])
                new_maze[temp_start_pos[0]][temp_start_pos[1]] = 'w'
            #right check
            elif new_maze[temp_start_pos[0]][temp_start_pos[1]+1]==' ':
                poslist.append(temp_start_pos)
                temp_start_pos = (temp_start_pos[0], temp_start_pos[1]+1)
                new_maze[temp_start_pos[0]][temp_start_pos[1]] = 'w'
            #left check
            elif new_maze[temp_start_pos[0]][temp_start_pos[1]-1]==' ':
                poslist.append(temp_start_pos)
                temp_start_pos = (temp_start_pos[0], temp_start_pos[1]-1)
                new_maze[temp_start_pos[0]][temp_start_pos[1]] = 'w'
            #bottom check
            elif new_maze[temp_start_pos[0]+1][temp_start_pos[1]]==' ':
                poslist.append(temp_start_pos)
                temp_start_pos = (temp_start_pos[0]+1, temp_start_pos[1])
                new_maze[temp_start_pos[0]][temp_start_pos[1]] = 'w'
            #random
            else:
            #carving if stuck
            #carve up

                if temp_start_pos[0]>Logic.ENDPOS[0]:
                    if new_maze[temp_start_pos[0]-1][temp_start_pos[1]]=='XXX':
                        new_maze[temp_start_pos[0]-1][temp_start_pos[1]]=' '
                        poslist.append(temp_start_pos)
                        temp_start_pos=(temp_start_pos[0]-1,temp_start_pos[1])
                        new_maze[temp_start_pos[0]][temp_start_pos[1]] = 'wv'
                    else:
                        temp_start_pos=self.retrace(poslist)
                #carve down
                elif temp_start_pos[0]<Logic.ENDPOS[0]:
                    if new_maze[temp_start_pos[0]+1][temp_start_pos[1]]=='XXX':
                        new_maze[temp_start_pos[0]+1][temp_start_pos[1]]=' '
                        poslist.append(temp_start_pos)
                        temp_start_pos=(temp_start_pos[0]+1,temp_start_pos[1])
                        new_maze[temp_start_pos[0]][temp_start_pos[1]] = 'wv'
                    else:
                        temp_start_pos=self.retrace(poslist)
                #carve left
                elif temp_start_pos[1]<Logic.ENDPOS[1]:
                    if new_maze[temp_start_pos[0]][temp_start_pos[1]+1]=='XXX':
                        new_maze[temp_start_pos[0]][temp_start_pos[1]+1]=' '
                        poslist.append(temp_start_pos)
                        temp_start_pos=(temp_start_pos[0],temp_start_pos[1]+1)
                        new_maze[temp_start_pos[0]][temp_start_pos[1]] = 'wv'
                    else:
                        temp_start_pos=self.retrace(poslist)
                #carve right
                elif temp_start_pos[1]>Logic.ENDPOS[1]:
                    if new_maze[temp_start_pos[0]][temp_start_pos[1]-1]=='XXX':
                        new_maze[temp_start_pos[0]][temp_start_pos[1]-1]=' '
                        poslist.append(temp_start_pos)
                        temp_start_pos=(temp_start_pos[0],temp_start_pos[1]-1)
                        new_maze[temp_start_pos[0]][temp_start_pos[1]] = 'wv'
                    else:
                        temp_start_pos=self.retrace(poslist)
        Logic.TEMP=temp_start_pos
        return new_maze
    def retrace(self,poslist, n=1)->tuple:
        '''
        recursive function that goes to previous positions
        :param poslist:
        :param n: number of times to go back a position
        :return:
        '''
        backone=poslist.pop(-1)
        return backone

    def maze_display(self,maze:list)->None:
        '''
        displays maze to table
        :return:
        '''
        for row in range(len(maze)):
            for cell in range(len(maze[row])):
                self.maze.setItem(row,cell,QTableWidgetItem(maze[row][cell]))
                if maze[row][cell]== 'w' or maze[row][cell] =='wv':
                    self.maze.item(row, cell).setBackground(QtGui.QColor(0, 225, 0))
        #color start
        self.maze.item(Logic.STARTPOS[0], Logic.STARTPOS[1]).setBackground(QtGui.QColor(243, 225, 66))
        #color end
        self.maze.item(Logic.ENDPOS[0], Logic.ENDPOS[1]).setBackground(QtGui.QColor(225, 62, 58))
        self.maze.item(Logic.TEMP[0], Logic.TEMP[1]).setBackground(QtGui.QColor(0, 225, 0))


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

