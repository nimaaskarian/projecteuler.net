default_values = {
        "T": 8,
        "J": 9,
        "Q": 10,
        "K": 11,
        "A": 12,
        }
def card_value(card):
    charval = ord(card[0])-ord('0')
    if charval < 2:
        return
    if charval > 9:
        return default_values[card[0]]
    return charval-2


def suits(cards):
    from collections import Counter
    return Counter(val_suit[1] for val_suit in cards)

def values(cards):
    from collections import Counter
    return Counter(card_value(card) for card in cards)

def val_suits(cards):
    out = {}
    for card in cards:
        val = card_value(card)
        out[val] = out.get(val, []) + [card[1]]
    return out

def player_value(player):
    val_counts = values(player)
    is_flush = 5 in suits(player).values()
    pairs = tuple(key for key, val in val_counts.items() if val == 2)
    if len(pairs) == 2:
        three_value = 0
    else:
        three_value = sum((val == 3)*key for key,val in val_counts.items())
    if three_value or len(pairs):
        is_straight = False
    else:
        sorted_cards = sorted(val_counts.keys())
        is_straight = all(sorted_cards[i]+1 == sorted_cards[i+1] for i in range(len(sorted_cards)-1))
    if not len(pairs) and not three_value:
        four_oak_value = sum((val == 4)*key for key,val in val_counts.items())
    else:
        four_oak_value = 0
    is_full_house = three_value and len(pairs)
    if is_flush:
        is_royal_flush = all(key >= 9 for key in val_counts.keys())
    else:
        is_royal_flush = False
    straight_flush = is_straight and is_flush
    two_pairs = len(pairs) == 2 
    one_pair = len(pairs) == 1 
    if two_pairs:
        two_pairs_value = max(pairs)
    else:
        two_pairs_value = 0
    if one_pair:
        one_pair_value = pairs[0]
    else:
        one_pair_value = 0
    high_card = max(val_counts.keys())

    return (is_royal_flush*13**9 + straight_flush*13**8 + four_oak_value*13**7 +
     is_full_house*13**6 + is_flush*13**5 + is_straight*13**4 + three_value*13**3 +
     two_pairs_value*13**2 + one_pair_value*13**1 + high_card
     )


def does_player1_win(player1, player2):
    if player_value(player1) > player_value(player2):
        return True
    return False

def players(line):
    cards = line.split()
    return cards[:5], cards[5:]

with open("0054_poker.txt") as file:
    wins = 0
    while (line := file.readline()[:-1]):
        player1, player2 = players(line)
        if does_player1_win(player1, player2):
            wins += 1
    print(wins)
