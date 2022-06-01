#include <iostream>
#include <string>
#include <cmath>
#include <cassert>

// most complicated code jam problem I've ever seen.

double PI = 3.1415926535897932385;
int MAX_DEPTH = 10;

struct pt {
    pt(double X, double Y) {
        this->x = X;
        this->y = Y;
    }
    double x;
    double y;
    pt operator+(pt other) {
        return pt(this->x + other.x, this->y + other.y);
    }
    pt operator-(pt other) {
        return pt(this->x - other.x, this->y - other.y);
    }
    pt operator*(double k) {
        return pt(k*this->x, k*this->y);
    }
    double norm() {
        return std::sqrt((this->x)*(this->x) + (this->y)*(this->y));
    }
};

// just approximate the area in the case where the square is being intersected by the circle.
double get_approximate_area(pt bl, pt tr, double side, double rad, int depth) {
    // top right points of quadrants of existing square
    pt tr_q[4] = {tr, {(bl.x + tr.x)/2, tr.y}, (bl + tr)*0.5, {tr.x, (bl.y + tr.y)/2}};
    pt bl_q[4] = {(bl + tr)*0.5, {bl.x, (bl.y + tr.y)/2}, bl, {(bl.x + tr.x)/2, bl.y}};
    side /= 2;
    double area = 0;
    for(int i=0; i<4; i++) {
        if(tr_q[i].norm() < rad) {
            // fully inside circle, full area of square.
            area += side*side;
        }
        else if(bl_q[i].norm() > rad) {
            // fully outside circle, no area
        }
        else {
            if(depth < MAX_DEPTH) {
                area += get_approximate_area(bl_q[i], tr_q[i], side, rad, depth+1);
            } else {
                // just guess because hopefully the area is now small enough to not have much effect.
                area += 0.5*side*side;
            }
        }
    }
    return area;
}

double get_area_region(pt X, double side_len, double rad) {
    double area_region = 0;
    pt diag1 = {0.5*side_len, 0.5*side_len}, diag2 = {0.5*side_len, -0.5*side_len};
    pt tr = X + diag1, bl = X - diag1, br = X + diag2, tl = X - diag1;
    if(tr.norm() < rad) {
        // hole fully inside racket, just calculate area of square.
        area_region = side_len * side_len;
    }
    else if(bl.norm() > rad) {
        // hole fully outside racket, we don't need to calculate any area.
        area_region = 0;
    }
    else {
        // hole on racket boundary.
        area_region = get_approximate_area(bl, tr, side_len, rad, 0);
    }
    assert(area_region >= 0);
    return area_region;
}
// put axes at centre of the racket parallel to the two strings, by symmetry we only need
// to think about the top left quadrant. Then 
double solve(double f, double R, double t, double r, double g) {
    double delta = 2*r + g;
    double origin = r + 0.5*g;
    double bound = R + delta;
    double side_len = g - 2*f;
    if(side_len <= 0) {
        return 1;
    }
    // take into account the racket ring hitting the fly with the -f.
    double inner_radius = R - t - f;
    assert(inner_radius > 0);
    double whole_area = (PI * R * R)/4;
    double miss_area = 0;
    // iterate through all centres on the lattice
    for(double x = origin; x <= bound; x += delta) {
        for(double y = origin; y <= bound; y += delta) {
            pt X = {x, y};
            double area_reg = get_area_region(X, side_len, inner_radius);
            miss_area += area_reg; 
        }
    }
    double prob_hit = (whole_area - miss_area)/whole_area;
    return prob_hit;
}

// #define FLYS_DEBUG

#ifndef FLYS_DEBUG
int main() {
    int N;
    std::cin >> N;
    for(int i=0; i<N; i++) {
        double f, R, t, r, g;
        std::cin >> f >> R >> t >> r;
        std::string ugh;
        std::getline(std::cin, ugh);
        g = std::stod(ugh);
        double res = solve(f, R, t, r, g);
        std::cout << "Case #" << i+1 << ": " << res << std::endl;
    }
}
#else
int main() {
    pt X = {0.5, 0.5};
    std::cout << get_area_region(X, 1, 1) << std::endl;
}
#endif