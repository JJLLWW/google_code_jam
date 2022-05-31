def read_intlist():
    words = input().split()
    return [int(word) for word in words]

def get_all_digits(n):
    dig = []
    while n != 0:
        dig.append(n%10)
        n //= 10
    dig.reverse()
    return dig

def solve(Y):
    X = Y+1
    while True:
        # test if X is roaring
        dig = get_all_digits(X)
        split = []
        is_roaring = False
        i = 0
        for first_sz in range(1,):
        if is_roaring:
            return X
        X += 1

def main():
    ncases = int(input())
    for case in range(1, ncases+1):
        Y = int(input())
        print(f"Case #{case}:")

main()