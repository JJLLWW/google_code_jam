#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cassert>

struct train {
    int time;
    bool dep;
    bool operator<(const train& rhs) {
        if(this->time < rhs.time) {
            return true;
        } else if(this->time == rhs.time) {
            // count an arrival as being "before" a departure at the same time.
            if((this->dep == false) && (rhs.dep == true)) {
                return true;
            }
        }
        return false;
    }
};

// assume s is of the form DD:DD where D is a digit between 0 and 9 inclusive.
int get_time_in_min(std::string& s) {
    std::string hrs, mins;
    hrs = s.substr(0,2);
    mins = s.substr(3,2);
    return std::stoi(hrs) * 60 + std::stoi(mins);
}

void get_trains(int T, int num, std::vector<train>& DEPS, std::vector<train>& ARRS) {
    std::string time1_s, time2_s;
    int time1, time2;
    for(int i=0; i<num; i++) {
        std::cin >> time1_s >> time2_s;
        time1 = get_time_in_min(time1_s);
        // factor in the turnaround time of arrivals
        time2 = get_time_in_min(time2_s) + T;
        DEPS.push_back({time1, true});
        ARRS.push_back({time2, false});
    }

}

void read_input(std::vector<train>& TTA, std::vector<train>& TTB) {
    // it makes more sense to store all arrivals and departures in order at each station.
    // additionally trains are considered to arrive when their turnaround time has expired and are able
    // to leave immediately
    int T, NA, NB;
    std::cin >> T >> NA >> NB;
    get_trains(T, NA, TTA, TTB);
    get_trains(T, NB, TTB, TTA);
    // ascending order
    std::sort(TTA.begin(), TTA.end());
    std::sort(TTB.begin(), TTB.end());
}

// A < (-1) < (-2) < (-3) > (-2) > (-1) < >
int solve_one_station(std::vector<train>& TTX) {
    // what happens if a train arrives at the same time one leaves?
    int least = 0, cur = 0;
    for(const train& tr : TTX) {
        if(tr.dep) {
            cur -= 1;
            if(cur < least) {
                least = cur;
            }
        }
        else {
            cur += 1;
        }
    }
    assert(least <= 0);
    return -least;
}

void solve(int& TA, int& TB, std::vector<train>& TTA, std::vector<train>& TTB) {
    // assume TTA and TTB are in increasing order.
    TA = solve_one_station(TTA);
    TB = solve_one_station(TTB);
}

int main() {
    int N;
    std::cin >> N;
    for(int i = 1; i < N+1; i++) {
        std::vector<train> TRAINS_A, TRAINS_B;
        int TA = 0, TB = 0;
        read_input(TRAINS_A, TRAINS_B);
        solve(TA, TB, TRAINS_A, TRAINS_B);
        std::cout << "Case #" << i << ": " << TA << " " << TB << std::endl; 
    }
}