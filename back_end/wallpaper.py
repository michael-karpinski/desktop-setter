"""Finds desktop environment and sets wallpaper."""

import subprocess
import sys
import os


def get_desktop_environment():
    """Determines user's desktop environment and returns an instantiated object."""
    # http://stackoverflow.com/questions/2035657/what-is-my-current-desktop-environment
    if sys.platform in ["win32", "cygwin"]:
        return "windows"
    if sys.platform == "darwin":
        return "mac"
    # Most likely either a POSIX system or something not much common
    desktop_session = os.environ.get("DESKTOP_SESSION")
    if desktop_session is not None:
        desktop_session = desktop_session.lower()
        if desktop_session in ["gnome", "unity", "cinnamon", "lxde", "mate", "xfce4",
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


def set_wallpaper(file_loc):
    """Based on desktop environment, sets wallpaper."""
    # https://stackoverflow.com/questions/1977694/how-can-i-change-my-desktop-background-with-python
    # - Martin Hansen

    desktop_env = get_desktop_environment()
    try:
        if sys.platform in ["win32", "cygwin"]:
            ctypes.windll.user32.SystemParametersInfoW(
                20, 0, file_loc, 0)
        elif sys.platform == "darwin":
            CMD = """/usr/bin/osascript<<END
                        tell application "Finder"
                        set desktop picture to POSIX file "%s"
                        end tell
                        END"""
            subprocess.Popen(CMD % file_loc, shell=True)
            return "Mac"
        elif desktop_env in ["gnome", "unity", "cinnamon"]:
            uri = "'file://%s'" % file_loc
            try:
                SCHEMA = "org.gnome.desktop.background"
                KEY = "picture-uri"
                gsettings = Gio.Settings.new(SCHEMA)
                gsettings.set_string(KEY, uri)
            except:
                args = ["gsettings", "set",
                        "org.gnome.desktop.background", "picture-uri", uri]
                subprocess.Popen(args)
        elif desktop_env == "mate":
            try:  # MATE >= 1.6
                # info from http://wiki.mate-desktop.org/docs:gsettings
                args = ["gsettings", "set", "org.mate.background",
                        "picture-filename", "'%s'" % file_loc]
                subprocess.Popen(args)
            except:  # MATE < 1.6
                # From https://bugs.launchpad.net/variety/+bug/1033918
                args = ["mateconftool-2", "-t", "string", "--set",
                        "/desktop/mate/background/picture_filename", '"%s"' % file_loc]
                subprocess.Popen(args)
        elif desktop_env == "gnome2":  # Not tested
            # From https://bugs.launchpad.net/variety/+bug/1033918
            args = ["gconftool-2", "-t", "string", "--set",
                    "/desktop/gnome/background/picture_filename", '"%s"' % file_loc]
            subprocess.Popen(args)
        ## KDE4 is difficult
        # see http://blog.zx2c4.com/699 for a solution that might work
        elif desktop_env in ["kde3", "trinity"]:
            # From http://ubuntuforums.org/archive/index.php/t-803417.html
            args = 'dcop kdesktop KBackgroundIface setWallpaper 0 "%s" 6' % file_loc
            subprocess.Popen(args, shell=True)
        elif desktop_env == "xfce4":
            # From http://www.commandlinefu.com/commands/view/2055/change-wallpaper-for-xfce4-4.6.0
            args0 = ["xfconf-query", "-c", "xfce4-desktop", "-p",
                     "/backdrop/screen0/monitor0/image-path", "-s", file_loc]
            args1 = ["xfconf-query", "-c", "xfce4-desktop", "-p",
                     "/backdrop/screen0/monitor0/image-style", "-s", "3"]
            args2 = ["xfconf-query", "-c", "xfce4-desktop", "-p",
                     "/backdrop/screen0/monitor0/image-show", "-s", "true"]
            subprocess.Popen(args0)
            subprocess.Popen(args1)
            subprocess.Popen(args2)
            args = ["xfdesktop", "--reload"]
            subprocess.Popen(args)
        elif desktop_env in ["fluxbox", "jwm", "openbox", "afterstep"]:
            # http://fluxbox-wiki.org/index.php/Howto_set_the_background
            # used fbsetbg on jwm too since I am too lazy to edit the XML configuration
            # now where fbsetbg does the job excellent anyway.
            # and I have not figured out how else it can be set on Openbox and AfterSTep
            # but fbsetbg works excellent here too.
            try:
                args = ["fbsetbg", file_loc]
                subprocess.Popen(args)
            except:
                sys.stderr.write(
                    "ERROR: Failed to set wallpaper with fbsetbg!\n")
                sys.stderr.write(
                    "Please make sre that You have fbsetbg installed.\n")
        elif desktop_env == "icewm":
            # command found at http://urukrama.wordpress.com/2007/12/05/desktop-backgrounds-in-window-managers/
            args = ["icewmbg", file_loc]
            subprocess.Popen(args)
        elif desktop_env == "blackbox":
            # command found at http://blackboxwm.sourceforge.net/BlackboxDocumentation/BlackboxBackground
            args = ["bsetbg", "-full", file_loc]
            subprocess.Popen(args)
        elif desktop_env == "lxde":
            args = "pcmanfm --set-wallpaper %s --wallpaper-mode=scaled" % file_loc
            subprocess.Popen(args, shell=True)
        elif desktop_env == "windowmaker":
            # From http://www.commandlinefu.com/commands/view/3857/set-wallpaper-on-windowmaker-in-one-line
            args = "wmsetbg -s -u %s" % file_loc
            subprocess.Popen(args, shell=True)
        else:
            sys.stderr.write(
                "Warning: Failed to set wallpaper. Your desktop environment is not supported.")
            sys.stderr.write(
                "You can try manually to set Your wallpaper to %s" % file_loc)
            return False
        return True
    except:
        sys.stderr.write(
            "ERROR: Failed to set wallpaper. There might be a bug.\n")
        return False


def get_home_dir():
    if sys.platform == "cygwin":
        home_dir = os.getenv('HOME')
    else:
        home_dir = os.getenv('USERPROFILE') or os.getenv('HOME')
    if home_dir is not None:
        return os.path.normpath(home_dir)
    else:
        raise KeyError(
            "Neither USERPROFILE or HOME environment variables set.")
