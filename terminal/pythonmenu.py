import config
import sys
import os

class pythonmenu():
    def __init__(self):
        enabled = True
        while True:
            menu = self.makemenu("")
            print(menu)
            raw_input("")

    def makemenu(self, error):
        temp = ["##",""]
        for i in config.application_name:
            temp[0] += "#"
        menu = temp[0] + "\n#" + str(config.application_name) + "#\n" + temp[0] + "\n"
        x = 0
        for option in config.menu_options[x]:
            menu += str(config.menu_options[x][0]) + ". " + str(config.menu_options[x][1]) + "\n"
            x += 1
        if error != "":
            menu += "Error: " + error + "\n"
        return menu

pythonmenu()