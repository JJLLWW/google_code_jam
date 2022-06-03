#include <iostream>
#include <string>
#include <cassert>

// find last 4 digits of number of times "welcome to code jam" appears in some line.

// Each line <= 500 characters, if test every ordered group of 13 characters, worst case
// 500C13 approx. 1.67 * 10^25 options. So need a better approach.

// Look for a 'w' in the string, then for each time it's found, look for an 'e', recurse deeper
// with the 'e' etc. (is this fast enough?)

using ll = long long;

// be very careful with index overruns.
ll rec_get_substr(int spos, int sspos, const std::string& substr, const std::string& str) {
    // we've already matched all the characters of substr
    if(sspos >= substr.size()) {
        return 1;
    }
    // we've still got some unmatched characters of substr, but we're at the end of str.
    if(spos >= str.size()) {
        return 0;
    }
    ll res = 0;
    // find all instances of first character of substr in str.
    for(int i=spos; i<str.size(); i++) {
        if(str[i] == substr[sspos]) {
            res += rec_get_substr(i, sspos+1, substr, str);
        }
    }
    return res;
}

int main() {
    int N;
    std::cin >> N;
    // flush newline
    std::cin.ignore();
    for(int i=1; i<=N; i++) {
        std::string line;
        std::getline(std::cin, line);
        ll ntimes = rec_get_substr(0, 0, "welcome to code jam", line);
        int dig1 = (ntimes/1) % 10;
        int dig2 = (ntimes/10) % 10;
        int dig3 = (ntimes/100) % 10;
        int dig4 = (ntimes/1000) % 10;
        std::cout << "Case #" << i << ": " << dig4 << dig3 << dig2 << dig1 << std::endl;
    }
}