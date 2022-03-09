def get_first_block_sz(stack):
    blk_char = stack[0]
    end_char = '-' if blk_char == '+' else '+'
    sz = 0
    for i in range(len(stack)):
        if stack[i] == end_char:
            break
        sz += 1
    return sz

def flip_first_n(stack, n):
    blk_char = stack[0]
    desired_char = '-' if blk_char == '+' else '+'
    stack[:n] = [desired_char]*n

def main():
    # strategy: always flip the first block of - or + until we get all +.
    ncases = int(input())
    for case in range(1, ncases+1):
        stack = list(input())
        ncakes = len(stack)
        steps = 0
        while stack.count('+') < ncakes:
            blk_sz = get_first_block_sz(stack)
            flip_first_n(stack, blk_sz)
            print(stack)
            steps += 1
        print(f"Case #{case}: {steps}")

def test():
    pass

main()