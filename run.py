"""Updates front_end/ui.py and runs GUI code."""


import os


def run():
    import front_end.gui as gui
    gui.main()


os.system('pyuic5 front_end/main.ui -o front_end/ui.py')

run()
