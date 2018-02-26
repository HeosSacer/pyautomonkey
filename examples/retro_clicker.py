"""
this script shows the clicking and finding a template ability of this framework
"""

from pyautomonkey.image_tools import load_template, find_template
from pyautomonkey import automation as auto
from pyautomonkey import utils

from time import sleep
import webbrowser


# Open very difficult website
url = 'http://retrominder.tv/'
webbrowser.open(url)#[, new=0[, autoraise=True]])

# Load Templates
template_path_list = ['res/start_button.PNG',
                      'res/high_score_button.PNG',
                      'res/credits_button.PNG',
                      'res/press_enter_to_start_button.PNG']

game_logo = load_template('res/retro_game_logo.PNG')

loaded_templates = []
for template in template_path_list:
    loaded_templates.append(load_template(template))

print('Wait till retro game is loaded...')

matching_probability = 0
# Wait, till game is loaded/ game logo appeared...
while matching_probability < 0.8:
    __, matching_probability = find_template(game_logo)

for template in loaded_templates:
    xy = auto.click_on_template(template, matching_threashold=0.4)
    sleep(2) # Wait 2 seconds to get the gui to do its stuff
    utils.click(xy) # click on the previous coordinates
    sleep(2) # Wait 2 seconds to get the gui to do its stuff

print("The game starts, have fun!")
