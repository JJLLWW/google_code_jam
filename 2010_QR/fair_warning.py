# for all y>=0 there is supposedly a greatest common divisor T of ALL (y+ti)

def main():
    C = int(input())
    for case in range(1, C+1):
        words = input().split()
        N = int(words[0])
        t = []
        for i in range(1, N+1):
            t.append(int(words[i]))
        print(t)
        res = 0
        print(f"Case #{case}: {res}")

main()