import linepy as lp 

m1 = lp.Matrix([2,3,2], [1,2,5])
m2 = lp.Matrix([1,0], [2,5])
print("m1 = ", m1, "m2 = ", m2)
# Initiallize matrices

try:
    A = lp.Matrix([2,3], [[2,3]])
except Exception as e:
    print(e)
# Should be a list of numbers

try:
    A = lp.Matrix([2,3], [2])
except Exception as e:
    print(e)
# Should have a valid Matrix structure
# Components should all have the same length

print("Components of m1:", m1.components)
# Get the components as a list of rows

m1.set_components([2,2], [1,5.7])
print(m1)
# Change the components 

m3 = lp.Matrix([4,5,6,7], [8,7,5,9])
print(m3)
print("m3 dimensions is: ", m3.dimensions)
# dimensions as tuple contain (rows, cols)

print(f"{m1} + {m2} = {m1 + m2}")
print(f"{m1} - {m2} = {m1 - m2}")
# Basic operations

x = lp.Vector(1,2)
print(f"{m1}*2 = {m1*2}")
print(f"{m1}*{x} = {m1*x}")
print(f"{m1}*{m2} = {m1*m2}")
# Multiplication with scalar, vector and matrix