import itertools as it
import math

def test():
    s = "hello"

def main():
    suits = ["H", "C", "D", "S"]
    values = [0, 1, 2]
    cards = []
    for suit in suits:
        for val in values:
            cards.append([suit, val])
    hands = it.combinations(cards, 5)
    total = math.comb(12, 5)
    n_4suit = 0
    for hand in hands:
        obs_suits = []
        for card in hand:
            obs_suits.append(card[0])
        # generator
        if all(suit in obs_suits for suit in suits):
            n_4suit += 1
    prob = n_4suit / total
    print(f"part a) probability is {prob}")

test()
# main()