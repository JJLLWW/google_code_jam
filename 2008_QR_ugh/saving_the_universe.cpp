#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>
#include <set>

// using iostream is much harder than the actual problem
void read_input(int& neng, std::vector<int>& quer) {
    // use cin.ignore() to get rid of newlines that cin won't read ):
    std::unordered_map<std::string, int> eng_idxs;
    int Q;
    std::cin >> neng;
    std::cin.ignore();
    std::string line;
    for(int j=0; j<neng; j++) {
        std::getline(std::cin, line);
        eng_idxs.insert({line, j});
    }
    std::cin >> Q;
    std::cin.ignore();
    for(int j=0; j<Q; j++) {
        std::getline(std::cin, line);
        quer.push_back(eng_idxs[line]);
    }
}

// strategy, move along query list until we have seen every engine, then we are forced to switch.
int solve(int neng, std::vector<int>& quer) {
    int nswtch = 0;
    std::set<int> seen;
    for(const auto& q : quer) {
        seen.insert(q);
        if(seen.size() == neng) {
            nswtch += 1;
            seen.clear();
            seen.insert(q);
        }
    }
    return nswtch;
}

int main() {
    int N;
    std::cin >> N;
    for(int i=1; i<N+1; i++) {
        int neng;
        std::vector<int> quer;
        read_input(neng, quer);
        int res = solve(neng, quer);
        std::cout << "Case #" << i << ": " << res << std::endl;
    }
}