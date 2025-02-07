# OPEN SOURCE CODE (Comments added for readability.)


# Devnote from ven
# =========================
# bruh why do you unnecesarrily import everything lol. there was no reason to import datetime or glob xD
#
# added ubuntu booting and ubuntu cmds

# Imports
import colorama
import subprocess
import os
import ctypes
import time
import pystyle
from tqdm import tqdm
import sys

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
version = '0.1.0 Beta'

# Folder Paths
current_dir = os.path.dirname(os.path.abspath(__file__))  # Get the current directory of the script

# Functions

def spinning_loader():
    spinner = tqdm(range(100), desc="Loading", bar_format="{desc}: {percentage:3.0f}%|{bar}|", ncols=50)
    for _ in spinner:
        time.sleep(0.009)
        spinner.set_postfix_str("Please wait...")



def CustomPrompt():
    while True:
        cmdinpt = input(f'{red}!{cyan}{username}@{white}Vanilla{blue}$ {white}')

        if cmdinpt == 'help':
            help()
        elif cmdinpt == 'themeset':
            set_theme()
        elif cmdinpt == 'clear':
            MainModule()
        elif cmdinpt == 'vnl':
            print(f'Vanilla is located in {current_dir}')

        elif cmdinpt == 'boot ubuntu':
            boot('Ubuntu VNL v0.1.0 Beta')
        else:
            print(f"{red}[!] Illegal command received. Use 'help' for a list of available commands.")

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
    ║ [boot ubuntu] ~ Boots into Ubuntu.               ║
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


# Booting sequences
# ============================

def ubuntu():
    pass



def boot(distro):
    print(f'\n {white}Preparing to boot to {blue}{distro}{white}..')
    print()

    if __name__ == "__main__":
        spinning_loader()
    else:
        sys.exit()

    print(f'\n{blue}{distro} {white}ready.')
    print('Booting...')
    time.sleep(0.1)

    subprocess.run('cls', shell=True)

    if distro.__contains__('Ubuntu'):
        ubuntu()










if __name__ == '__main__':
    MainModule()
