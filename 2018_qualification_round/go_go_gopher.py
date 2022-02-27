# the 1000x1000 double array is 1 indexed

def handle_one_case():
    for i in range(0,1000):
        # create the 3x? rectangle by creating a bunch of disjoint 3x3 squares,
        # centred at (1+3i, 1)
        filled = set()
        while len(filled) < 9:
            # print(f"{2+3*i} {2}", end='', flush=True)
            print(f"{2+3*i} {2}")
            new_fill = input()
            if new_fill == "0 0":
                # success, need to break out of both loops
                return True
            elif new_fill == "-1 -1":
                # failiure
                return False
            filled.add(new_fill)

def main():
    # as we never get an A anywhere close to the board width, just create a 3x?
    # rectangle on the bottom of the board.
    ncases = int(input())
    for case in range(1, ncases+1):
        A = int(input())
        if not handle_one_case():
            return False
    return True

main()