import linepy as lp 

m1 = lp.Matrix([2,3], [1,2])
print(m1.components)
m1.set_components([2,3,5], [1, 7, 3])
print(m1.components)
print(m1.dimensions)
print(m1)
