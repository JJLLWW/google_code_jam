import bisect
import math

def read_intlist():
    words = input().split()
    return [int(word) for word in words]

def brute_force(N, K):
    # brute force should be sufficient for first 2 test cases.
    occ = [0, N+1]
    # we must stop after K people have gone.
    while len(occ) < 2+K:
        max_min_L_R = -1
        max_max_L_R = -1
        max_j = None
        for i in range(len(occ)-1):
            nbetween = (occ[i+1] - occ[i]) - 1
            if nbetween == 0:
                continue
            # (!) if 4 spaces, the minimal one will be on the 2nd from i O . . . . O ; 
            # O . . . O 
            j = occ[i] + math.ceil(nbetween/2)
            L = j - occ[i] - 1
            R = occ[i+1] - j - 1
            min_L_R, max_L_R = min(L, R), max(L, R)
            if min_L_R >= max_min_L_R:
                max_min_L_R = min_L_R
                if max_L_R > max_max_L_R:
                    # we only re-assign on strictly greater than, to get the leftmost such index j.
                    max_max_L_R = max_L_R
                    max_j = j
        bisect.insort(occ, j)
    final_L, final_R = max_min_L_R, max_max_L_R
    return final_L, final_R
            

def main():
    ncases = int(input())
    for case in range(1, ncases+1):
        N, K = read_intlist()
        L_fin, R_fin = brute_force(N, K)
        print(f"Case #{case}: {max(L_fin, R_fin)} {min(L_fin, R_fin)}")

main()

# we attempt to solve by brute forcing the procedure, hopefully there isn't
# a smart mathematical way to solve it much faster.

# why wrong answer?