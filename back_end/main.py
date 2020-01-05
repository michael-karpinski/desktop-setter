"""Nature Desktop (name is a WIP) creates beautiful desktop backgrounds by searching through
r/EarthPorn and finding a recent image whose resolution is close to your desktop's."""

import sys
import os
import datetime
import requests
from PyQt5 import QtWidgets
from back_end.url_finder import get_image_url
from back_end.wallpaper import change_background

FILE_EXTENSIONS = ['.jpg', '.png']


def run():
    """Determines platform, finds and downloads appropriate image, and sets desktop background."""
    os.system('stty sane')
    url = get_image_url()
    file_path = _download_image(url)
    change_background(file_path)
    sys.exit()


def _download_image(url):
    """Saves image from URL to cwd and returns its path."""
    data = requests.get(url).content
    file_path = _get_file_path(url)
    with open(file_path, 'wb') as handler:
        handler.write(data)
    return file_path


def _get_file_path(url):
    """Determines file path to save image to."""
    folder = _get_directory()
    datetime_string = datetime.datetime.now().strftime('%d-%b-%Y_%H-%M-%S')
    file_name = folder + os.path.sep + datetime_string + _get_extension(url)
    return file_name


def _get_directory():
    """Determines directory that images are saved to."""
    try:
        with open('folder.txt', 'r') as file_obj:
            return file_obj.read()
    except FileNotFoundError:
        folder = str(QtWidgets.QFileDialog.getExistingDirectory(
            None, 'Select Directory', options=QtWidgets.QFileDialog.DontUseNativeDialog))
        with open('folder.txt', 'w') as file_obj:
            file_obj.write(folder)
        return folder


def _get_extension(url):
    """Determines file type based on URL. Defaults to PNG."""
    for ext in FILE_EXTENSIONS:
        if ext in url:
            return ext
    return '.png'
