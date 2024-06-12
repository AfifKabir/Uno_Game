import random
from Card import Deck, Card, COLORS, SPECIAL_VALUES, WILD_VALUES
from player import Player
from utils import clear_screen, wait_for_player, display_hand, color_text

def initialize_game():
    num_players = int(input("Enter the number of players (2-8): "))
    players = []
    for i in range(num_players):
        name = input(f"Enter the name for player {i + 1}: ")
        players.append(Player(name))
        return players

def deal_initial_hands(players, deck):
    for player in players:
        player.draw_cards(deck, 7)

def check_uno(player, deck):
    if len(player.hand) == 1:
        call_uno = input(f"{color_text(player.name, 'yellow')}, call UNO! (y/n): ").strip().lower()
        if call_uno != 'y':
            print(f"{color_text(player.name, 'yellow')} forgot to call UNO! Drawing 2 penalty cards.")
            player.draw_cards(deck, 2)

def main():
    deck = Deck()
    players = initialize_game()
    deal_initial_hands(players, deck)
    
    top_card = deck.draw_card()
    while top_card.value in SPECIAL_VALUES + WILD_VALUES:
        deck.cards.append(top_card)
        random.shuffle(deck.cards)
        top_card = deck.draw_card()
    
    print(f"Starting card: {color_text(str(top_card), top_card.color)}\n")
    
    direction = 1
    player_turn = 0

    while True:
        current_player = players[player_turn]
        wait_for_player(current_player.name)
        display_hand(current_player)
        
        valid_play = False
        while not valid_play:
            choice = int(input(f"{current_player.name}, choose a card to play (1-{len(current_player.hand)}) or 0 to draw: "))
            if choice == 0:
                current_player.draw_cards(deck)
                valid_play = True
            else:
                chosen_card = current_player.hand[choice - 1]
                if (chosen_card.color == top_card.color or chosen_card.value == top_card.value or chosen_card.value in WILD_VALUES):
                    current_player.play_card(chosen_card)
                    top_card = chosen_card
                    valid_play = True
                else:
                    print(color_text("Invalid move. Card does not match.", 'red'))
        
        if not current_player.hand:
            print(f"{color_text(current_player.name, 'green')} wins!")
            break
        
        check_uno(current_player, deck)
        
        if top_card.value == 'Skip':
            player_turn = (player_turn + direction) % len(players)
        elif top_card.value == 'Reverse':
            direction *= -1
        elif top_card.value == 'Draw Two':
            next_player = (player_turn + direction) % len(players)
            players[next_player].draw_cards(deck, 2)
        elif top_card.value == 'Wild Draw Four':
            next_player = (player_turn + direction) % len(players)
            players[next_player].draw_cards(deck, 4)

        player_turn = (player_turn + direction) % len(players)
        clear_screen()

if __name__ == "__main__":
    main()