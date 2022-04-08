#include <stdio.h>
#include <set>
#include <numeric>
#include <vector>

typedef long ll;
using namespace std;

// we have U[19] >= 1 guaranteed.
int N, A, B, U[21];

bool is_possible() {
    // for now, only try and solve Test Set 1.
    return true;
}

bool is_valid_solution(int y) {
    multiset<int> X, desired;
    for(int i=1; i<=N; i++) {

    }
    return false;
}

ll solve() {
    if(!is_possible()) {
        return 0;
    }
    ll y = N+1;
    while(true) {
        if(is_valid_solution(y)) {
            return y;
        }
        y += 1;
    }
}

int main() {
    int ncases;
    scanf("%d", &ncases);
    for(int c=1; c<ncases+1; c++) {
        scanf("%d%d%d", &N, &A, &B);
        for(int i=1; i<N+1; i++) { scanf("%d", &U[i]); }
        ll res = solve();
        if(res == 0) {
            printf("Case #%d: IMPOSSIBLE\n", c);
        } 
        else {
            printf("Case #%d: %ld\n", c, res);
        }
    }
}