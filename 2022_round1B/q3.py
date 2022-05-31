def read_intlist():
    words = input().split()
    return [int(word) for word in words]

def main():
    ncases = int(input())
    for case in range(1, ncases+1):
        print(f"Case #{case}:")

main()