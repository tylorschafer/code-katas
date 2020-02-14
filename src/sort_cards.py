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
    print(letters)
    print(numbers)

    sorted_cards = numbers + letters
    print(sorted_cards)

    for _ in range(a_count):
        sorted_cards.insert(0, 'A')

    print(sorted_cards)
    return sorted_cards
