"""Nature Desktop (name is a WIP). Creates beautiful desktop backgrounds by searching through
r/EarthPorn and finding a recent image whose resolution is close to your desktop's."""

import sys
import os
import datetime
import requests
from PyQt5 import QtWidgets
import back_end.img_functions as img_functions
from back_end import wallpaper

FILE_EXTENSIONS = ['jpg', 'png']


def run():
    """Determines platform, finds and downloads appropriate image, and sets desktop background."""
    file_name = download_image(img_functions.get_image_url())
    sys.exit(wallpaper.change_background(os.path.abspath(file_name)))


def download_image(url):
    """Saves image from URL to cwd."""
    data = requests.get(url).content
    file_path = get_file_path(url)
    with open(file_path, 'wb') as handler:
        handler.write(data)
    return file_path


def get_file_path(url):
    """Determines file path to save data to."""
    try:
        with open('folder.txt', 'r') as file_obj:
            folder = file_obj.read()
    except FileNotFoundError:
        folder = str(QtWidgets.QFileDialog.getExistingDirectory(
            None, 'Select Directory', options=QtWidgets.QFileDialog.DontUseNativeDialog))
        with open('folder.txt', 'w') as file_obj:
            file_obj.write(folder)
    file_name = folder + os.path.sep + \
        datetime.datetime.now().strftime('%d-%b-%Y_%H:%M:%S') + '.'
    file_name += get_extension(url)
    return file_name


def get_extension(url):
    """Determines file type based on URL. Defaults to PNG."""
    for ext in FILE_EXTENSIONS:
        if ext in url:
            return ext
    return 'png'
