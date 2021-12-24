
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QWidget, QLabel, QApplication


class Loading_gui(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(800, 600)
        self.label_animation = QLabel(self)
        self.movie = QMovie('script/gui/img/loading.gif')
        self.label_animation.setMovie(self.movie)
        self.label_animation.setAttribute(Qt.WA_TranslucentBackground, True)
        self.label_animation.setWindowFlags(Qt.FramelessWindowHint)
        self.startAnimation()

    def startAnimation(self):
        self.movie.start()


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    loading = Loading_gui()
    loading.show()
    sys.exit(app.exec_())
