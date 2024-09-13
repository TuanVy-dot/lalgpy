import numpy as np 
from .utilities import *
from .exceptions import *
from .vectors import *

class Matrix:
    def __init__(self, *args: list[int | float]) -> None:
        for arg in args:
            if not isinstance(arg, list):
                raise TypeError("Matrix components(rows) should be a list with elements of type `int` or `float`")
            for elements in arg:
                if not isinstance(elements, (int, float)):
                    raise TypeError("Matrix components(rows) should be a list with elements of type `int` or `float`")
        if not all(len(component) == len(args[0]) for component in args):
            raise DimensionsError("Matrix components(rows) should all be the same length")
        self.__components = [*args]

    @property
    def components(self) -> list[list[int | float]]:
        return self.__components
    
    def set_components(self, *args: list[int | float]) -> None:
        self.__components = Matrix(*args).components
    
    @property
    def dimensions(self) -> tuple:
        return (len(self.__components), len(self.__components[0]))

    def __repr__(self) -> str:
        return f"Matrix{tuple(self.__components)}"

    def __add__(self, other):
        if not isinstance(other, Matrix):
            return NotImplemented
        if self.dimensions != other.dimensions:
            raise DimensionsError("Operand `+` required two matrices with the same dimensions")
        return Matrix(*[utilities.array_add(c1, c2) 
                        for c1, c2 in zip(self.components, other.components)])
