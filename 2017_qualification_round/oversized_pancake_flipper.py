def main():
    ncases = int(input())
    for case in range(1, ncases+1):
        words = input().split()
        row, K = list(words[0]), int(words[1])
        N = len(row)
        impossible = False
        nflips = 0
        for i in range(N-K+1):
            # final step
            if i == N-K:
                if row[i] == '-' and '+' in row[i:N]:
                    impossible = True
            # do flip if see '-'
            if row[i] == '-':
                for j in range(i,i+K):
                    if row[j] == '-':
                        row[j] = '+'
                    elif row[j] == '+':
                        row[j] = '-'
                nflips += 1
        if impossible:
            print(f"Case #{case}: IMPOSSIBLE")
        else:
            print(f"Case #{case}: {nflips}")

main()