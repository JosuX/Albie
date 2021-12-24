from PyQt5.QtGui import QPixmap, QIcon, QStandardItem


class Photonode(QStandardItem):
    def __init__(self, id):
        super().__init__()

        self.id = id
        self.name = None
        self.photo = None
        self.caption = None
        self.date = None

    def update(self):
        self.thumbnail = QPixmap()
        self.thumbnail.loadFromData(self.photo)
        self.icon = QIcon(self.thumbnail)
        self.setData(self.id)
        self.setIcon(self.icon)
        self.setText(self.name)
        self.setEditable(False)
        self.setDragEnabled(False)



