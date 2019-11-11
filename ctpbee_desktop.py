import os
import sys
import platform

from PySide2.QtGui import QIcon, QPixmap
from PySide2.QtWidgets import QApplication

from app.lib.get_path import init_file
from app.main import MainWindow

if __name__ == '__main__':

    if platform.system() == 'Windows':
        import PySide2

        dirname = os.path.dirname(PySide2.__file__)
        plugin_path = os.path.join(dirname, 'plugins', 'platforms')
        os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path

        import ctypes
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")

    init_file()
    app = QApplication(sys.argv)

    window = MainWindow()
    icon = QIcon()
    icon.addPixmap(QPixmap("bee2.ico"), QIcon.Normal, QIcon.Off)
    window.setWindowIcon(icon)
    window.show()

    sys.exit(app.exec_())
