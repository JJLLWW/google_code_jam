#include <iostream>
#include <vector>
#include <string>
#include <cassert>

// just test whether each word matches the pattern O(N*D*L)

// is there some clever data structure to make the next parts simpler?
void read_words(int D, std::vector<std::string>& words) {
    words.reserve(D);
    std::string line;
    for(int i=0; i<D; i++) {
        std::cin >> line;
        words.push_back(line);
    }
}

void read_pattern(std::vector<std::vector<bool>>& pat) {
    std::string line;
    std::cin >> line;
    int c_idx = 0;
    for(int i=0; i<line.size(); i++) {
        if(line[i] == '(') {
            i++;
            while(line[i] != ')') {
                pat[c_idx][line[i]-'a'] = true;
                i++;
            }
        }
        else {
            pat[c_idx][line[i]-'a'] = true;
        }
        c_idx++;
    }
}

// internal representation of the pattern is bool pat[L][26], where pat[i][j] means
// jth letter of alphabet is a match for the ith character.

int solve(int L, const std::vector<std::string>& words) {
    std::vector<std::vector<bool>> pat(L, std::vector<bool>(26, false));
    read_pattern(pat);
    // go through each word and see if it matches
    int nmatch = 0;
    for(const auto& word : words) {
        bool match = true;
        for(int i=0; i<L; i++) {
            char c = word[i];
            if(pat[i][c-'a'] == false) {
                match = false;
                break;
            }
        }
        if(match) {
            nmatch++;
        }
    }
    return nmatch;
}

// input: line1 -> L D N, D lines with the words, N test cases
int main() {
    int L, D, N;
    std::cin >> L >> D >> N;
    std::vector<std::string> words;
    read_words(D, words);
    for(int i=1; i<N+1; i++) {
        int K = solve(L, words);
        std::cout << "Case #" << i << ": " << K << std::endl;
    }
}