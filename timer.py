import time
from PyQt6.QtCore import *
class Timer(QThread):
    time=pyqtSignal(int)

    def run(self)->None:
        '''
        Starts thread
        :return:
        '''
        num=1
        while True:
            time.sleep(1)
            self.time.emit(num)
            num+=1
            if QThread.isInterruptionRequested(self):
                break

