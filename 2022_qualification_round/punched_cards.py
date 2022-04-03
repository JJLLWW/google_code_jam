def output_first_border(ncols):
    print("..", end='')
    for i in range(ncols-1):
        print("+-", end="")
    print("+")

def output_border(ncols):
    print('+', end='')
    for i in range(ncols):
        print("-+", end='')
    print('')

def output_row(ncols, first=False):
    first_char = "|" if not first else "."
    print(first_char, end='')
    for i in range(ncols):
        print(".|", end="")
    print('')

def main():
    ncases = int(input())
    for case in range(1, ncases+1):
        words = input().split()
        nrows, ncols = int(words[0]), int(words[1])
        print(f"Case #{case}:")
        # we know there are at least two rows
        output_first_border(ncols)
        output_row(ncols, first=True)
        output_border(ncols)
        for i in range(nrows-1):
            output_row(ncols)
            output_border(ncols)

main()