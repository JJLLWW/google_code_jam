def intlist_from_input():
    words = input().split()
    lst = [int(word) for word in words]
    return lst

def get_adjlst(P, N):
    # adj[i] is a list of indeces that point to i
    adj = [[]]*(N+1)
    for i in range(N):
        pts_to = P[i]
        adj[pts_to].append(i+1)
    return adj

def dfs(idx, adj, F, P, total):
    # do a dfs from root idx
    vals = []
    for i in adj[idx]:
        val = dfs(i, adj, F, P, total)
        vals.append(val)
    # branch 
    if len(vals) > 1:
        mval = min(vals)
        total[0] += sum(vals) - mval
        last = mval
    # straight
    else:
        last = vals[0]
    if F[idx] > last:
        last = F[idx]
    total[0] += last
    return last

def main():
    ncases = int(input())
    for case in range(1, ncases+1):
        N = int(input())
        F = intlist_from_input()
        P = intlist_from_input()
        adj = get_adjlst()
        # hacked out way to get a global variable in Python
        maxfun = [0]
        dfs(0, adj, F, P, maxfun)
        print(f"Case #{case}: {maxfun[0]}")

main()