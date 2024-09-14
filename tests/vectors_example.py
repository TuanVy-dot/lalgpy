import linepy as lp

v1 = lp.Vector(1, 2, 3)
# Initiallize a vector named v1 with component 1, 2, 3
v2 = lp.Vector(0, 1, 4.3)
# Initiallize v2

print(v1, v2)
# String representation of vectors

try:
    v3 = lp.Vector("2", 5, 6)
except Exception as e:
    print(e)
# Vector components only accept type int

print(v1.components)
# Get the components

v1.set_components(1, 0, 0)
print(v1)
# Set new components for v1

print("dimensions of v1:", v1.dimensions)
# Get the dimensions of vectors

m1 = v1.magnitude
print("v1 magnitude is: ", m1)
# The magnitude of a vector

print("v1 + v2 = ", v1 + v2)
print("v1 - v2 = ", v1 - v2)
# Vectors addition and subtraction 

try:
    a = v1 + 2 
except Exception as e:
    print(e)
# Add the wrong type 

try:
    a = v1 + lp.Vector(2, 3)
except Exception as e:
    print(e)
# Adding vectors should be in the same dimensions

print("v1 * 2 = ", v1 * 2)
print("v2 / 5 = ", v2 / 5)
print("v1 // 2 = ", v1 // 2)
# Scalar operations

try:
   a = v1*v2
except Exception as e:
    print(e)
# You can't multiply vectors like this, use lp.Vector.dot(v1, v2)
# And lp.Vector.cross(v1, v2) instead

print("v1 == v2?", v1==v2)
print("v1 != v2?", v1!=v2)
# Equality statements 

v3 = lp.Vector(0.235, 0.6, 1.7, 2)

v3.round(2)
print(v3)
# Round v3 up to 2 decimal places

print(v3.round())
# You would get None, instead do the following
# If you want a return

v3_prime = v3.rounded()
print(v3)
print(v3_prime)
# Return the rounded version of v3 while v3 stay the same

v3_prime = round(v3)
print(v3_prime)
# You can also use the built-in round() function, same as rounded

print("v1 dot v2 = ",lp.Vector.dot(v1, v2))
# The dot product of two vectors 

try:
    lp.Vector.dot(v1, 2)
except Exception as e:
    print(e)
# Dot product required 2 vectors 

try:
    lp.Vector.dot(
        lp.Vector(1, 0), lp.Vector(2, 3, 0)
        )
except Exception as e:
    print(e)
# Dot product required 2 vectors in the same dimensions 

print(lp.Vector.cross(v1, v2))
# The cross product between two 3D vectors 

try:
    lp.Vector.cross(v1, 2)
except Exception as e:
    print(e)
# Inputs should both be vectors 

try:
    lp.Vector.cross(
        lp.Vector(1,2), lp.Vector(2, 3, 2)
        )
except Exception as e:
    print(e)
# Only supported 3 dimensions for now

print("The angle between v1 and v2 is: ", lp.Vector.get_angle(v1, v2))
# Get angle between 2 vectors in radians
# To get on degrees, do this
print("deg: ", lp.Vector.get_angle(v1, v2, rad=False))

print("The direction of v1 is: ", lp.Vector.get_angle(v1, lp.Vector(1, 0)))
# You can get the direction by getting the angle between a vector 
# and a basis vector of your choice 

try:
    lp.Vector.get_angle(v1, 2)
except Exception as e:
    print(e)
# Two inputs better be both vectors 

try:
    lp.Vector.get_angle(
        lp.Vector(1), lp.Vector(1, 3)
        )
except Exception as e:
    print(e)
# And should be in the same dimensions too 

try:
    lp.Vector.get_angle(
       lp.Vector(1,0), lp.Vector(0,0)
        )
except Exception as e:
    print(e)
# Both vectors should also have a non-zero magnitude 

v1.resize(2)
print(v1)
# You can truncate a vector into lower dimensions 

v1.resize(5)
print(v1)
# Or also extend it into higher dimensions 

try:
    v1.resize(2.3)
except Exception as e:
    print(e)
# Dimensions should be type int only
