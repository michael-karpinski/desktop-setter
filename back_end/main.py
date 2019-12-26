"""Nature Desktop (name is a WIP). Creates beautiful desktop backgrounds by searching through
r/EarthPorn and finding a recent image whose resolution is close to your desktop's."""

import sys
import os
import requests

try:
    import back_end.img_functions as img_functions
    from back_end import wallpaper
except ImportError:
    import img_functions
    import wallpaper


def download_image(url):
    """Saves image from URL to cwd."""
    data = requests.get(url).content
    with open('img.jpg', 'wb') as handler:
        handler.write(data)


def run():
    """Determines platform, finds and downloads appropriate image, and sets desktop background."""
    download_image(img_functions.get_image_url())
    sys.exit(wallpaper.change_background(os.path.abspath('img.jpg')))


if __name__ == '__main__':
    run()
