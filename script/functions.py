from PyQt5 import QtCore
from PyQt5.QtGui import QPainter, QPixmap
from PyQt5.QtWidgets import QMdiArea
import winreg as wreg

from instabot import Bot
from win32comext.shell import shell, shellcon
import os


def eventFilter(self, object, event):
    if event.type() == QtCore.QEvent.HoverEnter:
        print("In")
        return True
    elif event.type() == QtCore.QEvent.HoverLeave:
        print("Out")
        return False
    else:
        return False

##Static Window Background Class
class paintedcentral(QMdiArea):
    def __init__(self, parent=None):
        QMdiArea.__init__(self, parent=parent)

    def paintEvent(self, event):
        QMdiArea.paintEvent(self, event)
        painter = QPainter(self.viewport())
        background = QPixmap("gui/img/mainscreen_background.png")
        painter.drawPixmap(self.rect(), background)


def icon_assoc():
    sourcepath = os.path.dirname(os.path.abspath(__file__))
    root = wreg.OpenKey(wreg.HKEY_CLASSES_ROOT, sub_key=None, reserved=0,access=wreg.KEY_CREATE_SUB_KEY)
    wreg.CreateKeyEx(root,".alb",reserved=0,access=wreg.KEY_ALL_ACCESS)
    root.Close()

    albkey = wreg.OpenKey(wreg.HKEY_CLASSES_ROOT,".alb",0,access=wreg.KEY_ALL_ACCESS)
    wreg.CreateKey(albkey,"DefaultIcon")
    wreg.SetValue(albkey,"DefaultIcon",wreg.REG_SZ,sourcepath+"\\gui\\img\\file_icon.ico")
    shell.SHChangeNotify(shellcon.SHCNE_ASSOCCHANGED, shellcon.SHCNF_IDLIST, None, None)

def sharetoinstagram(username, password):
    username = username
    password = password

    bot = Bot()
    bot.login(username=username, password=password, is_threaded=True, use_cookie=True, force=True)
    bot.upload_photo("after.txt","This is a test", options={"configure_timeout":5, "rename": False})