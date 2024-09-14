# LinePy
LinePy is a Python package that support simple operation for **Linear Algebra**.
It provides several features such as `Vector()` and `Matrix()` class. 
Additionally, it have a utilities package which provides `array_add()` and more. I made this package mainly for **practice** and not recommend for 
important and technical uses. Here is an example:
```py
import linepy as lp
v1 = lp.Vector(1, 0)
v2 = lp.Vector(0, 1)
print(v1, v2)
print(f"{v1} + {v2} = {v1 + v2}")
```
The output should be
```
Vector(1,0) Vector(0,1)
Vector(1,0) + Vector(0,1) = Vector(1,1)
```
For more documentation, I suggest looking at the source, it is well documented.
## Installation
```
pip install linepy
```
This should install the package via the ***PYPI*** repository

This is not a completed version of the package, issues can arrive and the `Matrix` class is not all implemented
