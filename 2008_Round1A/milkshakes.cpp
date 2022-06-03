#include <iostream>
#include <vector>

// N flavours each 0 (unmalted) or 1 (malted)

// make N, one for each flavour, each customer gets one milkshake they want, minimum malted.
// only one answer.

// store customer's preferences as integer between 1 and 2N inclusive


// RVO
std::vector<int> solve(int N, std::vector<std::vector<int>>& custs) {
    std::vector<int> malt;
    return malt;
}

int main() {
    int C;
    std::cin >> C;
    for(int i=1; i<=C; i++) {
        int N, M, T;
        std::cin >> N >> M;
        std::vector<std::vector<int>> custs = std::vector(M, std::vector<int>());
        for(int j=0; j<M; j++) {
            std::cin >> T;
            for(int k=0; k<T; k++) {
                int X, Y;
                std::cin >> X >> Y;
                custs[j].push_back(X + Y*N);
            }
        }
        std::vector<int> malt = solve(N, custs);
        if(malt.size() == 0) {
            std::cout << "Case #" << i << ": IMPOSSIBLE" << std::endl;
        }
        else {
            std::cout << "Case #" << i << ": ";
            for(int j=0; j<N-1; j++) {
                std::cout << malt[j] << " ";
            }
            std::cout << malt[N-1] << std::endl;
        }
    }
}