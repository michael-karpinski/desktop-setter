"""Loads GUI and starts application."""

import sys
import os
from PyQt5 import QtWidgets, uic
from back_end.main import run


class GUI():
    """User interface."""

    def __init__(self):
        self.app = QtWidgets.QApplication([])
        self.win = uic.loadUi('main.ui')
        self.set_listeners()
        self.win.show()
        os.system('stty sane')
        sys.exit(self.app.exec_())

    def set_listeners(self):
        """Sets event listeners."""
        self.win.confirm_button.clicked.connect(run)
        self.win.no_button.clicked.connect(sys.exit)


if __name__ == "__main__":
    GUI()
