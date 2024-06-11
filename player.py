class Player:
    def __init__(self,name):
        self.name=name
        self.hand=[]
    def draw_cards(self,deck,number=1):
        self.hand.extend(deck.draw_cards(number))
    def play_card(self,card):
        self.hand.remove(card)
    def __repr__(self):
        return self.name