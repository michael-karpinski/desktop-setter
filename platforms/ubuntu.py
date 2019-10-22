
import curses
SCR = curses.initscr()


def screen_resolution_ratio():
    """find desktop screen resolution"""
    height, width = SCR.getmaxyx()
    return width/height
