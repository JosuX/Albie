from queue import Queue

from PyQt5 import QtCore, QtGui, QtWidgets

from script.classes.listview import PhotoList


class UIContainer(object):
    def __init__(self):
        self.queue = Queue()


    def setupUi(self, AlbiePhotography):
        AlbiePhotography.setObjectName("AlbiePhotography")
        AlbiePhotography.resize(960, 540)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../ALL PICTURES/logo1.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AlbiePhotography.setWindowIcon(icon)
        AlbiePhotography.setStyleSheet("\n"
                                           "QMainWindow{\n"
                                           "background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:1.805, fx:0.5, fy:0.5, stop:0.0497512 rgba(166, 166, 166, 255), stop:0.880597 rgba(117, 117, 109, 255));\n"
                                           "}")
        self.centralwidget = QtWidgets.QWidget(AlbiePhotography)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        self.backButton.setMaximumSize(QtCore.QSize(50, 16777215))
        self.backButton.setStyleSheet("QPushButton:hover { color: white }\n"
                                          "QPushButton:hover {font-size:32px}\n"
                                          "QPushButton{\n"
                                          "background-color: rgba(255, 255, 255, 0);\n"
                                          "\n"
                                          "}\n"
                                          "QPushButton{\n"
                                          "image:url(script/gui/img/back button.png);\n"
                                          "    color: rgb(255, 255, 255);\n"
                                          "    border-radius: 50px;\n"
                                          "    border-color: beige;\n"
                                          "    font: 18pt \"Phenomena\";\n"
                                          "    min-width: 0em;\n"
                                          "    padding: 0px;\n"
                                          "}")
        self.backButton.setText("")
        self.backButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.backButton)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setMinimumSize(QtCore.QSize(330, 40))
        self.label_title.setMaximumSize(QtCore.QSize(300, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI Light")
        font.setPointSize(14)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet("image:url(script/gui/img/window_3.png);")
        self.label_title.setText("")
        self.label_title.setScaledContents(True)
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.horizontalLayout.addWidget(self.label_title)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.container_lisview = PhotoList()
        self.container_lisview.setStyleSheet("")
        self.container_lisview.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.container_lisview.setFrameShadow(QtWidgets.QFrame.Plain)
        self.container_lisview.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.container_lisview.setObjectName("container_lisview")
        self.gridLayout.addWidget(self.container_lisview, 1, 0, 1, 1)
        AlbiePhotography.setCentralWidget(self.centralwidget)

        self.retranslateUi(AlbiePhotography)
        QtCore.QMetaObject.connectSlotsByName(AlbiePhotography)


    def retranslateUi(self, AlbiePhotography):
        _translate = QtCore.QCoreApplication.translate
        AlbiePhotography.setWindowTitle(_translate("AlbiePhotography", "Albie"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AlbiePhotography = QtWidgets.QMainWindow()
    ui = UIContainer()
    ui.setupUi(AlbiePhotography)
    AlbiePhotography.show()
    sys.exit(app.exec_())
