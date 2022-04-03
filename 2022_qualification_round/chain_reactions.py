# strategy: for each initiator record the maximum factor along the route from the initiator to void, call this the
# mnode of the initiator. If any mnode is common, recompute the mnode for each initiator and choose the recomputation
# with the least factor, do this to the node as many times as necessary to minimise the sum of the factors.

def get_case():
    words = input().split()
    factors = [int(word) for word in words]
    words = input().split()
    next = [int(word) for word in words]
    return factors, next

def get_initiators(next, nmod):
    idxs = []
    for i in range(1,nmod+1):
        if i not in next:
            idxs.append(i)
    return idxs

# get the maximum node from initiator with index idx.
def calc_max_node(idx, factors, next):
    curr_idx = idx
    maxval = factors[idx-1]
    while next[curr_idx-1] != 0:
        curr_idx = next[curr_idx-1]
        if factors[curr_idx-1] > maxval:
            maxval = factors[curr_idx-1]
    return maxval

# idxs is a list of initiator indeces. Also return the index of the mnode.
def get_initial_mnodes(idxs, factors, next):
    max_nodes = []
    mn_idxs = {}
    for idx in idxs:
        mnode = calc_max_node(idx, factors, next)
        max_nodes.append(mnode)
        if mnode not in mn_idxs.keys():
            mn_idxs[mnode] = []
        mn_idxs[mnode].append(idx)
    return max_nodes, mn_idxs

def remove_repeated(idx, factors, next):
    pass

def main():
    ncases = int(input())
    for case in range(1, ncases+1):
        nmod = int(input())
        factors, next = get_case()
        idxs = get_initiators(next, nmod)
        # mn_idxs keeps track of the 
        max_nodes, mn_idxs = get_initial_mnodes(idxs, factors, next)
        # now find a fast way to remove the repeated mnodes.
        print(f"{max_nodes}, {mn_idxs}")

main()