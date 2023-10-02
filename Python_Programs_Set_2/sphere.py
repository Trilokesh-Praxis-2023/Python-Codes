# The sphere module has functions that perform
# calculations related to spheres.
import math

# The volume function accepts a sphere's radius as an
# argument and returns the volume of the circle.
def volume(radius):
	return math.pi * (4/3)*radius**3

# The surf_area function accepts a circle's
# radius and returns the surface area of the sphere.
def surf_area(radius):
	return math.pi * 4.0* radius**2