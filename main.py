import os
import sys
import csv
import ast
import webbrowser
import PIL
import atexit
from PIL import Image
from io import BytesIO


from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QThreadPool
from PyQt5.QtGui import QIcon, QKeyEvent, QMouseEvent
from PyQt5.QtWidgets import QFileDialog, QApplication
from instabot import Bot
from os import environ

from script.classes.card import Ui_Card
from script.crypt.crypt import encrypt, decrypt
from script.functions import icon_assoc
from script.gui import mainWindow, createView
from script.gui.instalog import InstaLog
from script.gui.listview_container import UIContainer
from script.gui.loading import Loading_gui
from script.classes.node import Photonode
from script.gui.uploading import Uploading_gui
from script.workers.worker import Worker
from datetime import datetime

dynpath = os.path.dirname(sys.argv[0])
##Uploading Controller
class Uploading(Uploading_gui):
    def __init__(self, *args, obj=None, **kwargs):
        super(Uploading, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon(dynpath + "/script/gui/img/logo1.jpg"))
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.CustomizeWindowHint | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setWindowTitle("Uploading...")

    def uploadingstart(self):
        self.show()
        self.setWindowModality(Qt.ApplicationModal)
        self.widget.startAnimation()

    def uploadingstop(self):
        self.widget.movie.stop()
        self.close()


##Loading Controller
class Loading(Loading_gui):
    def __init__(self, *args, obj=None, **kwargs):
        super(Loading, self).__init__()
        self.setWindowIcon(QIcon(dynpath + "/script/gui/img/logo1.jpg"))
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.CustomizeWindowHint | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setWindowTitle("Loading...")


    def stopAnimation(self):
        self.movie.stop()
        self.close()

    def loadingstart(self):
        self.show()
        self.startAnimation()

    def stopAnimation_cont(self):
        self.movie.stop()
        self.close()

##Start Window Controller
class StartWindow(QtWidgets.QMainWindow, mainWindow.Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(StartWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.id_entrance = 0
        self.setWindowIcon(QIcon(dynpath + "/script/gui/img/logo1.jpg"))
        self.fb.triggered.connect(self.gotofb)
        self.insta.triggered.connect(self.gotoinsta)
        self.twit.triggered.connect(self.gototwitter)
        self.site.triggered.connect(self.gotosite)

    def gotofb(self):
        webbrowser.open('https://www.facebook.com/AlbieGallery', new=2)

    def gotoinsta(self):
        webbrowser.open('https://www.instagram.com/albie_photography/', new=2)

    def gototwitter(self):
        webbrowser.open('https://twitter.com/AlbieGallery',new=2)

    def gotosite(self):
        webbrowser.open('https://albie-photography.business.site/', new=2)

    def keyReleaseEvent(self, event: QKeyEvent):
        if event.key() != None:
            self.moveto_createView()

    def mouseDoubleClickEvent(self, event: QMouseEvent):
        if event.button() == 1:
            self.moveto_createView()

    def moveto_createView(self):
        self.close()
        create_view.show()


##Create View Controller
class CreateWindow(QtWidgets.QMainWindow, createView.Ui_Win_Create):
    def __init__(self, *args, obj=None, **kwargs):
        super(CreateWindow, self).__init__(*args, **kwargs)
        self.filepath = None
        self.id_entrance = 0
        self.setupUi(self)
        self.Button_view.clicked.connect(self.view_album)
        self.Button_create.clicked.connect(self.create_album)
        self.threadpool = QThreadPool()
        self.setWindowIcon(QIcon(dynpath + "/script/gui/img/logo1.jpg"))

    def view_album(self):
        global lines
        global filepath
        get_alb = QFileDialog()
        filepath = get_alb.getOpenFileName(self, 'Open Album file', 'c:\\', "Album (*.alb)")
        self.filepath = filepath
        try:
            file = open(filepath[0], "r", newline="")
        except FileNotFoundError:
            return
        alb_file = csv.reader(file)
        lines = list(alb_file)
        file.close()
        self.close()
        container.show()
        container.loading.loadingstart()

        Jarvis = Worker(self.view_insertq)
        Jarvis.signals.finished.connect(self.insert_finished)
        self.threadpool.start(Jarvis)

    def view_insertq(self):
        global lines
        for row in lines:
            insertnode = Photonode(int(row[0]))
            insertnode.name = row[1]
            insertnode.photo = decrypt(ast.literal_eval(row[2]))
            insertnode.caption = row[3]
            insertnode.date = row[4]
            container.queue.put(insertnode)

    def insert_finished(self):
        Jarvis = Worker(container.loadItems)
        Jarvis.signals.finished.connect(container.loading.stopAnimation_cont)
        self.threadpool.start(Jarvis)


    def create_album(self):
        global filepath
        global photos_in
        global album_file
        global first_half
        global second_half
        global photos
        global mid

        ##Create Album Phase 1
        create_alb = QFileDialog()
        upload_photo = QFileDialog()
        filepath = create_alb.getSaveFileName(self, 'Save Album File', 'c:\\', "Album (*.alb)")
        self.filepath = filepath
        photos_in = upload_photo.getOpenFileNames(self, 'Upload Photo', 'c:\\', "Image Files (*.jpg , *.png)")
        try:
            album_file = open(str(filepath[0]), mode='w', newline='')
        except FileNotFoundError:
            return
        photos = photos_in[0]
        container.show()
        container.loading.loadingstart()
        self.close()

        Jarvis = Worker(self.create_album_jarvis)
        Jarvis.signals.finished.connect(self.create_album_finished)
        self.threadpool.start(Jarvis)

    def create_album_jarvis(self):
        album_writer1 = csv.writer(album_file)
        id = 0
        print(photos)
        for photo in photos:
            id += 1
            filename = os.path.basename(photo)
            data = encrypt(photo)
            now = datetime.now()
            album_writer1.writerow([id, filename, data, "", now])
            insertnode = Photonode(id)
            insertnode.name = filename
            insertnode.photo = decrypt(data)
            insertnode.date = now
            container.queue.put(insertnode)

    def create_album_finished(self):
        Jarvis = Worker(container.loadItems)
        Jarvis.signals.finished.connect(container.loading.stopAnimation_cont)
        self.threadpool.start(Jarvis)
        album_file.close()
        print("Jarvis: Album Creation Finished")


##Container Controller
class Container(QtWidgets.QMainWindow, UIContainer):
    def __init__(self, *args, obj=None, **kwargs):
        super().__init__()
        self.loading = Loading()

        self.setupUi(self)
        self.retranslateUi(self)
        self.gridLayout.addWidget(self.loading,1,0,1,1, Qt.AlignCenter)
        self.loading.setWindowModality(Qt.ApplicationModal)
        self.setWindowIcon(QIcon(dynpath + "/script/gui/img/logo1.jpg"))
        self.card = Card()
        self.backButton.clicked.connect(self.goBack)
        self.setWindowState(Qt.WindowMaximized)
        self.threadpool = QThreadPool()
        self.setAcceptDrops(True)


    def goBack(self):
        self.close()
        self.container_lisview.model.clear()
        create_view.show()

    def loadItems(self):
        while self.queue.qsize() != 0:
            item = self.queue.get()
            item.update()
            self.container_lisview.model.appendRow(item)

    def delete_from_alb(self, datas):
        ##Deleting photos
        filepath = create_view.filepath

        album_read = open(filepath[0], "r", newline="")
        reader = csv.reader(album_read)
        readlist = list(reader)
        templist = list()
        print(datas)
        for data in datas:
            for row in readlist:
                if row[1] == str(data):
                    readlist.remove(row)

        ##ID SORTING
        i = 1
        for row in readlist:
            row[0] = i
            i += 1
        album_read.close()
        album_write = open(filepath[0], "w", newline="")
        writer = csv.writer(album_write)
        writer.writerows(readlist)
        album_write.close()
        j = 1
        container.container_lisview.selectAll()
        for index in self.container_lisview.selectedIndexes():
            item = self.container_lisview.model.itemFromIndex(index)
            item.setData(j)
            item.id = j
            j += 1
        container.container_lisview.clearSelection()
        container.container_lisview.refresh()

    def add_to_alb(self, inputrows):
        filepath = create_view.filepath
        album_write = open(filepath[0], "a", newline="")
        writer = csv.writer(album_write)
        writer.writerows(inputrows)
        self.loadItems()
        album_write.close()


##Card Controller
class Card(QtWidgets.QMainWindow, Ui_Card):
    def __init__(self, *args, obj=None, **kwargs):
        super(Card,self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.setWindowIcon(QIcon(dynpath + "/script/gui/img/logo1.jpg"))
        self.button_back.clicked.connect(self.close)
        self.Button_next_2.clicked.connect(self.callnext)
        self.Button_previous_2.clicked.connect(self.callprev)
        self.button_plus.clicked.connect(self.Widget_Display.zoomIn)
        self.button_minus.clicked.connect(self.Widget_Display.zoomOut)
        self.button_edit.clicked.connect(self.editcaption)
        self.IG_Button.clicked.connect(self.sharetoIG)
        self.editting = 0
        self.threadpool = QThreadPool()

    def sharetoIG(self):
        if instalog.loggedin == 0:
            instalog.show()
        else:
            uploading.uploadingstart()
            Jarvis = Worker(instalog.upload)
            self.threadpool.start(Jarvis)



    def editcaption(self):
        if self.editting == 0:
            self.textEdit.setReadOnly(False)
            self.button_edit.setStyleSheet("QPushButton:hover { color: white }\n"
                                           "QPushButton:hover {font-size:32px}\n"
                                           "QPushButton{\n"
                                           "background-color: rgba(255, 255, 255, 0);\n"
                                           "font-color:( white); \n"
                                           "}\n"
                                           "QPushButton{\n"
                                           "image:url(script/gui/img/edit_icon_enabled.png);\n"
                                           "    color: rgb(255, 255, 255);\n"
                                           "    border-radius: 50px;\n"
                                           "    border-color: beige;\n"
                                           "    font: 18pt \"Phenomena\";\n"
                                           "    min-width: 0em;\n"
                                           "    padding: 0px;\n"
                                           "}")
            self.editting = 1

        elif self.editting == 1:
            self.textEdit.setReadOnly(True)
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
            Jarvis = Worker(self.jarvis_edit)
            container.threadpool.start(Jarvis)
            self.editting = 0

    def jarvis_edit(self):
        filepath = create_view.filepath
        album_read = open(filepath[0], "r", newline="")
        node = container.container_lisview.model.itemFromIndex(self.index)
        ID = node.id
        node.caption = self.textEdit.toPlainText()
        reader = csv.reader(album_read)
        readlist = list(reader)
        album_read.close()
        for row in readlist:
            if row[0] == str(ID):
                row[3] = self.textEdit.toPlainText()
        album_writer = open(filepath[0], "w", newline="")
        writer = csv.writer(album_writer)
        writer.writerows(readlist)
        album_writer.close()

    def keyReleaseEvent(self, event):
        if event.key() == Qt.Key_Left:
            self.callprev()

        if event.key() == Qt.Key_Right:
            self.callnext()


    def callnext(self):
        currentrow = self.index.row()
        if self.index.siblingAtRow(currentrow+1).isValid():
            self.called(self.index.siblingAtRow(currentrow + 1))
        else:
            pass

    def callprev(self):
        currentrow = self.index.row()
        if self.index.siblingAtRow(currentrow - 1).isValid():
            self.called(self.index.siblingAtRow(currentrow - 1))
        else:
            pass

    def called(self, index):
        self.index = index
        self.Widget_Display.zoomCounter = 0
        node = container.container_lisview.model.itemFromIndex(index)
        photo = node.photo
        photo_pixmap = node.thumbnail
        caption = node.caption
        name = node.name
        date = node.date

        img = PIL.Image.open(BytesIO(photo))
        width, height = img.size
        size = sys.getsizeof(photo)
        size = size//1000
        reverse = name[::1]
        reverse = reverse.split('.',1)
        filename = reverse[0][::1]
        filetype = reverse[1][::1]
        filesize = "{:,}".format(size)
        self.Widget_Display.open(photo_pixmap)
        self.textEdit.setText(caption)
        self.label_filename.setText("Filename: " + filename)
        self.label_filetype.setText("File type: " + filetype.upper())
        self.label_size.setText("File size: " + str(filesize) +" KB")
        self.label_date.setText("Date: " + str(date).split(" ")[0])
        self.label_resolution.setText("Image size: " + str(width) + " x " + str(height))
        self.show()

##InstaLog Controller
class InstaLogin(QtWidgets.QMainWindow, InstaLog):
    def __init__(self, *args, obj=None, **kwargs):
        super(InstaLogin,self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.pushButton.clicked.connect(self.login)
        self.loggedin = 0
        self.bot = None
        self.threadpool = QThreadPool()
        Jarvis = Worker(self.createBot)
        self.threadpool.start(Jarvis)

    def createBot(self):
        self.bot = Bot(save_logfile=False)

    def login(self):
        uploading.uploadingstart()
        Jarvis = Worker(self.jarvis_login)
        self.threadpool.start(Jarvis)
        self.close()

    def jarvis_login(self):
        username = self.textEdit_3.text()
        password = self.textEdit_4.text()
        try:
            self.bot.login(username=username, password=password, is_threaded=True, use_cookie=True)
        except:
            print("Account not found.")
            uploading.uploadingstop()
            return
        self.loggedin = 1
        self.upload()

    def upload(self):
        filetype = container.card.label_filetype.text().split(" ")[2]
        file = open("temp." + filetype.lower(), "wb")
        file.write(container.container_lisview.model.itemFromIndex(container.card.index).photo)
        file.close()
        try:
            self.bot.upload_photo("temp." + filetype.lower(),
                                  container.card.textEdit.toPlainText(),
                                  options={"configure_timeout": 5,
                                           "rename": False})
        except InterruptedError:
            uploading.uploadingstop()

##MAIN METHOD

def exit_handler():
    print("Saving...")
    print("Albie is closing...")

def override_where():
    return os.path.abspath("certifi/cacert.pem")


def initialize():
    global Jarvis
    global associated
    global writeassoc
    if hasattr(sys, "frozen"):
        import certifi.core

        os.environ["REQUESTS_CA_BUNDLE"] = override_where()
        certifi.core.where = override_where
        import requests.utils
        import requests.adapters
        requests.utils.DEFAULT_CA_BUNDLE_PATH = override_where()
        requests.adapters.DEFAULT_CA_BUNDLE_PATH = override_where()
    assocpath = "icon.assoc"
    readassoc = open(assocpath, "r")
    associated = readassoc.read()
    readassoc.close()
    writeassoc = open(assocpath, "w")
    if associated == str(0):
        try:
            icon_assoc()
            writeassoc.write("1")
            writeassoc.close()
        except:
            print("User is not admin.")
            writeassoc.write("0")
            writeassoc.close()

atexit.register(exit_handler)
initialize()
environ["QT_DEVICE_PIXEL_RATIO"] = "0"
environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
environ["QT_SCREEN_SCALE_FACTORS"] = "1"
environ["QT_SCALE_FACTOR"] = "1"
QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps,True)
QApplication.setAttribute(Qt.AA_UseSoftwareOpenGL, True)
QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
QApplication.setAttribute(Qt.AA_CompressHighFrequencyEvents,True)
app = QApplication(sys.argv)
uploading = Uploading()
start_window = StartWindow()
start_window.show()
container = Container()
create_view = CreateWindow()
instalog = InstaLogin()
app.exec_()
