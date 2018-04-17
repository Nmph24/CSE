heart_cards = ["H1", "H2", "H3", "H4", "H5", "H6", "H7", "H8", "H9", "H10", "HJ", "HK", "HQ"]
diamond_cards = ["D1", "D2", "D3", "D4", "D5", "D6", "D7", "D8", "D9", "D10", "DJ", "DK", "DQ"]
deck = []
for num in range(13):
    for suit in ['H', 'C', 'D', 'S']:
        card = suit + str(num + 1)
        deck.append(card)

print(deck)
