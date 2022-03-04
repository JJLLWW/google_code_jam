from unicodedata import decimal
from matplotlib import pyplot as plt
import numpy as np
import itertools

def unit_vector(v):
    return v/np.linalg.norm(v)

def get_vertical_angle(v):
    v_unit = unit_vector(v)
    # clip just traps the value in [-1.0, 1.0]
    dot_prod = np.clip(np.dot([0,1], v_unit), -1.0, 1.0)
    angle = np.arccos(dot_prod)
    # convert from [-pi, pi] range to [0, 2*pi] range
    return np.mod(angle, 2*np.pi)

def get_convex_hull(pts):
    """
    Return sequence of vertices representing the convex hull of pts, use gift wrapping algorithm 
    (bad).
    """
    # leftmost points are guaranteed to be in the convex hull
    minpt = min(pts, key = lambda x: x[0])
    for pt in pts:
        print(get_vertical_angle(np.subtract(pt, minpt)))

def get_polygon_area(pts):
    raise NotImplementedError("get_polygon_area")

def main():
    face_vecs = np.array([[1/2,0,0],[0,1/2,0],[0,0,1/2]])
    three_signs = [[1, -1]]*3
    three_signs = list(itertools.product(*three_signs))
    # may not be very efficient, or the easiest way to do this.
    corners = np.array([signs[0]*face_vecs[0] + signs[1]*face_vecs[1] + signs[2]*face_vecs[2] for signs in three_signs])
    proj_corners = corners[:,:2]
    # we may have repeats, try and eliminate floats that are almost equal as well.
    proj_corners = np.unique(proj_corners, axis=0)
    # now get the 2d convex hull and its area. (gift wrapping algorithm as small set of points)
    plt.scatter(proj_corners[:,0], proj_corners[:,1])
    get_convex_hull(proj_corners)
    plt.show()

main()