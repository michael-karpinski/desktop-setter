"""Nature Desktop (name is a WIP). Creates beautiful desktop backgrounds by searching through
r/EarthPorn and finding a recent image whose resolution is close to your desktop's."""

import sys
import os
import requests

import back_end.img_functions as img_functions
from platforms import lxde


def get_desktop_environment():
    """Determines user's desktop environment and returns an instantiated object."""
    # http://stackoverflow.com/questions/2035657/what-is-my-current-desktop-environment
    if sys.platform in ["win32", "cygwin"]:
        return "Windows"
    if sys.platform == "darwin":
        return "Mac"
    # Most likely either a POSIX system or something not much common
    desktop_session = os.environ.get("DESKTOP_SESSION")
    if desktop_session is not None:
        desktop_session = desktop_session.lower()
        if desktop_session == 'lxde':
            return lxde
        if desktop_session in ["gnome", "unity", "cinnamon", "mate", "xfce4",
                               "fluxbox", "blackbox", "openbox", "icewm",
                               "jwm", "afterstep", "trinity", "kde"]:
            return desktop_session
        ## Special cases ##
        # Canonical sets $DESKTOP_SESSION to Lubuntu rather than LXDE if using LXDE.
        if "xfce" in desktop_session or desktop_session.startswith("xubuntu"):
            return "xfce4"
        if desktop_session.startswith("ubuntu"):
            return "unity"
        if desktop_session.startswith("lubuntu"):
            return "lxde"
        if desktop_session.startswith("kubuntu"):
            return "kde"
        if desktop_session.startswith("razor"):  # e.g. razorkwin
            return "razor-qt"
        # e.g. wmaker-common
        if desktop_session.startswith("wmaker"):
            return "windowmaker"
    if os.environ.get('KDE_FULL_SESSION') == 'true':
        return "kde"
    if os.environ.get('GNOME_DESKTOP_SESSION_ID'):
        if not "deprecated" in os.environ.get('GNOME_DESKTOP_SESSION_ID'):
            return "gnome2"
    return "unknown"


def download_image(url):
    """Saves image from URL to cwd."""
    data = requests.get(url).content
    with open('img.jpg', 'wb') as handler:
        handler.write(data)


def run():
    """Determines platform, finds and downloads appropriate image, and sets desktop background."""
    platform = get_desktop_environment()
    img_url = img_functions.get_image_url()
    download_image(img_url)
    platform.set_background()


if __name__ == '__main__':
    run()
    sys.exit()
