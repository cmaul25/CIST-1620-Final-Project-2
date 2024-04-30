from PyQt6.QtWidgets import *
from gui import *


class Logic(QMainWindow, Ui_Maze):
        def __init__(self)->None:
            '''

            '''
            super().__init__()
            self.setupUi(self)