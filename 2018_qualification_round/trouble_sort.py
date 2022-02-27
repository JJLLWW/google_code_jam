def swap(data, i, j):
    tmp = data[i]
    data[i] = data[j]
    data[j] = tmp

def faster_sort(data, ndata):
    # trouble_sort effectively sorts 2 sublists oxoxo xoxox using bubble sort.
    # if we sort them with a faster algorithm, we will still get the same output.
    # will this use too much memory?
    data_sorted = [0]*ndata
    data_sorted[1::2] = sorted(data[1::2])
    data_sorted[0::2] = sorted(data[0::2])
    return data_sorted

def main():
    ncases = int(input())
    for case in range(1, ncases+1):
        ndata = int(input())
        line = input()
        words = line.split()
        data = [int(word) for word in words]
        data = faster_sort(data, ndata)
        failed = False
        for i in range(ndata-1):
            if data[i] > data[i+1]:
                print(f"Case #{case}: {i}")
                failed = True
                break
        if not failed:
            print(f"Case #{case}: OK")

main()