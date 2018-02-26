import win32api, win32con
from time import sleep
import keyboard
import os


def click(xy, offset_xy=(0,0)):
    """
    click with left mouse button with offset
    """
    (x,y) = xy
    (offset_x, offset_y) = offset_xy
    x = x + offset_x
    y = y + offset_y
    move_to((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)


def move_to(xy):
    """
    move your mouse to xy
    """
    (x,y) = xy
    win32api.SetCursorPos((x,y))


def hit_enter():
    """
    hit the enter button
    """
    keyboard.press_and_release('Enter')
