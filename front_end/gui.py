"""Loads GUI and starts application."""

import sys
import threading
from PyQt5 import QtWidgets
from back_end.main import run
import front_end.ui as ui


class GUI(QtWidgets.QDialog, ui.Ui_Dialog):
    """User interface."""

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Desktop Setter')
        self.set_listeners()
        self.show()

    def start_backend(self):
        main_thread = threading.Thread(target=run)
        main_thread.start()

    def set_listeners(self):
        """Sets event listeners."""
        self.confirm_button.clicked.connect(run)
        self.no_button.clicked.connect(sys.exit)


def main():
    """Runs GUI."""
    app = QtWidgets.QApplication([])
    win = GUI()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
