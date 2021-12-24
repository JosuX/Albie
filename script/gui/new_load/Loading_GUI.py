from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainLoad(object):
    def setupUi(self, MainLoad):
        MainLoad.setObjectName("MainLoad")
        MainLoad.resize(320, 330)
        MainLoad.setWindowTitle("")
        self.centralwidget = QtWidgets.QWidget(MainLoad)
        self.centralwidget.setObjectName("centralwidget")
        self.container = QtWidgets.QFrame(self.centralwidget)
        self.container.setGeometry(QtCore.QRect(10, 10, 300, 300))
        self.container.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.container.setFrameShadow(QtWidgets.QFrame.Raised)
        self.container.setObjectName("listview")
        self.frame_blue = QtWidgets.QFrame(self.container)
        self.frame_blue.setGeometry(QtCore.QRect(10, 10, 280, 280))
        self.frame_blue.setStyleSheet("QFrame{\n"
                                      "border-radius: 140px;\n"
                                      "background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.749 rgba(255, 255, 255, 0), stop:0.75 rgba(149, 174, 221, 255));\n"
                                      "}")
        self.frame_blue.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_blue.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_blue.setObjectName("frame_blue")
        self.frame_grey = QtWidgets.QFrame(self.container)
        self.frame_grey.setGeometry(QtCore.QRect(10, 10, 280, 280))
        self.frame_grey.setStyleSheet("QFrame{\n"
                                      "\n"
                                      "border-radius: 140px;\n"
                                      "background-color: rgba(163, 163, 163, 100);\n"
                                      "\n"
                                      "}")
        self.frame_grey.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_grey.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_grey.setObjectName("frame_grey")
        self.frame_white = QtWidgets.QFrame(self.container)
        self.frame_white.setGeometry(QtCore.QRect(30, 30, 240, 240))
        self.frame_white.setStyleSheet("QFrame{\n"
                                       "\n"
                                       "border-radius: 120px;\n"
                                       "    background-color: qradialgradient(spread:pad, cx:0.51, cy:0.5, radius:1.805, fx:0.51, fy:0.529, stop:0.00995025 rgba(255, 255, 255, 255), stop:0.756219 rgba(198, 185, 181, 255));\n"
                                       "\n"
                                       "}")
        self.frame_white.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_white.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_white.setObjectName("frame_white")
        self.label_title = QtWidgets.QLabel(self.frame_white)
        self.label_title.setGeometry(QtCore.QRect(40, 10, 161, 101))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet("background-color: None;\n"
                                       "color: rgb(86, 86, 86)")
        self.label_title.setObjectName("label_title")
        self.label_percentage = QtWidgets.QLabel(self.frame_white)
        self.label_percentage.setGeometry(QtCore.QRect(80, 70, 121, 101))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI Light")
        font.setPointSize(52)
        font.setBold(False)
        font.setWeight(50)
        self.label_percentage.setFont(font)
        self.label_percentage.setStyleSheet("background-color: None;\n"
                                            "color: rgb(80, 80, 80)")
        self.label_percentage.setAlignment(QtCore.Qt.AlignCenter)
        self.label_percentage.setObjectName("label_percentage")
        self.label_loading = QtWidgets.QLabel(self.frame_white)
        self.label_loading.setGeometry(QtCore.QRect(80, 180, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_loading.setFont(font)
        self.label_loading.setStyleSheet("QLabel{\n"
                                         "border-radius: 10px;\n"
                                         "}")
        self.label_loading.setAlignment(QtCore.Qt.AlignCenter)
        self.label_loading.setObjectName("label_loading")
        self.frame_grey.raise_()
        self.frame_blue.raise_()
        self.frame_white.raise_()
        MainLoad.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainLoad)
        self.statusbar.setObjectName("statusbar")
        MainLoad.setStatusBar(self.statusbar)

        self.retranslateUi(MainLoad)
        QtCore.QMetaObject.connectSlotsByName(MainLoad)

    def retranslateUi(self, MainLoad):
        _translate = QtCore.QCoreApplication.translate
        self.label_title.setText(_translate("MainLoad", "ALBIE  PHOTOGRAPHY"))
        self.label_percentage.setText(
            _translate("MainLoad", "<p>0<span style=\" font-size:40pt;\">%</span></p><p><br/></p>"))
        self.label_loading.setText(_translate("MainLoad", "loading.."))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainLoad = QtWidgets.QMainWindow()
    ui = Ui_MainLoad()
    ui.setupUi(MainLoad)
    MainLoad.show()
    sys.exit(app.exec_())
