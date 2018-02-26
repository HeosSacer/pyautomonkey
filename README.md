<img align="right" width="509" height="140" title="monkey logo" src="https://raw.githubusercontent.com/HeosSacer/pyautomonkey/master/logo.PNG" />


[![Get Support at https://discord.gg/5MRJaTf](https://img.shields.io/badge/join-discord-blue.svg)](https://discord.gg/5MRJaTf)

This handy framework will help you to automate all GUI-applications with python!



# pyautomonkey
This monkey will find templates of pictures like created with the windows snipping tool on your
screen or inside a specified window.

# Installation
This monkey will only work on windows machines, but on demand, maybe on others...

You need to install:
```
pip install Desktopmagic,numpy,opencv-python,Pillow,pywin32
```        

# Example

```
from pyautomonkey.image_tools import load_template
from pyautomonkey import automation as auto

# Load template from file
loaded_template = load_template('some_path_to_picture/picture_of_button')
# Find template/button on screen and click 
auto.click_on_template(loaded_template)
```

Check out the *retro_clicker.py* example for a more complex one!

#Credits
Go and try Desktopmagic for python! Extremly fast library to capture your screen!
Logo by https://www.designevo.com/, check out their stuff!
