import os
from datetime import datetime

from PyQt5.QtCore import QSize, QThreadPool
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtWidgets import QListView, QMenu, QFileDialog, QAbstractItemView

from script.classes.node import Photonode
from script.crypt.crypt import encrypt_bytes
from script.workers.worker import Worker


class PhotoList(QListView):
    def __init__(self):
        super().__init__()
        self.threadpool = QThreadPool()
        self.large = QSize()
        self.large.setWidth(240)
        self.large.setHeight(135)
        self.model = QStandardItemModel(self)
        self.setModel(self.model)
        self.setMovement(0)
        self.setViewMode(1)
        self.setIconSize(self.large)
        self.setSpacing(45)
        self.setResizeMode(1)
        self.setAcceptDrops(True)
        self.setSelectionMode(3)
        self.setDropIndicatorShown(True)
        self.setDragDropOverwriteMode(True)
        self.setDragDropMode(QAbstractItemView.DropOnly)
        self.formats = ('.jpg', '.png', '.jpeg', '.gif',
                        '.JPG', '.PNG', '.JPEG', '.GIF')

    def mouseDoubleClickEvent(self, event):
        if event.button() == 1:
            item = self.indexAt(event.pos())
            node = self.model.itemFromIndex(item)
            print(node.data())
            if item.isValid():
                self.parent().parent().card.called(item)
            else:
                print("No item selected.")

    def contextMenuEvent(self, event):
        global item_data
        global ext
        item = self.indexAt(event.pos())
        try:
            item_data = self.model.itemFromIndex(item)
            ext = os.path.splitext(item_data.name)[1]
        except AttributeError:
            pass
        if item.isValid():
            item_menu = QMenu(self)
            view = item_menu.addAction("View")
            export = item_menu.addAction("Export")
            delete = item_menu.addAction("Delete")
            action = item_menu.exec_(self.mapToGlobal(event.pos()))

            if action == view:
                item_data.card.show()

            if action == export:
                Jarvis = Worker(self.export_photo)
                self.threadpool.start(Jarvis)

            if action == delete:
                rows = set()
                items = self.selectedIndexes()
                datas = list()


                for item in items:
                    datas.append(item.model().data(item))
                    rows.add(item.row())

                for row in sorted(rows, reverse=True):
                    self.model.removeRow(row)
                Jarvis = Worker(self.parent().parent().delete_from_alb, datas)
                self.threadpool.start(Jarvis)

        else:
            blank_menu = QMenu(self)
            refresh = blank_menu.addAction("Refresh")
            file_import = blank_menu.addAction("Import")
            action = blank_menu.exec_(self.mapToGlobal(event.pos()))

            if action == refresh:
                self.refresh()

            if action == file_import:
                receive_file = QFileDialog()
                photos = receive_file.getOpenFileNames(self, 'Upload Photo', 'c:\\', "Image Files (*.jpg , *.png)")
                photos = photos[0]
                Jarvis = Worker(self.import_photo,photos)
                self.threadpool.start(Jarvis)

    def export_photo(self):
        out_loc = QFileDialog()
        file_export = out_loc.getSaveFileName(self, 'Export Photo', 'c:\\', "Photo ( *" + ext + ")")
        try:
            exporter = open(file_export[0], "wb")
            exporter.write(item_data.photo)
            exporter.close()
        except FileNotFoundError:
            print("No file selected.")

    def import_photo(self, photos):
        inputrows = list()
        j = 1
        self.selectAll()
        for index in self.selectedIndexes():
            j += 1
        self.clearSelection()
        j += 1
        for photo in photos:
            file = open(photo, "rb")
            bytes = file.read()
            file.close()
            filename = os.path.basename(photo)
            now = datetime.now()
            insertnode = Photonode(j)
            insertnode.name = filename
            insertnode.photo = bytes
            insertnode.date = now
            insertnode.update()
            self.model.appendRow(insertnode)
            input = [j, filename, encrypt_bytes(bytes), "", now]
            inputrows.append(input)
            j += 1
        self.parent().parent().add_to_alb(inputrows)

    def refresh(self):
        self.model.beginResetModel()
        self.model.parent().parent().parent().loadItems()
        self.model.endResetModel()

    def dragEnterEvent(self, event):
        global file, areImages
        areImages = 0
        mime = event.mimeData()
        print(mime)
        try:
            for files in mime.urls():
                file = files.path()[1:]
                if file.endswith(self.formats):
                    areImages = 0
                else:
                    areImages += 1
            if areImages == 0 and os.path.isfile(file):
                event.accept()
            else:
                event.ignore()

        except IndexError or NameError:
            event.accept()

    def dragMoveEvent(self, event):
        global file
        mime = event.mimeData()
        try:
            file = mime.urls()[0].path()[1:]
            if file.endswith(self.formats) and os.path.isfile(file):
                event.accept()
            else:
                event.ignore()
        except IndexError or NameError:
            event.accept()

    def dragLeaveEvent(self, event):
        if event.spontaneous():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        event.accept()
        mime = event.mimeData()
        photos = list()
        try:
            for files in mime.urls():
                file = files.path()[1:]
                photos.append(file)
            Jarvis = Worker(self.import_photo, photos)
            self.threadpool.start(Jarvis)
        except IndexError or NameError:
            pass
