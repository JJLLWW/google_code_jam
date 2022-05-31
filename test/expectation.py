import itertools as it
import fractions as fr

cards = [val for val in it.product(["Q", "K", "A"], ["1", "2", "3", "4"])]
hands = it.combinations(cards, 3)

n_2ace = 0
n_comb = 0
n_more1ace = 0

for hand in hands:
    n_comb += 1
    n_ace = 0
    for card in hand:
        if card[0] == "A":
            n_ace += 1
    if n_ace >= 1:
        n_more1ace += 1
    if n_ace == 2:
        n_2ace += 1

print(fr.Fraction(n_2ace, n_comb))
print(fr.Fraction(n_2ace, n_more1ace))