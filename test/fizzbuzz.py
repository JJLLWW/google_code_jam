# find sum of ints in [1,N] not multiples of A or B
# 1 <= N,A,B <= 10**9
# Input: N A B

import math

def read_input():
    words = input().split()
    N, A, B = int(words[0]), int(words[1]), int(words[2])
    return N, A, B

# sum of first q multiples of d
def sum_mult(q, d):
    # sum first n integers is n*(n+1)/2, order of evaluation to avoid
    # floating point errors
    return (d*q*(q+1))//2

def solve():
    N, A, B = read_input()
    # we don't need to consider A > N or B > N seperately as nmultA
    # or nmultB will be zero
    nmultA = N//A
    nmultB = N//B
    # LCM
    nmultAandB = N//(math.lcm(A,B))
    sum_multA = sum_mult(nmultA, A)
    sum_multB = sum_mult(nmultB, B)
    sum_multAandB = sum_mult(nmultAandB, math.lcm(A,B))
    # inclusion-exclusion
    sum_multAorB = sum_multA + sum_multB - sum_multAandB
    total = sum_mult(N,1)
    return total - sum_multAorB

def test_main():
    while True:
        main()

def main():
    res = solve()
    print(res)
    
main()