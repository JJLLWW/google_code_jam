def add_digits_to_set(n, s):
    while n > 0:
        s.add(n%10)
        n //= 10

def main():
    # strategy, if N isn't 0, we must get every digit in [0-9] at least once.
    # If N is d digits, and nonzero, then for any D in [0,1,2,3,4,5,6,7,8,9], we have there 
    # is k such that
    # D*10**(d+1) <= N < (D+1)*10**(d+1)
    # meaning we see each of [0-9] at least once eventually.

    ncases = int(input())
    for case in range(1, ncases+1):
        N = int(input())
        if N == 0:
            print(f"Case #{case}: INSOMNIA")
            continue
        digits_seen = set()
        curnum = 0
        # we know we must get every digit eventually
        while len(digits_seen) < 10:
            curnum += N
            add_digits_to_set(curnum, digits_seen)
        print(f"Case #{case}: {curnum}")

main()