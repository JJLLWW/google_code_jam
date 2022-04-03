# object oriented approach.

class node:
    def __init__(self):
        self.idx = None
        self.factor = None
        self.next = None
        # set if an initiator node
        self.mfac = None

class mfac:
    def __init__(self, factor, val_idx, init_idx):
        self.factor = factor
        self.val_idx = val_idx
        self.init_idx = init_idx

    # overloaded equals so can use count() on a list of them
    def __eq__(self, other):
        if self.factor == other.factor and self.val_idx == other.val_idx:
            return True
        else:
            return False

class graph:
    def __init__(self, factors, next):
        self.nmods = len(factors)
        self.nodes = [node() for i in range(self.nmods)]
        self.inits = []
        self.ninit = 0
        self.mfacs = []
        # initialise internal representation of the nodes
        for i in range(self.nmods):
            # switch to internal zero index as simpler
            self.nodes[i].idx = i
            self.nodes[i].factor = factors[i]
            # void node is represented by None
            next_idx = next[i] if next[i] != 0 else None
            self.nodes[i].next = self.nodes[next_idx]
        # record which nodes are initiators
        for i in range(self.nmods):
            if i not in next:
                self.inits.append(self.nodes[i])
        self.ninit = len(self.inits)
        # do an initial calculation of the maximum factor mfac of the path from any initiator to void.
        for i in range(self.ninit):
            maxfac, mfac_idx = self.factor_of_path(self.inits[i], None)
            mfac = mfac(maxfac, mfac_idx, i)
            self.mfacs.append(mfac)

    # return the value and index of the maximum factor along the path from src to dest.
    def factor_of_path(src, dest):
        maxfac = src.factor
        maxfac_idx = src.idx
        curr = src
        while curr.next != dest:
            curr = curr.next
            if curr.factor > maxfac:
                maxfac = curr.factor
                maxfac_idx = curr.idx
        return maxfac, maxfac_idx

    def get_global_maxfac(self):
        # assumption: there will be no repeated factors after one pass.
        for mfac in self.mfacs:
            if self.mfacs.count(mfac) > 1:
                # find the best place to move this mfac to.
                initor = self.inits[mfac.init_idx]
                end_node = self.nodes[mfac.val_idx]
                maxval, maxidx = 0, 0


        # now the sum of the maxfacs is a maximum factor
        return sum(self.mfacs)
        
def main():
    pass

main()