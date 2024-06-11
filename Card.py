import random
from colorama import Fore, Style,init
init(autoreset=True)

class card():
    color_map = {
        'Red': Fore.RED,
        'Yellow': Fore.YELLOW,
        'Green':Fore.GREEN,
        'Blue':Fore.BLUE,
        'Wild':Fore.MAGENTA
    }
    def __init__(self,color,value):
        self.color=color
        self.value=value

    def __str__(self):
        color_str=self.color_map.get(self.color, '')
        return f'{color_str} {self.color} {self.value} {Style.RESET_ALL}'


