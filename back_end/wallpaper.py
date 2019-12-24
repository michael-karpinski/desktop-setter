"""Finds desktop environment and sets wallpaper."""

import os
import platform

# OLD SOLUTIONS. #
# http://stackoverflow.com/questions/2035657/what-is-my-current-desktop-environment
# https://stackoverflow.com/questions/1977694/how-can-i-change-my-desktop-background-with-python
# - Martin Hansen

# CURRENT SOLUTION. #
# https://github.com/Thomas9292/nasa-background


def change_background(file_path):
    """
    Checks the operating system and defers to OS-specific function
    """
    try:
        # Detect operating system and defer to specific function
        if platform.system().lower().startswith('win'):
            change_windows_background(file_path)
        elif platform.system().lower().startswith('lin'):
            change_linux_background(file_path)
        elif platform.system().lower().startswith('dar'):
            change_mac_background(file_path)

    except Exception as e:
        print(
            "Unable to change background. Your operating system may not yet be supported."
        )


def change_windows_background(file_path):
    """
    Change the background on windows operating systems
    """
    import ctypes
    SPI_SETDESKWALLPAPER = 20

    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0,
                                               file_path, 1)


def change_linux_background(file_path):
    """
    Change the background on Linux operating systems
    """
    import subprocess

    # Initialize variables
    ARG_MAP = {
        'feh': ['feh', ['--bg-center'], '%s'],
        'gnome': [
            'gsettings',
            ['set', 'org.gnome.desktop.background', 'picture-uri'], 'file://%s'
        ]
    }

    WM_BKG_SETTERS = {
        'spectrwm': ARG_MAP['feh'],
        'scrotwm': ARG_MAP['feh'],
        'wmii': ARG_MAP['feh'],
        'i3': ARG_MAP['feh'],
        'awesome': ARG_MAP['feh'],
        'awesome-gnome': ARG_MAP['gnome'],
        'gnome': ARG_MAP['gnome'],
        'ubuntu': ARG_MAP['gnome']
    }

    # Try to find background setter
    desktop_environ = os.environ.get('DESKTOP_SESSION', '')

    # Get settings arguments
    if desktop_environ and desktop_environ in WM_BKG_SETTERS:
        bkg_setter, args, pic_arg = WM_BKG_SETTERS.get(desktop_environ,
                                                       [None, None])
    else:
        bkg_setter, args, pic_arg = WM_BKG_SETTERS['spectrwm']

    # Parse and execute background change command
    pargs = [bkg_setter] + args + [pic_arg % file_path]
    subprocess.call(pargs)


def change_mac_background(file_path):
    """
    Change the background on Mac operating systems
    """
    try:
        from appscript import app, mactypes
        app('Finder').desktop_picture.set(mactypes.File(file_path))
    except ImportError:
        import subprocess
        SCRIPT = """
                 /usr/bin/osascript<<END
                 tell application "Finder" to
                 set desktop picture to POSIX file "%s"
                 end tell
                 END
                 """
        subprocess.Popen(SCRIPT % file_path, shell=True)
