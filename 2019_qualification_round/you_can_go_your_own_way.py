def main():
    # Strategy: reflect Lydia's moves, S->E, E->S.
    ncases = int(input())
    for case in range(1,ncases+1):
        N = int(input())
        moves = input()
        moves = moves.replace('S','T')
        moves = moves.replace('E', 'S')
        moves = moves.replace('T', 'E')
        print(f"Case #{case}: {moves}")

main()