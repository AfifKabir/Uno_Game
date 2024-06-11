import random
from colorama import Fore, Style

COLORS=['Red','Yellow','Green','Blue']
SPECIAL_VALUES=['Skip','Reverse','Draw Two']
WILD_VALUES=['Wild','Wild Draw Four']

class Card:
    def __init__(self,color,value):
        self.color=color
        self.value=value

    def __repr__(self):
        color_code= getattr(Fore,self.color.upper(), Fore.WHITE)
        return f"{color_code} {self.color} {self.value} {Style.RESET_ALL}"
    
class Deck:
    def __init__(self):
        self.cards = []
        self.generate_deck()
        self.shuffle_deck()
    def generate_deck(self):
        for color in COLORS:
        #Number cards (0-9),two sets of each from 1-9
            self.cards.append(Card(color,'0'))
        for value in range (1,10):
             self.cards.append(Card(color,str(value)))
        #Action cards
        for _ in range(2):
             for special_value in SPECIAL_VALUES:
                  self.cards.append(Card(color,special_value))
        #Wild cards
        for _ in range(4):
             self.cards.append(Card(None,'Wild'))
             self.cards.append(Card(None,'Wild Draw Four'))
    def shuffle_deck(self):
        random.shuffle(self.cards)
    def draw_card(self):
        return self.cards.pop()
    def draw_cards(self,number):
        return [self.draw_card() for _ in range(number)]
        