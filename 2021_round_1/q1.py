def N(x):
    # number of base 10 digits in x, know x != 0
    ndig = 0
    while x != 0:
        ndig += 1
        x //= 10
    return ndig

def lead(x, ndig):
    # leading ndig digits of x
    tdig = N(x)
    lead = x // 10**(tdig-ndig)
    return lead

def all_nines(x, ndig):
    for i in range(ndig):
        if x % 10 != 9:
            return False
        x //= 10
    return True

def main():
    ncases = int(input())
    for case in range(1, ncases+1):
        n = int(input())
        words = input().split()
        X = [int(word) for word in words]
        # len(X >= 2)
        nops = 0
        for i in range(0, n-1):
            if X[i] < X[i+1]:
                continue
            dig, dig_nxt = N(X[i]), N(X[i+1])
            if dig == dig_nxt:
                X[i+1] *= 10
                nops += 1
            elif dig > dig_nxt:
                diff = dig - dig_nxt
                ldig, ldig_nxt = lead(X[i], dig_nxt), X[i+1]
                # if the leading diff digits of X[i] are < the leading diff digits of X[i+1] diff operations needed
                if ldig < ldig_nxt:
                    X[i+1] *= 10**diff
                    nops += diff
                elif ldig > ldig_nxt:
                    X[i+1] *= 10**(diff+1)
                    nops += diff + 1
                else: # equal
                    if all_nines(X[i], diff):
                        X[i+1] *= 10**(diff+1)
                        nops += diff + 1
                    else:
                        X[i+1] = X[i] + 1
                        nops += diff
            else:
                raise(ValueError("what?"))
        print(f"Case #{case}: {nops}")

main()