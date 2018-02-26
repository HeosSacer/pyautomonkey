from .image_tools import *
from .utils import *


def click_on_template(template, matching_threashold=0.9, window_name=None):
    """
    clicks on template found on whole screen or on specified window
    raises an error, if matching probability is below specified
    matching_threashold
    """
    xy, match_prob = find_template(template, window_name=window_name)
    if match_prob >= matching_threashold:
        click(xy)
    else:
        raise ValueError("Template not found! Matching probability is ", match_prob)
    return xy


def click_through_template_list(template_list, matching_threashold=0.9, window_name=None):
    """
    clicks on several templates in order, how they are in the list
    """
    template_no = 1
    for template in template_list:
        try:
            click_on_template(template,
                          matching_threashold=matching_threashold,
                          window_name=window_name)
            template_no += 1
        except ValueError:
            print("ERROR: Template No. %i not found!" % template_no)
            raise
