import numpy as np 
from .exceptions import *
from .vectors import *

class Matrix:
    def __init__(self, *args: list[float]) -> None:
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
    def components(self) -> list[list[float]]:
        return self.__components
    
    def set_components(self, *args):
        self.__components = Matrix(*args).components
