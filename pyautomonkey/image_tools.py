from desktopmagic.screengrab_win32 import getScreenAsImage
import win32gui, win32con
from PIL import Image
from time import sleep
from timeit import default_timer as timer
import numpy as np
import cv2


def retrieve_image(window_name=None):
    """
    brings specified window to foreground and returns an image of the
    whole screen.
    """
    start = timer()

    toplist, winlist = [], []

    def enum_cb(hwnd, results):
        winlist.append((hwnd, win32gui.GetWindowText(hwnd)))

    win32gui.EnumWindows(enum_cb, toplist)

    if window_name:
        window_name = window_name.lower()
        window = [(hwnd, title) for hwnd, title in winlist if window_name in title.lower()]

        # just grab the hwnd for first window matching the window name
        try:
            window = window[0]
            hwnd = window[0]
        except IndexError:
            print("\nERROR: Specified window with name %s not found!\n" % window_name)
            raise

        win32gui.ShowWindow(hwnd,win32con.SW_MAXIMIZE)
        win32gui.SetForegroundWindow(hwnd)
        bbox = win32gui.GetWindowRect(hwnd)
    img = getScreenAsImage()

    end = timer()

    img = np.array(img.convert('RGB'))
    img = img.astype(np.uint8)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    return img


def load_template(template_file_name):
    """
    loads a template from file
    """
    if type(template_file_name) is not list:
        template = Image.open(template_file_name).convert('RGB')
        template = np.array(template)
        # Convert RGB to BGR
        template = template.astype(np.uint8)
        template = cv2.cvtColor(template, cv2.COLOR_RGB2GRAY)
        return template
    elif type(template_file_name) is list:
        raise AttributeError("lists of templates are work in progress")


def find_template(template, im=None, window_name=None):
    """
    finds template on screen or specified window_name and returns xy-coordinates
    """
    # if no image was specified, retreive an image
    im_loaded = False
    im = retrieve_image(window_name)
    # find template
    res = cv2.matchTemplate(im, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    # calculate position of found picture center
    height, width = template.shape
    x_corner, y_corner = max_loc
    xy = (int(x_corner + (width/2)), int(y_corner + (height/2)))

    # return location and matching probability
    return xy, max_val
