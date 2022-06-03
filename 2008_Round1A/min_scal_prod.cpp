#include <iostream>
#include <vector>
#include <algorithm>

// permuting v1 and v2 output the minimum possible scalar product.
// we only need to permute one vector, as only which elements are paired together matters.
// largest from 1 vector should be paired with smallest from other.

using ll = long long;

ll solve(std::vector<int>& v1, std::vector<int>& v2) {
    std::sort(v1.begin(), v1.end());
    std::sort(v2.rbegin(), v2.rend());
    ll prod = 0;
    for(int i=0; i<v1.size(); i++) {
        // danger zone: without the cast gives the wrong answer.
        prod += (ll)v1[i]*v2[i];
    }
    return prod;
}

int main() {
    int T;
    std::cin >> T;
    for(int i=1; i<=T; i++) {
        int n;
        std::cin >> n;
        std::vector<int> v1(n), v2(n);
        for(int i=0; i<n; i++) {
            std::cin >> v1[i];
        }
        for(int i=0; i<n; i++) {
            std::cin >> v2[i];
        }
        ll res = solve(v1, v2);
        std::cout << "Case #" << i << ": " << res << std::endl;
    }
}