# FAILED IN TIME LIMIT, if an approach seems very hard in the qualifier, it's
# probably not the intended one.

import math

def append_if_not_in(lst, elem):
    if elem not in lst:
        lst.append(elem)

def main():
    # Strategy: gcd(p_1*p_2, p_2*p_3) = p_2. gcd() can be run in reasonable time.
    ncases = int(input())
    for case in range(1, ncases+1):
        _ = input()
        words = input().split()
        pairs = [int(word) for word in words]
        npairs = len(pairs)
        prime1 = math.gcd(pairs[0], pairs[1])
        prime0 = pairs[0]//prime1
        primes = [prime0]
        # this is not set so can be sorted later.
        distinct_primes = [prime0]
        for i in range(npairs-1):
            prime_i = math.gcd(pairs[i], pairs[i+1])
            primes.append(prime_i)
            append_if_not_in(distinct_primes, prime_i)
        last_prime = pairs[-1]//primes[-1]
        primes.append(last_prime)
        append_if_not_in(distinct_primes, last_prime)
        distinct_primes.sort()
        # hackery
        letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        msg = ""
        for prime in primes:
            idx = distinct_primes.index(prime)
            # print(idx)
            msg += letters[idx]
        print(f"Case #{case}: {msg}")

main()