def read_intlist():
    words = input().split()
    return [int(word) for word in words]

def solve(D, N):
    # strategy: just always serve the least delicious pancake.
    start, end = 0, N-1
    best = 0
    npay = 0
    # always get at least 2 pancakes.
    while start != end:
        popped = None
        if D[start] < D[end]:
            popped = D[start]
            start += 1
        else:
            popped = D[end]
            end -= 1
        if popped >= best:
            npay += 1
            best = popped
    # now there is only one pancake left at D[start] == D[end]
    if D[start] >= best:
        npay += 1
    return npay

def main():
    ncases = int(input())
    for case in range(1, ncases+1):
        N = int(input())
        D = read_intlist()
        npay = solve(D,N)
        print(f"Case #{case}: {npay}")

main()