# LAlgPy
LAlgPy short for Python Linear Algebra is a lightweight Python package that support simple operation for **Linear Algebra**.
It provides several features such as `Vector()` and `Matrix()` class. 
Additionally, it have a utilities module which provides `array_add()` and more. I made this package mainly for **practice** and not recommend for 
important and technical uses. Here are some examples:
```py
import lalgpy as lp
v1 = lp.Vector(1,0)
v2 = lp.Vector(0,1)
print(v1, v2)
print(f"{v1} + {v2} = {v1 + v2}")
```
The output should be
```
Vector(1,0) Vector(0,1)
Vector(1,0) + Vector(0,1) = Vector(1,1)
```
It have some "shortcut" that help you calculate very quickly
```py
x = lp.Vector(2,5,2)
y = lp.Vector(5,8,3)
print(lp.Vector.dot(x,y))
# The dot product
print(lp.Vector.cross(x,y))
# The cross product
print(lp.Vector.get_angle(x,y,rad=False))
# Get the angle between two vectors
```
The output should be:
```
56
Vector(-1,4,-9)
10.024987862075728
```

And much more features.
*****
For more documentation, I suggest looking at the source, it is well documented.
## Installation
```
pip install linearpy
```
This should install the package via the ***PYPI*** repository.
**Latest**: 1.0.0 release

This is not a completed version of the package, issues can arrive and the `Matrix` class is not all implemented.
