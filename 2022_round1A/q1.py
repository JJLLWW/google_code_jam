def read_intlist():
    words = input().split()
    return [int(word) for word in words]

def solve(s):
    i, l = 0, len(s)
    res = ''
    while True:
        # get block of character
        char = s[i]
        for j in range(i, l):
            if s[j] != char:
                j -= 1
                break
        if j == l - 1:
            # this is the last block, dont double
            nchrs_block = (j-i)+1
            res += char*(nchrs_block)
            return res
        # compare it to character at the end
        endchar = s[j+1]
        nchrs_block = (j-i)+1
        if char < endchar:
            # double
            res += char*(2*nchrs_block)
        else:
            # don't double
            res += char*(nchrs_block)
        i = j+1

def main():
    ncases = int(input())
    for case in range(1, ncases+1):
        s = input()
        r = solve(s)
        print(f"Case #{case}: {r}")

main()