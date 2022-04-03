# strategy: put the numbers of sides in increasing order. Then move left to right
# along the ordered list, adding 1 if possible to the max, otherwise doing nothing.

# not going to be this easy
def main():
    ncases = int(input())
    for case in range(1, ncases+1):
        ndice = int(input())
        words = input().split()
        dsizes = [int(word) for word in words]
        dsizes.sort()
        straight = 0
        for i in range(ndice):
            if straight < dsizes[i]:
                straight += 1
        print(f"Case #{case}: {straight}")

main()