from functools import reduce
from itertools import chain, combinations
from operator import mul

from numpy import product

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def subs_minus(s, S):
    res = S.copy()
    for e in list(s):
        if e in res:
            res.remove(e)
    return res

def brute_force(M, P, N):
    # This is O(2^n)!
    n = sum(N)
    primes = []
    for i in range(M):
        for j in range(N[i]):
            primes.append(P[i])
    max = 0
    ps = powerset(primes)
    for subset in ps:
        if len(subset) == 0 or len(subset) == len(primes):
            continue
        # !
        sminus = subs_minus(subset, primes)
        product = reduce(mul, sminus, 1)
        if sum(subset) == product:
            if sum(subset) > max:
                max = sum(subset)
    return max

def main():
    ncases = int(input())
    for case in range(1, ncases+1):
        M = int(input())
        P, N = [], []
        for i in range(M):
            words = input().split()
            P_i, N_i = int(words[0]), int(words[1])
            P.append(P_i)
            N.append(N_i)
        mscore = brute_force(M, P, N)
        print(f"Case #{case}: {mscore}")

main()