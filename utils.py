import os
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def highlight(text):
    return f"{Fore.CYAN}{text}{Style.RESET_ALL}"

def success(text):
    return f"{Fore.GREEN}{text}{Style.RESET_ALL}"

def error(text):
    return f"{Fore.RED}{text}{Style.RESET_ALL}"