"""Represents LXDE desktop environment."""

import os


def set_background():
    """Sets desktop background."""
    os.system('pcmanfm --set-wallpaper="' +
              os.path.abspath('img.jpg') + '"')
