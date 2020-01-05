"""Updates front_end/ui.py and runs GUI code."""


import os
import front_end.gui as gui


os.system('pyuic5 front_end/main.ui -o front_end/ui.py')
gui.main()
