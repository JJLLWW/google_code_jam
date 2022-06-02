#include <iostream>
#include <vector>

// get 2d map of altitudes.

// if cell has altitude C, neighbours have altitudes N1 - N4, if C<=Ni is sink (no flow),
// otherwise C flows to min(Ni), if tie flow N (most likely), W, E, S.

// "drainage basin" defined as set of all cells that drain to the same sink. if cat rows of map
// basins are labelled from 'a' to 'z' such that the string is lexicographically least.

struct cells {
    cells(std::vector<std::vector<int>>& alts) {
        
    }
    int W;
    int H;
    std::vector<std::vector<int>> alts;

};

// just brute force it as solving properly would be very hard.

int main() {

}