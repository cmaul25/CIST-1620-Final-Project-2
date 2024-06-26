import time
from PyQt6.QtCore import *
class Timer(QThread):
    '''
    Timer Thread
    '''
    time=pyqtSignal(int)

    def run(self)->None:
        '''
        Starts thread
        :return:
        '''
        num=0
        while True:
            time.sleep(1)
            num += 1
            self.time.emit(num)
            if QThread.isInterruptionRequested(self):
                break

