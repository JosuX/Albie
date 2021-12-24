from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon

from script.gui.imageview_widget import QImageViewer


class Ui_Card(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1007, 598)
        MainWindow.setMinimumSize(QtCore.QSize(960, 540))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../ALL PICTURES/logo1.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("\n"
"QMainWindow{\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:1.805, fx:0.5, fy:0.5, stop:0.0497512 rgba(166, 166, 166, 255), stop:0.880597 rgba(117, 117, 109, 255));\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.button_back = QtWidgets.QPushButton(self.centralwidget)
        self.button_back.setMaximumSize(QtCore.QSize(50, 50))
        self.button_back.setStyleSheet("QPushButton:hover { color: white }\n"
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
        self.button_back.setText("")
        self.button_back.setObjectName("button_back")
        self.horizontalLayout.addWidget(self.button_back)
        self.ignorethis5 = QtWidgets.QLabel(self.centralwidget)
        self.ignorethis5.setMaximumSize(QtCore.QSize(16777215, 50))
        self.ignorethis5.setText("")
        self.ignorethis5.setObjectName("ignorethis5")
        self.horizontalLayout.addWidget(self.ignorethis5)
        self.ignorethis4 = QtWidgets.QLabel(self.centralwidget)
        self.ignorethis4.setMaximumSize(QtCore.QSize(16777215, 50))
        self.ignorethis4.setText("")
        self.ignorethis4.setObjectName("ignorethis4")
        self.horizontalLayout.addWidget(self.ignorethis4)
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_title.sizePolicy().hasHeightForWidth())
        self.label_title.setSizePolicy(sizePolicy)
        self.label_title.setMinimumSize(QtCore.QSize(400, 45))
        self.label_title.setMaximumSize(QtCore.QSize(400, 50))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI Light")
        font.setPointSize(14)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet("image:url(script/gui/img/window_4.png);")
        self.label_title.setText("")
        self.label_title.setScaledContents(True)
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.horizontalLayout.addWidget(self.label_title)
        self.ignore_this1 = QtWidgets.QLabel(self.centralwidget)
        self.ignore_this1.setMaximumSize(QtCore.QSize(16777215, 50))
        self.ignore_this1.setText("")
        self.ignore_this1.setObjectName("ignore_this1")
        self.horizontalLayout.addWidget(self.ignore_this1)
        self.ignorethis2 = QtWidgets.QLabel(self.centralwidget)
        self.ignorethis2.setMaximumSize(QtCore.QSize(16777215, 50))
        self.ignorethis2.setText("")
        self.ignorethis2.setObjectName("ignorethis2")
        self.horizontalLayout.addWidget(self.ignorethis2)
        self.ignorethis3 = QtWidgets.QLabel(self.centralwidget)
        self.ignorethis3.setMaximumSize(QtCore.QSize(50, 50))
        self.ignorethis3.setText("")
        self.ignorethis3.setObjectName("ignorethis3")
        self.horizontalLayout.addWidget(self.ignorethis3)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(983, 520))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 3, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem1, 1, 1, 1, 1)
        self.container_button_MaxMin = QtWidgets.QHBoxLayout()
        self.container_button_MaxMin.setSpacing(10)
        self.container_button_MaxMin.setObjectName("container_button_MaxMin")
        self.button_plus = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_plus.sizePolicy().hasHeightForWidth())
        self.button_plus.setSizePolicy(sizePolicy)
        self.button_plus.setMinimumSize(QtCore.QSize(0, 30))
        self.button_plus.setMaximumSize(QtCore.QSize(150, 30))
        font = QtGui.QFont()
        font.setFamily("Phenomena")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.button_plus.setFont(font)
        self.button_plus.setStyleSheet("QPushButton:hover { color: white }\n"
"QPushButton {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0.0597015 rgba(200, 197, 184, 255), stop:1 rgba(143, 206, 213, 255));\n"
"    border-width: 8px;\n"
"    border-radius: 15px;\n"
"    border-color: beige;\n"
"    min-width: 0em;\n"
"    padding: 0px;\n"
"}")
        self.button_plus.setObjectName("button_plus")
        self.container_button_MaxMin.addWidget(self.button_plus)
        self.button_minus = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_minus.sizePolicy().hasHeightForWidth())
        self.button_minus.setSizePolicy(sizePolicy)
        self.button_minus.setMinimumSize(QtCore.QSize(0, 30))
        self.button_minus.setMaximumSize(QtCore.QSize(150, 30))
        font = QtGui.QFont()
        font.setFamily("Phenomena")
        font.setPointSize(20)
        self.button_minus.setFont(font)
        self.button_minus.setStyleSheet("QPushButton:hover { color: white }\n"
"\n"
"QPushButton {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0.0597015 rgba(200, 197, 184, 255), stop:1 rgba(143, 206, 213, 255));\n"
"    border-width: 8px;\n"
"    border-radius: 15px;\n"
"    border-color: beige;\n"
"    min-width: 0em;\n"
"    padding: 0px;\n"
"}")
        self.button_minus.setObjectName("button_minus")
        self.container_button_MaxMin.addWidget(self.button_minus)
        self.gridLayout_3.addLayout(self.container_button_MaxMin, 2, 1, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.textEdit = QtWidgets.QTextEdit(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setMinimumSize(QtCore.QSize(10, 140))
        self.textEdit.setMaximumSize(QtCore.QSize(600, 600))
        self.textEdit.setStyleSheet("QTextEdit{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-style: outset;\n"
"    border-width: 5px;\n"
"    border-radius: 15px;\n"
"    border-color: grey;\n"
"    font: 25 8pt \"Microsoft JhengHei UI Light\";\n"
"    min-width: 0em;\n"
"    padding: 0px;\n"
"}")
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout_3.addWidget(self.textEdit)
        self.button_edit = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_edit.sizePolicy().hasHeightForWidth())
        self.button_edit.setSizePolicy(sizePolicy)
        self.button_edit.setMinimumSize(QtCore.QSize(0, 25))
        self.button_edit.setMaximumSize(QtCore.QSize(25, 25))
        self.button_edit.setStyleSheet("QPushButton:hover { color: white }\n"
"QPushButton:hover {font-size:32px}\n"
"QPushButton{\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font-color:( white); \n"
"}\n"
"QPushButton{\n"
"image:url(script/gui/img/editicon.png);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 50px;\n"
"    border-color: beige;\n"
"    font: 18pt \"Phenomena\";\n"
"    min-width: 0em;\n"
"    padding: 0px;\n"
"}")
        self.button_edit.setText("")
        self.button_edit.setObjectName("button_edit")
        self.horizontalLayout_3.addWidget(self.button_edit)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.label_filename = QtWidgets.QLabel(self.frame)
        self.label_filename.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_filename.setObjectName("label_filename")
        self.verticalLayout_3.addWidget(self.label_filename)
        self.label_filetype = QtWidgets.QLabel(self.frame)
        self.label_filetype.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_filetype.setObjectName("label_filetype")
        self.verticalLayout_3.addWidget(self.label_filetype)
        self.label_date = QtWidgets.QLabel(self.frame)
        self.label_date.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_date.setObjectName("label_date")
        self.verticalLayout_3.addWidget(self.label_date)
        self.label_size = QtWidgets.QLabel(self.frame)
        self.label_size.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_size.setObjectName("label_size")
        self.verticalLayout_3.addWidget(self.label_size)
        self.label_resolution = QtWidgets.QLabel(self.frame)
        self.label_resolution.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_resolution.setObjectName("label_resolution")
        self.verticalLayout_3.addWidget(self.label_resolution)
        self.label_share = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_share.sizePolicy().hasHeightForWidth())
        self.label_share.setSizePolicy(sizePolicy)
        self.label_share.setMinimumSize(QtCore.QSize(250, 30))
        self.label_share.setMaximumSize(QtCore.QSize(300, 30))
        self.label_share.setStyleSheet("image:url(script/gui/img/share_on_social_media.png);")
        self.label_share.setText("")
        self.label_share.setAlignment(QtCore.Qt.AlignCenter)
        self.label_share.setObjectName("label_share")
        self.verticalLayout_3.addWidget(self.label_share)
        self.Container_SocialIcon_2 = QtWidgets.QHBoxLayout()
        self.Container_SocialIcon_2.setObjectName("Container_SocialIcon_2")
        self.IG_Button = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.IG_Button.sizePolicy().hasHeightForWidth())
        self.IG_Button.setSizePolicy(sizePolicy)
        self.IG_Button.setMinimumSize(QtCore.QSize(40, 40))
        self.IG_Button.setMaximumSize(QtCore.QSize(50, 50))
        self.IG_Button.setText("")
        icon = QIcon()
        icon.addPixmap(QtGui.QPixmap("script/gui/img/social media icons/instagram icon.png"))
        self.IG_Button.setIcon(icon)
        size = QSize()
        size.setHeight(45)
        size.setWidth(45)
        self.IG_Button.setIconSize(size)
        self.IG_Button.setStyleSheet("QPushButton:hover { color: white }\n"
                                        "\n"
                                        "QPushButton {\n"
                                        "background-color: rgba(255, 255, 255, 0);\n"
                                        "    border-width: 8px;\n"
                                        "    border-radius: 15px;\n"
                                        "    border-color: beige;\n"
                                        "    min-width: 0em;\n"
                                        "    padding: 0px;\n"
                                        "}")
        self.IG_Button.setObjectName("Icon_IG_2")
        self.Container_SocialIcon_2.addWidget(self.IG_Button)
        self.verticalLayout_3.addLayout(self.Container_SocialIcon_2)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_3.addItem(spacerItem2)
        self.Container_Button_2 = QtWidgets.QHBoxLayout()
        self.Container_Button_2.setSpacing(10)
        self.Container_Button_2.setObjectName("Container_Button_2")
        self.Button_previous_2 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_previous_2.sizePolicy().hasHeightForWidth())
        self.Button_previous_2.setSizePolicy(sizePolicy)
        self.Button_previous_2.setMinimumSize(QtCore.QSize(16, 40))
        self.Button_previous_2.setMaximumSize(QtCore.QSize(150, 50))
        self.Button_previous_2.setStyleSheet("QPushButton:hover { color: white }\n"
"QPushButton {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0.0597015 rgba(200, 197, 184, 255), stop:1 rgba(143, 206, 213, 255));\n"
"    border-style: outset;\n"
"    border-width: 8px;\n"
"    border-radius: 15px;\n"
"    border-color: beige;\n"
"    font: 25 8pt \"Microsoft JhengHei UI Light\";\n"
"    min-width: 0em;\n"
"    padding: 0px;\n"
"}")
        self.Button_previous_2.setObjectName("Button_previous_2")
        self.Container_Button_2.addWidget(self.Button_previous_2)
        self.Button_next_2 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_next_2.sizePolicy().hasHeightForWidth())
        self.Button_next_2.setSizePolicy(sizePolicy)
        self.Button_next_2.setMinimumSize(QtCore.QSize(16, 40))
        self.Button_next_2.setMaximumSize(QtCore.QSize(150, 50))
        self.Button_next_2.setStyleSheet("QPushButton:hover { color: white }\n"
"\n"
"QPushButton {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0.0597015 rgba(200, 197, 184, 255), stop:1 rgba(143, 206, 213, 255));\n"
"    border-style: outset;\n"
"    border-width: 8px;\n"
"    border-radius: 15px;\n"
"    border-color: beige;\n"
"    font: 25 8pt \"Microsoft JhengHei UI Light\";\n"
"    min-width: 0em;\n"
"    padding: 0px;\n"
"}")
        self.Button_next_2.setObjectName("Button_next_2")
        self.Container_Button_2.addWidget(self.Button_next_2)
        self.verticalLayout_3.addLayout(self.Container_Button_2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem3)
        self.gridLayout_3.addLayout(self.verticalLayout_3, 0, 3, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem4, 0, 2, 1, 1)
        self.Widget_Display = QImageViewer()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(255)
        sizePolicy.setVerticalStretch(255)
        sizePolicy.setHeightForWidth(self.Widget_Display.sizePolicy().hasHeightForWidth())
        self.Widget_Display.setSizePolicy(sizePolicy)
        self.Widget_Display.setMinimumSize(QtCore.QSize(700, 400))
        self.Widget_Display.setMaximumSize(QtCore.QSize(1920, 1080))
        self.Widget_Display.setObjectName("Widget_Display")
        self.gridLayout_3.addWidget(self.Widget_Display, 0, 1, 1, 1)
        self.horizontalLayout_2.addWidget(self.frame)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Albie"))
        self.button_plus.setText(_translate("MainWindow", "+"))
        self.button_plus.setShortcut(_translate("MainWindow", "Left"))
        self.button_minus.setText(_translate("MainWindow", "-"))
        self.button_minus.setShortcut(_translate("MainWindow", "Right"))
        self.textEdit.setPlaceholderText(_translate("MainWindow", "you can add your caption here!"))
        self.label_filename.setText(_translate("MainWindow", "Filename:"))
        self.label_filetype.setText(_translate("MainWindow", "File Type:"))
        self.label_date.setText(_translate("MainWindow", "Date:"))
        self.label_size.setText(_translate("MainWindow", "Size:"))
        self.label_resolution.setText(_translate("MainWindow", "Resolution:"))
        self.Button_previous_2.setText(_translate("MainWindow", "previous"))
        self.Button_previous_2.setShortcut(_translate("MainWindow", "Left"))
        self.Button_next_2.setText(_translate("MainWindow", "next"))
        self.Button_next_2.setShortcut(_translate("MainWindow", "Right"))
        self.textEdit.setReadOnly(True)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Card()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
