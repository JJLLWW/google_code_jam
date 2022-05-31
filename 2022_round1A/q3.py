from collections import Counter
import sys

# dynamic programming, watch out for recursion depth exceeded exceptions.
sys.setrecursionlimit(1500)

def read_intlist():
    words = input().split()
    return [int(word) for word in words]

# watch out for edge cases - this could just be a while loop.
def solve(X):
    nops = 0
    # remove common weights (essentially place at bottom, contributing 2*least operations each)
    row_sz = len(X[0])
    for col_idx in range(row_sz):
        vals = [X[i][col_idx] for i in range(row_sz)]
        least = min(vals)
        if least > 0:
            for i in range(row_sz):
                X[i][col_idx] -= least
        nops += 2*least
    # remove zero rows (which don't contribute to any operations)
    rm_idxs = []
    for row_idx in range(len(X)):
        values = set(X[row_idx].values())
        if len(values) == 1:
            for e in values:
                if e == 0:
                    rm_idxs.append(row_idx)
                break
    rm_idxs.sort(reverse=True)
    for i in rm_idxs:
        del(X[rm_idxs])
    # (!) we have changed the shape of X, by removing rows, has it become empty? (!)
    if len(X) == 0:
        return nops
    # (!) if we have only one row remaining, we know how many operations are necessary (!)
    if len(X) == 1:
        pass
    # take into account columns with last row element a zero, (!) how do these effect nops? (!)

    return nops + solve(X)

def main():
    ncases = int(input())
    for case in range(1, ncases+1):
        E, W = read_intlist()
        X = []
        for _ in range(E):
            row = Counter(read_intlist())
            X.append(row)
        nops = solve(X)
        print(f"Case #{case}: {nops}")

main()