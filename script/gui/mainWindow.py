from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPixmap, QPainter, QMovie, QMouseEvent, QIcon
from PyQt5.QtWidgets import QMdiArea, QLabel, QMenu, QAction
import os

sourcepath = os.path.dirname(os.path.abspath(__file__))
class paintedcentral(QMdiArea):
    def __init__(self, parent=None):
        QMdiArea.__init__(self, parent=parent)

    def paintEvent(self, event):
        QMdiArea.paintEvent(self, event)
        painter = QPainter(self.viewport())
        background = QPixmap(sourcepath + "/img/mainscreen_background.png")
        painter.drawPixmap(self.rect(), background)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(960, 540)
        MainWindow.setWindowFlag(Qt.FramelessWindowHint,True)
        MainWindow.setMinimumSize(QtCore.QSize(960, 540))
        MainWindow.setMaximumSize(QtCore.QSize(960, 540))
        font = QtGui.QFont()
        font.setFamily("Monospac821 BT")
        MainWindow.setFont(font)
        self.centralwidget = paintedcentral(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.menu = QMenu()
        self.facebook = QIcon(sourcepath+"/img/social media icons/facebook icon.png")
        self.instagram = QIcon(sourcepath+"/img/social media icons/instagram icon.png")
        self.twitter = QIcon(sourcepath+"/img/social media icons/twitter icon.png")
        self.logo = QIcon(sourcepath+"/img/logo1.jpg")
        self.fb = QAction(self.facebook, "Facebook Page")
        self.insta = QAction(self.instagram, "Instagram")
        self.twit =QAction(self.twitter, "Twitter")
        self.site = QAction(self.logo, "Website")
        self.menu.addAction(self.fb)
        self.menu.addAction(self.insta)
        self.menu.addAction(self.twit)
        self.menu.addAction(self.site)
        menuicon = QIcon()
        self.menu.setIcon(menuicon)
        self.toolButton = QtWidgets.QPushButton(self.frame)
        self.menu.stackUnder(self.frame)
        self.toolButton.setMinimumSize(QtCore.QSize(150, 25))
        self.toolButton.setMaximumSize(QtCore.QSize(150, 25))
        self.toolButton.setMenu(self.menu)
        self.toolButton.clicked.connect(self.toolButton.showMenu)

        font = QtGui.QFont()
        font.setFamily("Phenomena Light")
        font.setPointSize(10)
        self.toolButton.setFont(font)
        stylesheet = """QPushButton{
        background-color: rgb(208, 208, 208);
        border-radius: 10px;}
        QPushButton::menu-indicator{width:0px;}
        """
        self.toolButton.setStyleSheet(stylesheet)
        self.toolButton.setObjectName("toolButton")
        self.horizontalLayout_2.addWidget(self.toolButton)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout.addWidget(self.frame_2)
        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Albie"))
        self.toolButton.setText(_translate("MainWindow", "CONNECT WITH US!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
