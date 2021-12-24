import sys


from PyQt5 import QtWidgets
from PyQt5.QtCore import QThreadPool
from PyQt5.QtWidgets import *

from denne.Loading_GUI import Ui_MainLoad
from script.workers.worker import Worker

j = 0
class Loading(QtWidgets.QMainWindow, Ui_MainLoad):
    def __init__(self, *args, obj=None, **kwargs):
        super().__init__()
        global Jarvis
        self.threadpool = QThreadPool()
        self.setupUi(self)
        self.retranslateUi(self)
        self.show()
        Jarvis = Worker(self.loadcount)
        self.threadpool.start(Jarvis)

    def loadcount(self):
        global j
        global Jarvis
        while j != 100:
            j += 1
            self.blue_progress(j)
            self.threadpool.thread().sleep(1)

    def blue_progress(self, value):
        # progress stylesheet
        stylesheet = """
        QFrame{
            border-radius: 140px;
            background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP_1} rgba(255, 255, 255, 0), stop:{STOP_2} rgba(149, 174, 221, 255));
        }
       " """
        progress = (100 - value) / 100.0
        stop_1 = str(progress - 0.001)
        stop_2 = str(progress)
        newStylesheet = stylesheet.replace("{STOP_1}", stop_1).replace("{STOP_2}", stop_2)
        self.frame_blue.setStyleSheet(newStylesheet)
        self.label_percentage.setText(str(value) +"%")
        self.frame_blue.update()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Loading()
    sys.exit(app.exec_())
