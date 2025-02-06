# OPEN SOURCE CODE (Comments added for readability.)

# Imports
import colorama
import pystyle
import subprocess
import os
import datetime
import ctypes
import glob

from colorama import *
from pystyle import *
from ctypes import *
from subprocess import *

# Initialize Colorama
colorama.init(autoreset=True)

# Variables
white = Fore.WHITE
cyan = Fore.CYAN
blue = Fore.BLUE
red = Fore.RED
username = os.getlogin()
version = '0.1.5'

# Folder Paths
current_dir = os.path.dirname(os.path.abspath(__file__))  # Get the current directory of the script

# Functions
def CustomPrompt():
    while True:
        cmdinpt = input(f'{red}!{cyan}{username}@{white}Vanilla{blue}% ')

        if cmdinpt == 'help':
            help()
        elif cmdinpt == 'themeset':
            set_theme()
        elif cmdinpt == 'clear':
            MainModule()
        elif cmdinpt == 'vnl':
            print(f'Vanilla is located in {current_dir}')
        else:
            print(f'{red}[!] Illegal command received. Use \'help\' for a list of available commands.')

def MainModule():

    subprocess.run('cls', shell=True)
    ctypes.windll.kernel32.SetConsoleTitleW(f'VANILLA || {version}')
    Write.Print(f'''
    
    ██╗   ██╗ █████╗ ███╗   ██╗██╗██╗     ██╗      █████╗ 
    ██║   ██║██╔══██╗████╗  ██║██║██║     ██║     ██╔══██╗
    ██║   ██║███████║██╔██╗ ██║██║██║     ██║     ███████║
    ╚██╗ ██╔╝██╔══██║██║╚██╗██║██║██║     ██║     ██╔══██║
     ╚████╔╝ ██║  ██║██║ ╚████║██║███████╗███████╗██║  ██║ 
      ╚═══╝  ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝╚══════╝╚══════╝╚═╝  ╚═╝ {version} 
    ══════════════════════════════════════════════════════════════════════════════════════════════
    To view a list of available commands, use 'help'.                                                  

    '''
    ,white, interval=0.000)
    CustomPrompt()

def help():
    Write.Print(f'''
     ██████╗███╗   ███╗██████╗ ███████╗
    ██╔════╝████╗ ████║██╔══██╗██╔════╝
    ██║     ██╔████╔██║██║  ██║███████╗
    ██║     ██║╚██╔╝██║██║  ██║╚════██║
    ╚██████╗██║ ╚═╝ ██║██████╔╝███████║
     ╚═════╝╚═╝     ╚═╝╚═════╝ ╚══════╝
    ╔══════════════════════════════════════════════════╗
    ║ [help] ~ Display this message.                   ║
    ║ [themeset] ~ Set your theme                      ║
    ║ [vnl] ~ Displays the location of Vanilla.        ║
    ║ [clear] ~ Clears the console.                    ║
    ╚══════════════════════════════════════════════════╝
    '''
    ,white, interval=0.000)

def set_theme():
    print(f"{cyan}[*] Available themes:")
    print(f"{white}[1] Vanilla (White)")
    print(f"{white}[2] Dark Theme (Black and Green)")
    print(f"{white}[3] Light Theme (Black and Yellow)")
    
    theme_choice = input(f"{red}!{cyan}{username}@{white}Vanilla{blue}% Choose a theme (1/2/3): ")
    
    if theme_choice == '1':
        set_default_theme()
    elif theme_choice == '2':
        set_dark_theme()
    elif theme_choice == '3':
        set_light_theme()
    else:
        print(f"{red}[!] Invalid choice. Keeping default theme.")

def set_default_theme():
    global white, cyan, blue, red
    white = Fore.WHITE
    cyan = Fore.CYAN
    blue = Fore.BLUE
    red = Fore.RED
    print(f"{cyan}[*] Theme set to Default (Blue and White).")

def set_dark_theme():
    global white, cyan, blue, red
    white = Fore.GREEN
    cyan = Fore.GREEN
    blue = Fore.GREEN
    red = Fore.GREEN
    print(f"{cyan}[*] Theme set to Dark (Black and Green).")

def set_light_theme():
    global white, cyan, blue, red
    white = Fore.YELLOW
    cyan = Fore.YELLOW
    blue = Fore.YELLOW
    red = Fore.YELLOW
    print(f"{cyan}[*] Theme set to Light (Black and Yellow).")

if __name__ == '__main__':
    MainModule()
