#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <windows.h>

using ll = long long;

// 1 - 1, 2 - 3, 3 - 4

// WRONG
int main() {
    while(true) {
        std::string line;
        std::getline(std::cin, line);
        if(line == "q") break;
        int N = std::stoi(line);
        ll npair = 0;
        std::vector<int> squares(N);
        for(int i=0; i<N; i++) {
            squares[i] = i*i;
        }
        for(int i=1; i<=N; i++) {
            for(int j=1; j<=N; j++) {
                if(std::find(squares.begin(), squares.end(), i*j) != squares.end()) {
                    npair++;
                }
            }
        }
        std::cout << npair << std::endl;
    }
}
