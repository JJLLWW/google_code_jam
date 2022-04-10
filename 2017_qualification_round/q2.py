# - find the first out of order pair, such that d[i] > d[i+1].
# - set d[i+1:] = [9,9, ..., 9]
# the only way any other digits can be out of order is if there is a block
# of digits equal to d[i] before it.
# take the first element of this block d[j], set it to (d[j] - 1) % 10,
# set d[j+1:] = [9,9, ..., 9]


def get_digits(n):
    # return list of n's digits, most significant first. 123 -> [1,2,3]
    digs = []
    while n > 0:
        digs.append(n%10)
        n //= 10
    digs.reverse()
    return digs

def int_from_digits(digs):
    # return an integer from a list of its digits.
    digs.reverse()
    vals = [digs[i]*(10**i) for i in range(len(digs))]
    return sum(vals)

def solve(N):
    d = get_digits(N)
    # all single digit numbers are tidy.
    if len(d) == 1:
        return int_from_digits(d)
    # not single digit, so can always get at least one pair here
    j = 0
    for i in range(len(d)-1):
        if d[i] > d[i+1]:
            # this may create a leading zero but we don't care.
            d[j] = (d[j] - 1) % 10
            # now set all other digits to nines. 1213 -> len = 4, j = 1
            d = d[:j+1] + [9]*(len(d) - (j+1))
            break
        # record the start of any block of repeated digits.
        if d[i] != d[i+1]:
            j = i+1
    return int_from_digits(d)

def main():
    ncases = int(input())
    for case in range(1, ncases+1):
        N = int(input())
        last_tidy = solve(N)
        print(f"Case #{case}: {last_tidy}")

main()