"""Uses pyinstaller to build the project."""

import os

os.system('rm -rf build dist')
os.system('pyinstaller front_end/gui.py --onefile --noconsole --icon=front_end' +
          os.path.sep + 'icon.png')
