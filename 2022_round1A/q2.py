def read_intlist():
    words = input().split()
    return [int(word) for word in words]

def output_intlist(L):
    N = len(L)
    for i in range(N):
        if i == N-1:
            print(f"{L[N-1]}")
        else:
            print(f"{L[i]} ", end='')

def solve(A, B):
    # elements of A that are not powers of 2 occur first, meaning after they are processed,
    # sum_s1 and sum_s2 differ by at most 10**9 and hence at most 2**30.
    # differing by 2**n, and adding 2**(n-1) to the least ultimately means they differ by at most
    # 1. sum_s1 + sum_s2 is even, so there is no difference.
    C = B + A
    s1, s2 = [], []
    sum_s1, sum_s2 = 0, 0
    for elem in C:
        if sum_s1 >= sum_s2:
            s2.append(elem)
            sum_s2 += elem
        else:
            s1.append(elem)
            sum_s1 += elem
    return s1

def main():
    ncases = int(input())
    # use the same set of 50 integers A every time.
    power_2 = [2**i for i in range(30)]
    power_2.sort(reverse=True)
    A_not_power2 = [2**7 + i for i in range(1, 71)]
    A = A_not_power2 + power_2
    for case in range(1, ncases+1):
        N = int(input())
        if N != 100:
            raise ValueError("Assuming in test case N=100")
        output_intlist(A)
        B = read_intlist()
        s1 = solve(A, B)
        output_intlist(s1)

main()