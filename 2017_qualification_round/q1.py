def flip(row, i, K):
    # assume there are at least K values after index i
    for j in range(0, K):
        if row[i+j] == '-':
            row[i+j] = '+'
        elif row[i+j] == '+':
            row[i+j] = '-'
        else:
            raise ValueError("flip, expected row to be an iterable with only '+' and '-'")

def solve(row, K):
    # we have 2 <= K <= len(row)
    nops = 0
    for i in range(0, len(row)-K+1):
        if row[i] == '-':
            flip(row, i, K)
            nops += 1
    # are there any '-' remaining?
    if '-' in row:
        return None
    else:
        return nops

def main():
    ncases = int(input())
    for case in range(1, ncases+1):
        words = input().split()
        row, K = list(words[0]), int(words[1])
        nops = solve(row, K)
        if nops is None:
            print(f"Case #{case}: IMPOSSIBLE")
        else:
            print(f"Case #{case}: {nops}")

main()