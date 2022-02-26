def swap(prog, i, j):
    tmp = prog[i]
    prog[i] = prog[j]
    prog[j] = tmp

def shot_dmg(prog):
    dmg = 0
    power = 1
    for op in prog:
        if op == 'C':
            power *= 2
        elif op == 'S':
            dmg += power
        else:
            raise ValueError("shot_dmg: prog contained a non 'C' or 'S' character")
    return dmg

def get_last_S_block_idx(prog):
    # watch out if there are no S's in the program.
    if prog.count('S') == 0:
        raise ValueError("get_last_S_block_idx called with prog with no S's")
    i = len(prog) - 1
    while True:
        if prog[i] == 'S':
            while True:
                # i < 0 to handle if just a block of S's
                if i < 0 or prog[i] == 'C':
                    return i+1
                i -= 1
        i -= 1

def main():
    nprogs = int(input())
    for i in range(1,nprogs+1):
        line = input()
        words = line.split()
        max_dmg, prog = int(words[0]), list(words[1])
        # we know its impossible if and only if there are more shots than the shield strength
        if prog.count('S') > max_dmg:
            print(f"Case #{i}: IMPOSSIBLE")
            continue
        nhacks = 0
        while shot_dmg(prog) > max_dmg:
            j = get_last_S_block_idx(prog)
            # if the last S block is at [0], we already know it is solvable, so we will already 
            # have shot_dmg <= max_dmg
            swap(prog, j-1, j)
            nhacks += 1
        print(f"Case #{i}: {nhacks}")

main()