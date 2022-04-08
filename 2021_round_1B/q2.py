import math

N, A, B = 0, 0, 0
U = []

def rm_intersection(X, I):
    I_copy = I.copy()
    rm_idxs = []
    for i in range(len(X)):
        if X[i] in I_copy:
            rm_idxs.append(i)
            I_copy.remove(X[i])
    rm_idxs.sort(reverse=True)
    for i in rm_idxs:
        del(X[i])

def is_valid_solution(y):
    # assume y >= N+1
    X = [y]
    DES = []
    for i in range(N):
        DES += [i+1]*U[i]
    while True:
        INTERSECT = [e for e in X if e in DES]
        rm_intersection(X, INTERSECT)
        rm_intersection(DES, INTERSECT)
        if DES == []:
            return True
        if X == []:
            return False
        m = max(X)
        X.remove(m)
        if m - A > 0:
            X.append(m-A)
        if m - B > 0:
            X.append(m-B)

def do_brute_force():
    y = 1
    while True:
        if is_valid_solution(y):
            return y
        y += 1

def is_impossible():
    # impossible if gcd(A,B) > 1 and U contains elements in multiple congruence classes
    d = math.gcd(A, B)
    seen_classes = []
    if d > 1:
        for i in range(1,N+1):
            if U[i-1] > 0:
                seen_classes.append(i%d)
            if len(seen_classes) > 1:
                return True
    return False

def solve():
    if is_impossible():
        return None
    # we know there is a solution, so just brute force it. (pray its fast enough)
    return do_brute_force()

def read_intlist():
    words = input().split()
    return [int(word) for word in words]

def main():
    global A, B, N, U
    ncases = int(input())
    for case in range(1, ncases+1):
        N, A, B = read_intlist()
        U = read_intlist()
        y = solve()
        if y is None:
            print(f"Case #{case}: IMPOSSIBLE")
        else:
            print(f"Case #{case}: {y}")

main()