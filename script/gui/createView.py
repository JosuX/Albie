import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

sourcepath = os.path.dirname(os.path.abspath(__file__))


class Ui_Win_Create(object):
    def setupUi(self, AlbiePhotography):
        AlbiePhotography.setObjectName("AlbiePhotography")
        AlbiePhotography.resize(960, 540)
        AlbiePhotography.setWindowTitle("Albie")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../python_case_study/logoooo/logo1.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AlbiePhotography.setWindowIcon(icon)
        AlbiePhotography.setWindowFlag(Qt.FramelessWindowHint, True)
        AlbiePhotography.setStyleSheet("QMainWindow{\n"
"image:url(script/gui/img/overlay no resize .png);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(AlbiePhotography)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.Frame_All_Attr = QtWidgets.QFrame(self.centralwidget)
        self.Frame_All_Attr.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Frame_All_Attr.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Frame_All_Attr.setObjectName("Frame_All_Attr")
        self.gridLayout = QtWidgets.QGridLayout(self.Frame_All_Attr)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 4, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 5, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 0, 0, 1, 1)
        self.Container_button = QtWidgets.QHBoxLayout()
        self.Container_button.setObjectName("Container_button")
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.Container_button.addItem(spacerItem4)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.Container_button.addItem(spacerItem5)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.Container_button.addItem(spacerItem6)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.Container_button.addItem(spacerItem7)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.Container_button.addItem(spacerItem8)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.Container_button.addItem(spacerItem9)
        self.Button_create = QtWidgets.QPushButton(self.Frame_All_Attr)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_create.sizePolicy().hasHeightForWidth())
        self.Button_create.setSizePolicy(sizePolicy)
        self.Button_create.setMinimumSize(QtCore.QSize(0, 332))
        self.Button_create.setMaximumSize(QtCore.QSize(237, 332))
        self.Button_create.setStyleSheet("QPushButton:hover { color: white }\n"
"QPushButton:hover {font-size:32px}\n"
"QPushButton{\n"
"background-color: rgba(255, 255, 255, 0);\n"
"\n"
"}\n"
"QPushButton{\n"
"image:url(script/gui/img/create_album_icon.png);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 50px;\n"
"    border-color: beige;\n"
"    font: 18pt \"Phenomena\";\n"
"    min-width: 0em;\n"
"    padding: 0px;\n"
"}")
        self.Button_create.setObjectName("Button_Create")
        self.Container_button.addWidget(self.Button_create)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.Container_button.addItem(spacerItem10)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.Container_button.addItem(spacerItem11)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.Container_button.addItem(spacerItem12)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.Container_button.addItem(spacerItem13)
        spacerItem14 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.Container_button.addItem(spacerItem14)
        self.Button_view = QtWidgets.QPushButton(self.Frame_All_Attr)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_view.sizePolicy().hasHeightForWidth())
        self.Button_view.setSizePolicy(sizePolicy)
        self.Button_view.setMinimumSize(QtCore.QSize(0, 332))
        self.Button_view.setMaximumSize(QtCore.QSize(237, 332))
        self.Button_view.setStyleSheet("QPushButton:hover { color: white }\n"
"QPushButton:hover {font-size:32px}\n"
"QPushButton{\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font-color:( white); \n"
"}\n"
"QPushButton{\n"
"image:url(script/gui/img/view_icon.png);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 50px;\n"
"    border-color: beige;\n"
"    font: 18pt \"Phenomena\";\n"
"    min-width: 0em;\n"
"    padding: 0px;\n"
"}")
        self.Button_view.setObjectName("Button_View")
        self.Container_button.addWidget(self.Button_view)
        spacerItem15 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.Container_button.addItem(spacerItem15)
        spacerItem16 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.Container_button.addItem(spacerItem16)
        spacerItem17 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.Container_button.addItem(spacerItem17)
        spacerItem18 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.Container_button.addItem(spacerItem18)
        spacerItem19 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.Container_button.addItem(spacerItem19)
        self.gridLayout.addLayout(self.Container_button, 3, 0, 1, 1)
        spacerItem20 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem20, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.Frame_All_Attr, 0, 0, 1, 1)
        AlbiePhotography.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(AlbiePhotography)
        self.statusbar.setObjectName("statusbar")
        AlbiePhotography.setStatusBar(self.statusbar)

        self.retranslateUi(AlbiePhotography)
        QtCore.QMetaObject.connectSlotsByName(AlbiePhotography)

    def retranslateUi(self, AlbiePhotography):
        _translate = QtCore.QCoreApplication.translate
        AlbiePhotography.setWindowTitle(_translate("AlbiePhotography", "Albie"))
        self.Button_create.setText(_translate("AlbiePhotography", "\n"
"\n"
"\n"
"\n"
"Create Album"))
        self.Button_create.setShortcut(_translate("AlbiePhotography", "Ctrl+C"))
        self.Button_view.setText(_translate("AlbiePhotography", "\n"
"\n"
"\n"
"\n"
"View Album"))
        self.Button_view.setShortcut(_translate("AlbiePhotography", "Ctrl+V"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AlbiePhotography = QtWidgets.QMainWindow()
    ui = Ui_Win_Create()
    ui.setupUi(AlbiePhotography)
    AlbiePhotography.show()
    sys.exit(app.exec_())
