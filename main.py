import os
import sys
import time
import random
sys.path.append("./scr")
import menus as mn


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


# import pygame
clear()
mn.main_menu()
