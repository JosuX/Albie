from PyQt5 import QtCore, QtGui, QtWidgets


class InstaLog(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(960, 540)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(960, 540))
        MainWindow.setMaximumSize(QtCore.QSize(960, 540))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("script/gui/img/logo1.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(245, 245, 245);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(320, 80, 300, 120))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(200, 120))
        self.label_2.setMaximumSize(QtCore.QSize(300, 300))
        self.label_2.setStyleSheet("image:url(script/gui/img/instagram letter icon1.png);")
        self.label_2.setText("")
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.textEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(280, 205, 400, 40))
        self.textEdit_3.setMinimumSize(QtCore.QSize(400, 40))
        self.textEdit_3.setMaximumSize(QtCore.QSize(400, 40))
        self.textEdit_3.setStyleSheet("    border-radius: 10px;\n"
"\n"
"background-color: rgb(234, 234, 234);")
        self.textEdit_3.setObjectName("textEdit_3")
        self.textEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.textEdit_4.setGeometry(QtCore.QRect(280, 270, 400, 40))
        self.textEdit_4.setMinimumSize(QtCore.QSize(400, 40))
        self.textEdit_4.setMaximumSize(QtCore.QSize(400, 40))
        self.textEdit_4.setEchoMode(QtWidgets.QLineEdit.Password)
        self.textEdit_4.setStyleSheet("\n"
"border-radius: 10px;\n"
"background-color: rgb(234, 234, 234);")
        self.textEdit_4.setObjectName("textEdit_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(350, 330, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(16, 140, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.pushButton.setAutoDefault(False)
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Albie"))
        self.textEdit_3.setPlaceholderText(_translate("MainWindow", "Username"))
        self.textEdit_4.setPlaceholderText(_translate("MainWindow", "Password"))
        self.pushButton.setText(_translate("MainWindow", "Log in"))


if __name__ == "__main__":
    import sys
    import os
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = InstaLog()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
