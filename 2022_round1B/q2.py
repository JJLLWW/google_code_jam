def read_intlist():
    words = input().split()
    return [int(word) for word in words]

def solve(N, P, X):
    # strategy, order each customers objects in increasing pressure. 
    # if the current pressure is p and X[i][0] < p < X[i][-1], go down first if p - X[i][0] <= X[i][-1] - p,
    # otherwise go up. 

    # only the max and min pressure are significant.
    npress = 0
    cur_pressure = 0
    for i in range(N):
        # increasing order
        X[i].sort()
        if X[i][0] < cur_pressure < X[i][-1]:
            # we need to go up and then down dependent on which is quicker. This also might need to
            # take the next customer into account. (lets just pray it doesn't)
            if cur_pressure - X[i][0] <= X[i][-1] - cur_pressure:
                # go down first.
                npress += (cur_pressure - X[i][0]) + (X[i][-1] - X[i][0])
                cur_pressure = X[i][-1]
            else:
                # go up first.
                npress += (X[i][-1] - cur_pressure) + (X[i][-1] - X[i][0])
                cur_pressure = X[i][0]
        else:
            # we only need to go up to X[-1] or down to X[0]. We don't have a choice so can't effect
            # the next customer.
            if cur_pressure < X[i][-1]:
                # inc. pressure
                npress += X[i][-1] - cur_pressure
                cur_pressure = X[i][-1]
            else:
                # dec. pressure
                npress += cur_pressure - X[i][0]
                cur_pressure = X[i][0]
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