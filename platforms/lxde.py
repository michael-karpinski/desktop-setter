import os

import curses
SCR = curses.initscr()


def image_ratio(image):
    """return width/height ratio of given image"""
    width = image['data']['preview']['images'][0]['source']['width']
    height = image['data']['preview']['images'][0]['source']['height']
    return width/height


class LXDE:
    def __init__(self):
        print('hello, I\'m LXDE!')

    def screen_resolution_ratio(self):
        """find desktop screen resolution"""
        height, width = SCR.getmaxyx()
        return width/height

    def find_most_compatible(self, imgs):
        """take a list of images and return the most compatible one"""
        imgs = sorted(imgs, key=lambda k: image_ratio(k))
        most_compatible = min(
            imgs, key=lambda x: abs(image_ratio(
                x)-self.screen_resolution_ratio())
        )
        url = most_compatible['data']['url']

        if len(url.split('.')[-1]) != 3 and url.split('.')[-1] != 'com':
            url = url + '.jpg'

        return url

    def set_background(self):
        os.system('pcmanfm --set-wallpaper="' +
                  os.path.abspath('img.jpg') + '"')
