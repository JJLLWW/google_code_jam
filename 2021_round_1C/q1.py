import math

def read_intlist():
    words = input().split()
    return [int(word) for word in words]

def solve(N, K, P):
    # look for gaps, edge case?
    P.sort()
    nspaces = []
    prob = 0.0
    for i in range(len(P)):
        # first also needs next
        endpt = False
        if i == 0:
            gap_sz = P[0] - 1
            if gap_sz > 0:
                nspaces.append(gap_sz)
        if i == len(P)-1:
            gap_sz = K - P[len(P)-1]
            if gap_sz > 0:
                nspaces.append(gap_sz)
            endpt = True
        if not endpt:
            gap_sz = P[i+1] - P[i] - 1
            if gap_sz > 0:
                sz_1 = math.ceil(gap_sz/2)
                # we may also want to put an integer on the other side of this gap.
                sz_2 = gap_sz - sz_1
                nspaces.append(sz_1)
                if sz_2 > 0:
                    nspaces.append(sz_2)
    if nspaces != []:
        m = max(nspaces)
        nspaces.remove(m)
        if nspaces == []:
            prob=m/K
        else:
            n = max(nspaces)
            prob=(m+n)/K
    return prob          

def main():
    ncases = int(input())
    for case in range(1, ncases+1):
        N, K = read_intlist()
        P = read_intlist()
        prob = solve(N, K, P)
        print(f"Case #{case}: {prob}")

main()