"""Uses pyinstaller to build the project."""

import os

os.system('rm -rf build dist')
os.system('pyinstaller dist_run.spec')
