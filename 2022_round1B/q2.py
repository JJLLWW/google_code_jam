def read_intlist():
    words = input().split()
    return [int(word) for word in words]

def solve(N, P, X):
    npress = 0
    p = 0
    
    # only the max and min pressure are significant.
    mins, maxs = [], []
    for i in range(N):
        mins.append(min(X[i]))
        maxs.append(max(X[i]))
    print(mins, maxs)
    # two cases where we have to think ahead are when max[i+1] < min[i] and min[i+1] > max[i],
    # and p is betwen min[i] and max[i].
    for i in range(N):
        if mins[i] < p < maxs[i]:
            if i+1<N and mins[i] > maxs[i+1]:
                # go down
                npress += (maxs[i] - p) + (maxs[i] - mins[i])
                p = mins[i]
            elif i+1<N and maxs[i] < mins[i+1]:
                # go up
                npress += (p - mins[i]) + (maxs[i] - mins[i])
                p = maxs[i]
            # now we only need to care about optimising this stage, not what the next customer needs.
            elif p - mins[i] >= maxs[i] - p:
                # go down
                npress += (maxs[i] - p) + (maxs[i] - mins[i])
                p = mins[i]
            else:
                # go up
                npress += (p - mins[i]) + (maxs[i] - mins[i])
                p = maxs[i]
        # we have no choice but to go straight up or straight down.
        if p <= mins[i]:
            # go up
            npress += maxs[i] - p
            p = maxs[i]
        else:
            # go down
            npress += p - mins[i]
            p = mins[i]
    return npress

def main():
    ncases = int(input())
    for case in range(1, ncases+1):
        N, P = read_intlist()
        X = []
        for _ in range(N):
            X.append(read_intlist())
        npress = solve(N, P, X)
        print(f"Case #{case}: {npress}")

main()