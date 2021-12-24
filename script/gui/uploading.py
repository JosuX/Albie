from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow

from script.gui.loading import Loading_gui


class Uploading_gui(QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 300)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(300, 300))
        MainWindow.setMaximumSize(QtCore.QSize(300, 300))
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(70, 180, 160, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.container_txt = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.container_txt.setContentsMargins(0, 0, 0, 0)
        self.container_txt.setObjectName("container_txt")
        self.label_uploading = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Phenomena")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_uploading.setFont(font)
        self.label_uploading.setAlignment(QtCore.Qt.AlignCenter)
        self.label_uploading.setObjectName("label_uploading")
        self.container_txt.addWidget(self.label_uploading)
        self.label_PW = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Phenomena")
        font.setPointSize(10)
        self.label_PW.setFont(font)
        self.label_PW.setAlignment(QtCore.Qt.AlignCenter)
        self.label_PW.setObjectName("label_PW")
        self.container_txt.addWidget(self.label_PW)
        self.widget = Loading_gui()
        self.widget.setParent(self.centralwidget)
        self.widget.label_animation.setFixedSize(301,226)
        self.widget.label_animation.setScaledContents(True)
        self.widget.setGeometry(QtCore.QRect(0, 0, 301, 301))
        self.widget.setObjectName("widget")
        self.widget.raise_()
        self.verticalLayoutWidget.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_uploading.setText(_translate("MainWindow", "UPLOADING"))
        self.label_PW.setText(_translate("MainWindow", "please wait..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Uploading_gui()
    ui.setAttribute(Qt.WA_TranslucentBackground, True)
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
