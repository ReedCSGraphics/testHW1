# Homework 1: object showcase

Jim: Please install the Pillow package to run my program:
pip3 install Pillow


*Due: 9/8/2017*

(Details about submitting this homework are coming soon!) 

Modify one of my two sample GL/GLUT python programs (`showV1` or `showV2`) so that it generates faceted models of the following:

* Facets that form the surface of a cube.
* A mesh of facets that form the surface of a cylinder (parameterized).
* A mesh of facets that form the surface of a sphere (parameterized).
* A mesh of factes that form the surface of a torus (parameterized).
* Programmer's choice: depict a surface of your choosing.

For all these, you can mimic either version 1 or version 2 of my tetrahedron demo. If you choose to modify version 1, you'll want to make the sequence of **OpenGL** calls---a `glColor3f` call and three `glColor3f` calls for each facet on the object you are depicting---within an object rendering function like my `drawTetra` in `show.py`. If you choose to modify version 2, you'll want to generate a list of facet objects, mimicking my definition of the function `make_tetra` in `object.py`. 

For the cube, you will want to create the six sides out of twelve triangular facets. Each square face should be cut in half by its diagonal, and so split into two right triangular pieces. 

For the middle three, your meshing will only approximate their figures. Write the code so that it relies on a global variable named smoothness that controls the number of points that are used to sample the shape of the mesh's approximation of the figure being depicted. With more smoothness, the better its quality. For example, the cylinder could have more sides forming its "drum", and this number should be governed by the value of smoothness. To do this, you'll want to add a parameter to the functions that depict/construct the objects and then make sure that they are each called with the global smoothness variable. 

Add code to the keyboard handler function so that the + and - keys control the smoothness for these figures and so that the number keys select which object is being depicted.

For the last one, make whatever surface you like. Include a comment in the code describing to me what that shape is and how you generate it. 
