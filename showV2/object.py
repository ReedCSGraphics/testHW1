#
# object.py
#
# Defines an RGB struct 'class color'.
# Defines a three-vertex struct 'class facet', that also has a color attribute.
# Defines a function 'make_object' that produces a list of facets.
#

from geometry import point

class color:
    def __init__(self, r, g, b):
        self.red = r
        self.green = g
        self.blue = b


class facet:

    def __init__(self, _p0,_p1,_p2, _m):
        self.vertices = [_p0,_p1,_p2]
        self.material = _m

    def __getitem__(self,i):
        return self.vertices[i]


def make_tetra():

    # Make a tetrahedron.

    fs = []

    # missing ---
    c0  = color(1.0,1.0,0.0)
    p00 = point.with_components( [ 1.0,-1.0, 1.0] )
    p01 = point.with_components( [ 1.0, 1.0,-1.0] )
    p02 = point.with_components( [-1.0, 1.0, 1.0] )
    f0  = facet(p00,p01,p02,c0) 
    fs.append(f0)

    # missing ++-
    c1  = color(0.0,1.0,1.0)
    p10 = point.with_components( [ 1.0,-1.0, 1.0] )
    p11 = point.with_components( [-1.0, 1.0, 1.0] )
    p12 = point.with_components( [-1.0,-1.0,-1.0] )
    f1  = facet(p10,p11,p12,c1) 
    fs.append(f1)

    # missing -++
    c2  = color(1.0,0.0,1.0)
    p20 = point.with_components( [-1.0,-1.0,-1.0] )
    p21 = point.with_components( [ 1.0, 1.0,-1.0] )
    p22 = point.with_components( [ 1.0,-1.0, 1.0] )
    f2  = facet(p20,p21,p22,c2) 
    fs.append(f2)

    # missing +-+
    c3  = color(1.0,1.0,1.0)
    p30 = point.with_components( [ 1.0, 1.0,-1.0] )
    p31 = point.with_components( [-1.0,-1.0,-1.0] )
    p32 = point.with_components( [-1.0, 1.0, 1.0] )
    f3  = facet(p30,p31,p32,c3) 
    fs.append(f3)

    return fs


