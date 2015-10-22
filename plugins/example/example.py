import config
import sys
import os

class example():
    def __init__(self):
        print("Hello!\n1 for do shit\n2 for exit")
        input = raw_input("Hello: ")
        if input == "2":
            return
        elif input == "1":
            print("1")
            return
        else:
            print("Fuck u")
            return