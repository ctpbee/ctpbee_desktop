import sys

from PySide2.QtWidgets import QApplication

from app.lib.get_path import init_file
from app.main import MainWindow

if __name__ == '__main__':
    init_file()
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
