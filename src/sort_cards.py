import re

def sort_cards(cards):
    a_count = cards.count('A')

    try:
        while True:
            cards.remove('A')
    except ValueError:
        pass

    letters = sorted([card for card in cards if card.isalpha()], reverse=True)
    numbers = sorted([card for card in cards if card.isdigit()])

    sorted_cards = numbers + letters

    for _ in range(a_count):
        sorted_cards.insert(0, 'A')

    return sorted_cards
