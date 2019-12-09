import os
import sys
import platform
from PySide2.QtWidgets import QApplication

from app.signin import SignInWidget

if __name__ == '__main__':

    if platform.system() == 'Windows':
        import PySide2

        dirname = os.path.dirname(PySide2.__file__)
        plugin_path = os.path.join(dirname, 'plugins', 'platforms')
        os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path

        import ctypes
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("ctpbee_desktop")

    app = QApplication(sys.argv)

    signinwindow = SignInWidget()
    signinwindow.show()
    signinwindow.raise_()

    sys.exit(app.exec_())
