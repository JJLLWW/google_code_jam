from functools import reduce
from itertools import chain, combinations
import itertools as it
from operator import mul

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

def brute_force_2(M, P, N):
    # for test set 2, we have 2<=P_i<=499, and 2<=N<=100, so the sum is <=49900 < 2^16.
    # therefore we must have a product of at most m = min(16,N) primes.
    n = sum(N)
    m = min(16, n)
    primes = []
    for i in range(M):
        for j in range(N[i]):
            primes.append(P[i])
    max = 0
    combs = it.chain(it.combinations(primes, i) for i in range(1,min(m+1,n)))
    for combs_k in combs:
        for comb in combs_k:
            # we may be getting the same combination multiple times but should still be fast enough
            mcomb = primes.copy()
            for e in comb:
                if e in mcomb:
                    mcomb.remove(e)
            product = reduce(mul, comb, 1)
            if sum(mcomb) == product:
                if sum(mcomb) > max:
                    max = sum(mcomb)
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
        mscore = brute_force_2(M, P, N)
        print(f"Case #{case}: {mscore}")

main()