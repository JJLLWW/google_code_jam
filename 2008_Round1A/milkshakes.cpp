#include <iostream>
#include <vector>
#include <algorithm>

// N flavours each 1 (unmalted) or 0 (malted)
// (~x1 v x2 v x3 v ~x4) - customer's preferences. (clause)
// as a whole (~x1 v x3) & (x2 v x3) & (x1 v ~x2 v ~x3)

// each clause has at most one negation. solve with minimum number of xi set to false.

// only set xi to false if have to for ~xi (if this encountered this xi must be false)

// store clause as vector of int, x%N is the variable index, x/N is malted or unmalted.

using clause = std::vector<int>;
using assignment = std::vector<int>;
using clause_set = std::vector<clause>;

// RVO
clause_set read_input(int N, int M) {
    int T;
    clause_set clauses(M);
    for(int i=0; i<M; i++) {
        std::cin >> T;
        clause cls(T);
        for(int j=0; j<T; j++) {
            int X, Y;
            std::cin >> X >> Y;
            cls[j] = X + Y*N;
        }
    }
    return clauses;
}

bool is_clause_sat(clause cls, assignment assign) {
    return false;
}

// return number of malted, or -1 on failiure.
int solve(int N, int M, clause_set& clauses) {
    int nmalt = 0;
    // 0 unmalted, 1 malted.
    std::vector<int> assign(N);
    // does milkshake i have to be malted/unmalted?
    std::vector<bool> fixed(N);
    std::fill(assign.begin(), assign.end(), 0);
    std::fill(fixed.begin(), fixed.end(), false);
    for(const clause& cls : clauses) {
        if(cls.size() == 1) {
            
        }
    }
    return nmalt;
}

int main() {
    int C;
    std::cin >> C;
    for(int i=1; i<=C; i++) {
        int N, M;
        clause_set clauses = read_input(N, M);
        int nmalt = solve(N, M, clauses);
    }
}