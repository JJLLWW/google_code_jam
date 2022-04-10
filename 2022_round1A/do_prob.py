import itertools as it
import math

def main():
    cards = []
    for suit in range(4):
        for val in range(3):
            cards.append([suit, val])
    hands = it.combinations(cards, 5)
    total = math.comb(12, 5)
    n_4suit = 0
    for hand in hands:
        suits = []
        for card in hand:
            suits.append(card[0])
        if 0 in suits and 1 in suits and 2 in suits and 3 in suits:
            n_4suit += 1
    prob = n_4suit / total
    print(f"part a) probability is {prob}")

main()