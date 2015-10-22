import config
import sys
import os

class pythonmenu():
    def __init__(self):
        error = ""
        while True:
            menu = self.makemenu("")
            os.system("clear")
            print(menu)
            input = raw_input("Please enter an option: ")
            self.checkinput(input)
            error = "Invalid Input!"

    def makemenu(self, error):
        temp = ["##",""]
        for i in config.application_name:
            temp[0] += "#"
        menu = temp[0] + "\n#" + str(config.application_name) + "#\n" + temp[0] + "\n"
        x = 0
        for option in config.menu_options:
            menu += str(config.menu_options[x][0]) + ". " + str(config.menu_options[x][1]) + "\n"
            x += 1
        if error != "":
            menu += "Error: " + error + "\n"
        return menu

    def checkinput(self, input):
        x = 0
        for option in config.menu_options[x]:
            if input == config.menu_options[x][0]:
                exec(config.menu_options[x][2])
            x += 1

pythonmenu()