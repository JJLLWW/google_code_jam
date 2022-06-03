#include <iostream>
#include <vector>
#include <utility>
#include <map>

// get 2d map of altitudes.

// if cell has altitude C, neighbours have altitudes N1 - N4, if C<=Ni is sink (no flow),
// otherwise C flows to min(Ni), if tie flow N (most likely), W, E, S.

// "drainage basin" defined as set of all cells that drain to the same sink. if cat rows of map
// basins are labelled from 'a' to 'z' such that the string is lexicographically least.

using map = std::vector<std::vector<int>>;
using labels = std::vector<std::vector<char>>;
using cell = std::pair<int, int>;
using sink_map = std::map<std::pair<int,int>, char>;

// RVO
map read_map() {
    int W, H;
    std::cin >> H >> W;
    map alts;
    for(int i=0; i<H; i++) {
        std::vector<int> row;
        for(int j=0; j<W; j++) {
            int alt;
            std::cin >> alt;
            row.push_back(alt);
        }
        alts.push_back(row);
    }
    return alts;
}

// was there a neater way of doing this?
cell get_least_neig(int i, int j, int W, int H, const map& alts) {
    int least = alts[i][j];
    cell least_n = {i, j};
    bool tie = false;
    // do in order S, E, W, N in case of a tie.
    if(i<H-1 && alts[i+1][j] < least) { // S
        least_n = std::make_pair(i+1, j);
        least = alts[least_n.first][least_n.second];
        tie = true;
    }
    if(j<W-1 && (alts[i][j+1] < least || tie && alts[i][j+1] <= least)) { // E
        least_n = std::make_pair(i, j+1);
        least = alts[least_n.first][least_n.second];
        tie = true;
    }
    if(j>0 && (alts[i][j-1] < least || tie && alts[i][j-1] <= least)) { // W
        least_n = std::make_pair(i, j-1);
        least = alts[least_n.first][least_n.second];
        tie = true;
    }
    if(i>0 && (alts[i-1][j] < least || tie && alts[i-1][j] <= least)) { // N
        least_n = std::make_pair(i-1, j);
        least = alts[least_n.first][least_n.second];
    }
    return least_n;
}

cell get_sink(int W, int H, cell cur, const map& alts, sink_map& sinks) {
    while(true) {
        cell next = get_least_neig(cur.first, cur.second, W, H, alts);
        if(next == cur) break;
        cur = next;
    }
    return cur;
}

// brute force, calculate the sink each cell drains to by following the rules
labels solve_map(const map& alts) {
    int H = alts.size(), W = alts[0].size();
    labels labs = std::vector<std::vector<char>>(H, std::vector<char>(W, ' '));
    char cur_char = 'a';
    sink_map sinks;
    for(int i=0; i<H; i++) {
        for(int j=0; j<W; j++) {
            cell cur = std::make_pair(i, j);
            cell sink = get_sink(W, H, cur, alts, sinks);
                if(sinks.count(sink) == 0) {
                sinks[sink] = cur_char;
                cur_char++;
            }
            labs[i][j] = sinks[sink];
        }
    }
    return labs;
}

void print_labels(int i, const labels& labs) {
    std::cout << "Case #" << i << ":" << std::endl;
    for(const auto& row : labs) {
        for(int i=0; i<row.size()-1; i++) {
            std::cout << row[i] << " ";
        }
        std::cout << row[row.size()-1] << std::endl;
    } 
}

int main() {
    int T;
    std::cin >> T;
    for(int i=1; i<=T; i++) {
        map alts = read_map();
        labels labs = solve_map(alts);
        print_labels(i, labs);
    }
}