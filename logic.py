import time

from PyQt6.QtWidgets import *
from gui import *
from random import *
from timer import *
import leaderboard

class Logic(QMainWindow, Ui_Maze):
    MAZEHEIGHT=68
    MAZEWIDTH=68
    STARTPOS=(0,0)
    ENDPOS=(0,0)
    ENDSTARTRANG=25

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
                elif random()>.45:
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
            #emergency break
            if temp_start_pos[0]<0 or temp_start_pos[1]<0 or temp_start_pos[1]>Logic.MAZEWIDTH or temp_start_pos[0]>Logic.MAZEHEIGHT or temp_start_pos==Logic.ENDPOS:
                break
            #end around check
            if new_maze[temp_start_pos[0]-1][temp_start_pos[1]]=='END' or  new_maze[temp_start_pos[0]][temp_start_pos[1]+1]=='END' or new_maze[temp_start_pos[0]][temp_start_pos[1]-1]=='END' or new_maze[temp_start_pos[0]+1][temp_start_pos[1]]=='END':
                break
            #check all sides for spaces
            #right check
            if new_maze[temp_start_pos[0]][temp_start_pos[1]+1]==' ':
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
            # top check
            elif new_maze[temp_start_pos[0] - 1][temp_start_pos[1]] == ' ':
                poslist.append(temp_start_pos)
                temp_start_pos = (temp_start_pos[0] - 1, temp_start_pos[1])
                new_maze[temp_start_pos[0]][temp_start_pos[1]] = 'w'
            # if wv means it was a carved tile checking for carved as to not remove to many tiles
            elif new_maze[temp_start_pos[0] - 1][temp_start_pos[1]] == 'wv' or new_maze[temp_start_pos[0] - 1][temp_start_pos[1]] == 'wv' or new_maze[temp_start_pos[0]][temp_start_pos[1]-1]=='wv' or new_maze[temp_start_pos[0]][temp_start_pos[1]+1]=='wv' or new_maze[temp_start_pos[0]][temp_start_pos[1]]=='wv':
                temp_start_pos,new_maze=self.retrace(poslist,new_maze)
            else:
            #carving if stuck
            #carve up
                if temp_start_pos[0]>Logic.ENDPOS[0] and new_maze[temp_start_pos[0]-1][temp_start_pos[1]]=='XXX' and new_maze[temp_start_pos[0]-2][temp_start_pos[1]]==' ':
                        new_maze[temp_start_pos[0]-1][temp_start_pos[1]]=' '
                        poslist.append(temp_start_pos)
                        temp_start_pos=(temp_start_pos[0]-1,temp_start_pos[1])
                        new_maze[temp_start_pos[0]][temp_start_pos[1]] = 'wv'
                #carve down
                elif temp_start_pos[0]<Logic.ENDPOS[0] and new_maze[temp_start_pos[0]+1][temp_start_pos[1]]=='XXX' and new_maze[temp_start_pos[0]+2][temp_start_pos[1]]==' ':
                        new_maze[temp_start_pos[0]+1][temp_start_pos[1]]=' '
                        poslist.append(temp_start_pos)
                        temp_start_pos=(temp_start_pos[0]+1,temp_start_pos[1])
                        new_maze[temp_start_pos[0]][temp_start_pos[1]] = 'wv'
                #carve left
                elif temp_start_pos[1]<Logic.ENDPOS[1] and new_maze[temp_start_pos[0]][temp_start_pos[1]+1]=='XXX' and new_maze[temp_start_pos[0]][temp_start_pos[1]+2]==' ':
                        new_maze[temp_start_pos[0]][temp_start_pos[1]+1]=' '
                        poslist.append(temp_start_pos)
                        temp_start_pos=(temp_start_pos[0],temp_start_pos[1]+1)
                        new_maze[temp_start_pos[0]][temp_start_pos[1]] = 'wv'
                #carve right
                elif temp_start_pos[1]>Logic.ENDPOS[1] and new_maze[temp_start_pos[0]][temp_start_pos[1]-1]=='XXX' and new_maze[temp_start_pos[0]][temp_start_pos[1]-2]==' ':
                        new_maze[temp_start_pos[0]][temp_start_pos[1]-1]=' '
                        poslist.append(temp_start_pos)
                        temp_start_pos=(temp_start_pos[0],temp_start_pos[1]-1)
                        new_maze[temp_start_pos[0]][temp_start_pos[1]] = 'wv'
                else:
                    temp_start_pos,new_maze = self.retrace(poslist,new_maze)
        return new_maze
    def retrace(self,poslist,maze)->tuple:
        '''
        recursive function that goes to previous positions
        :param poslist:
        :param n: number of times to go back a position
        :return:
        '''
        try:
            backone=poslist.pop(-1)

        except IndexError:
            #generates new maze if unable to find find path

            maze=self.maze_generation()
            for row in range(len(maze)):
                for cell in range(len(maze[row])):
                    if maze[row][cell] == 'wv' or maze[row][cell] == 'w':
                        maze[row][cell] = ' '
            backone=Logic.STARTPOS
        return backone,maze

    def maze_display(self,maze:list)->list:
        '''
        displays maze to table
        :return:the maze generation
        '''
        for row in range(len(maze)):
            for cell in range(len(maze[row])):
                if maze[row][cell]=='wv' or maze[row][cell]=='w':
                    maze[row][cell]=' '
                self.maze.setItem(row,cell,QTableWidgetItem(maze[row][cell]))
                if maze[row][cell]=='END':
                    # color end
                    self.maze.item(row, cell).setBackground(QtGui.QColor(225, 62, 58))
                elif maze[row][cell]=='Start':
                    # color start
                    self.maze.item(row, cell).setBackground(QtGui.QColor(243, 225, 66))
                elif maze[row][cell]==' :) ':
                    self.maze.item(row,cell).setBackground(QtGui.QColor(3, 170, 70))
        return maze
         #displays leaderboard
    def display_leaderboard(self):
        '''
        displays leaderboard
        :return:
        '''
        scores=leaderboard.read_board()
        top_5='Leaderboard: '
        for score in scores[:5]:
            top_5=top_5+score+'\n '
        self.LeaderBoardLabel.setText(top_5)
    def __init__(self)->None:
        '''

        '''
        super().__init__()
        self.setupUi(self)
        self.currentPlayerTime = 0
        self.display_leaderboard()
        self.gen_maze=self.maze_generation()
        self.gen_maze=self.maze_display(self.gen_maze)
        self.currentpos=Logic.STARTPOS
        self.timeon=False
        self.end=False
        self.UpButton.clicked.connect(lambda: self.upbutton(self.gen_maze))
        self.DownButton.clicked.connect(lambda: self.downbutton(self.gen_maze))
        self.RightButton.clicked.connect(lambda: self.rightbutton(self.gen_maze))
        self.LeftButton.clicked.connect(lambda: self.leftbutton(self.gen_maze))
        self.maze.keyPressEvent=self.keyPressEvent

    def timerWorker(self):
        self.worker=Timer()
        self.worker.start()
        self.worker.time.connect(self.update_time)

    def update_time(self,val):
        self.currentPlayerTime=val
        self.CurrentTime.setText(f'Current Time: {val}')

    def upbutton(self,maze:list)->list:
        '''
        makes character go up
        :return:updated maze
        '''
        if self.end == False:
            if self.timeon==False:
                self.timeon = True
                self.timerWorker()
            if maze[self.currentpos[0]-1][self.currentpos[1]]==' ':
                maze[self.currentpos[0] - 1][self.currentpos[1]] = ' :) '
                maze[self.currentpos[0]][self.currentpos[1]] = ' '
                self.currentpos=(self.currentpos[0]-1,self.currentpos[1])
                time.sleep(.001)
            if maze[self.currentpos[0] - 1][self.currentpos[1]] == 'END' or maze[self.currentpos[0]][self.currentpos[1] + 1] == 'END' or maze[self.currentpos[0]][self.currentpos[1] - 1] == 'END' or maze[self.currentpos[0] + 1][self.currentpos[1]] == 'END':
                self.worker.requestInterruption()
                print(self.currentPlayerTime)
                self.end=True
                leaderboard.new_score(self.currentPlayerTime)
                self.display_leaderboard()
        return self.maze_display(maze)
    def downbutton(self,maze:list)->list:
        '''
        makes character go up
        :return:updated maze
        '''
        if self.end == False:
            if self.timeon == False:
                self.timeon = True
                self.timerWorker()
            if maze[self.currentpos[0]+1][self.currentpos[1]]==' ':
                maze[self.currentpos[0] + 1][self.currentpos[1]] = ' :) '
                maze[self.currentpos[0]][self.currentpos[1]] = ' '
                self.currentpos=(self.currentpos[0]+1,self.currentpos[1])
                time.sleep(.001)
            if maze[self.currentpos[0] - 1][self.currentpos[1]] == 'END' or maze[self.currentpos[0]][self.currentpos[1] + 1] == 'END' or maze[self.currentpos[0]][self.currentpos[1] - 1] == 'END' or maze[self.currentpos[0] + 1][self.currentpos[1]] == 'END':
                self.worker.requestInterruption()
                print(self.currentPlayerTime)
                self.end=True
                leaderboard.new_score(self.currentPlayerTime)
                self.display_leaderboard()
        return self.maze_display(maze)
    def rightbutton(self,maze:list)->list:
        '''
        makes character go up
        :return:updated maze
        '''
        if self.end == False:
            if self.timeon == False:
                self.timeon = True
                self.timerWorker()
            if maze[self.currentpos[0]][self.currentpos[1]+1]==' ':
                maze[self.currentpos[0]][self.currentpos[1]+1] = ' :) '
                maze[self.currentpos[0]][self.currentpos[1]] = ' '
                self.currentpos=(self.currentpos[0],self.currentpos[1]+1)
                time.sleep(.001)
            if maze[self.currentpos[0] - 1][self.currentpos[1]] == 'END' or maze[self.currentpos[0]][self.currentpos[1] + 1] == 'END' or maze[self.currentpos[0]][self.currentpos[1] - 1] == 'END' or maze[self.currentpos[0] + 1][self.currentpos[1]] == 'END':
                self.worker.requestInterruption()
                print(self.currentPlayerTime)
                self.end=True
                leaderboard.new_score(self.currentPlayerTime)
                self.display_leaderboard()
        return self.maze_display(maze)
    def leftbutton(self,maze:list)->list:
        '''
        makes character go up
        :return:updated maze
        '''
        if self.end == False:
            if self.timeon == False:
                self.timeon = True
                self.timerWorker()
            if maze[self.currentpos[0]][self.currentpos[1]-1]==' ':
                maze[self.currentpos[0]][self.currentpos[1]-1] = ' :) '
                maze[self.currentpos[0]][self.currentpos[1]] = ' '
                self.currentpos=(self.currentpos[0],self.currentpos[1]-1)
                time.sleep(.001)
            if maze[self.currentpos[0] - 1][self.currentpos[1]] == 'END' or maze[self.currentpos[0]][self.currentpos[1] + 1] == 'END' or maze[self.currentpos[0]][self.currentpos[1] - 1] == 'END' or maze[self.currentpos[0] + 1][self.currentpos[1]] == 'END':
                self.worker.requestInterruption()
                print(self.currentPlayerTime)
                self.end=True
                leaderboard.new_score(self.currentPlayerTime)
                self.display_leaderboard()
        return self.maze_display(maze)
    #allows for the ability to use keys to move
    def keyPressEvent(self, event):
        if event.key()==16777235:
            self.upbutton(self.gen_maze)
        elif event.key()==16777237:
            self.downbutton(self.gen_maze)
        elif event.key()==16777236:
            self.rightbutton(self.gen_maze)
        elif event.key()==16777234:
            self.leftbutton(self.gen_maze)
