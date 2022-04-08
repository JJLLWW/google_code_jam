def main():
    # Strategy: N = 4**44*4, A=2**22*2, B=2002202, at least one digit is a 4
    ncases = int(input())
    for case in range(1, ncases+1):
        N = int(input())
        i = 0
        A, B = 0, 0
        while N > 0:
            next_digit = N%10
            if next_digit == 4:
                A += 2*(10**i)
                B += 2*(10**i)
            else:
                A += next_digit*(10**i)
            i += 1
            N //= 10
        print(f"Case #{case}: {A} {B}")

main()