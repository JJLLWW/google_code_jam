# strategy: we know this is possible if the sum of the minimum C_i, M_i,
# Y_i and K_i is >= 10^6.

def get_input_colors(colors):
    # assume the input line is just 4 space seperated numbers
    words = input().split()
    nums = [ int(word) for word in words ]
    for i in range(4):
        colors[i].append(nums[i])

def main():
    ncases = int(input())
    for case in range(1, ncases+1):
        c, m, y, k = [], [], [], []
        colors = [c, m, y, k]
        for i in range(3):
            get_input_colors(colors)
        mins = [min(x) for x in colors]
        if sum(mins) < 10**6:
            print(f"Case #{case}: IMPOSSIBLE")
            continue
        else:
            for i in range(4):
                if sum(mins) == 10**6:
                    break
                sum_others = sum(mins) - mins[i]
                if sum_others >= 10**6:
                    mins[i] = 0
                else:
                    # watch out for this line
                    delta = abs(sum(mins)-10**6)
                    mins[i] -= delta
            print(f"Case #{case}: {mins[0]} {mins[1]} {mins[2]} {mins[3]}")

main()