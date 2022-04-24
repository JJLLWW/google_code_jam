def read_intlist():
    words = input().split()
    return [int(word) for word in words]

def solve(N, P, X):
    # strategy, order each customers objects in increasing pressure. 
    # if the current pressure is p and X[i][0] < p < X[i][-1], go down first if p - X[i][0] <= X[i][-1] - p,
    # otherwise go up. 

    npress = 0
    p = 0
    
    # only the max and min pressure are significant.
    mins, maxs = [], []
    for i in range(N):
        mins[i] = min(X[i])
        maxs[i] = max(X[i])
    # two cases where we have to think ahead are when max[i+1] < min[i] and min[i+1] > max[i],
    # and p is betwen min[i] and max[i].
    for i in range(N):
        if min[i] < p < maxs[i]:
            if i+1<N and mins[i] > maxs[i+1]:
                # go down
                npress += (maxs[i] - p) + (maxs[i] - mins[i])
                p = mins[i]
            if i+1<N and maxs[i] < mins[i+1]:
                # go up
                npress += (p - mins[i]) + (maxs[i] - mins[i])
                p = maxs[i]


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