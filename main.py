"""Loads GUI and starts application."""

import sys
from PyQt5 import QtWidgets, uic
from back_end import run


if __name__ == "__main__":
    APP = QtWidgets.QApplication([])
    WIN = uic.loadUi('main.ui')
    WIN.confirm_button.clicked.connect(run)
    WIN.show()
    sys.exit(APP.exec_())
    sys.exit()
