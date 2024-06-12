import os
import time
from colorama import init, Fore, Style

init(autoreset=True)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def wait_for_player(name):
    input(f"{name}, press Enter to take your turn...")
    clear_screen()

def display_hand(player):
    print(f"{player.name}'s hand:")
    for idx, card in enumerate(player.hand):
        color = getattr(Fore, card.color.upper(), Fore.WHITE) if card.color else Fore.WHITE
        print(f"{idx + 1}: {color}{card}")
    print("\n")

def color_text(text, color):
    return f"{getattr(Fore, color.upper(), Fore.WHITE)}{text}{Style.RESET_ALL}"