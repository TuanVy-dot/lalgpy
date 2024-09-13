
"""
Mathematical object `Vector`
"""

import numpy as np
from .exceptions import *
from .utilities import *
from linepy import utilities

class Vector:
    """
Mathematical vectors

    Vector is a Mathematical object whose have both direction or magnitude, or in broader terms, anything that satisfied certain properties, this `Vector` class is the simpler one.
    Supported operations: addition, subtraction, multiplication, true division, floor division 
        Those operations work the same way as it is in math, true division will return floats whereas floor division return integers
        IMPORTANT: For multiplication and divison, those are for scalar and the vector should be the first operand. If you want to multiply two vectors, use `Vector.dot()` and `Vector.cross()`, see more later on.
    Supported statements:
        Equality(==): True if the two vectors components are the same otherwise False
        Non-Equality(!=): No more than negation of equality, True if the two vectors components are not the otherwise else False
        If the two sides are not the same type, it will return True or False depends on the nature of the statements. No inequalities supported
    Representation: 
        Formatted as `Vector(*components)`
    
    Attributes
    ----------
    __components: List
        Vectors components. Not directly changable, if you want to change vectors components, see `set_components()` method
    
    Properties
    ----------
    components(self) -> list
        Get access to the vector components as a list
    dimensions(self) -> int
        Get the vector dimensions, or just the length of the list of components
    magnitude(self) -> float
        Get the vector magnitude
    
    Methods
    -------
    set_components(self, *args: int | float)
        Set a new set of components for that vector
    round(self, decimal_places: int) -> None
        Round every components of the vector to a specific decimal_places, directly change the original vector
    rounded(self, decimal_places: int) -> Vector
        Round every components of the vector to a specific decimal_places, return a new vector, the original is unchanged
    resize(self, dimensions: int) -> None 
        Resize the vector into any dimensions, directly change the vector. This method does not try to maintain any properties of the vector, it will truncate or add additional 0s components so that the vector get to the target dimensions
    
    Static methods 
    --------------
    dot(v1, v2)
        The dot product between 2 vectors
    cross(v1, v2)
        The cross product between 2 vectors
    get_angle(v1, v2, rad=True)
        Get the angle between the 2 vectors. In the range [0, pi] radians or [0, 180] degrees only, if the angle is larger, it will just take the smaller or you can say absolute value of the co-terminal angle. So you should know what you are doing. Return angle in radians if `rad` is True, otherwise it will be in degrees
    """

    def __init__(self, *args: int | float) -> None:
        """
        Initialize the vector 

        Parameters
        ----------
        *args: int | float 
            The vectors components
        
        Raises
        ------
        TypeError
            If the components are not of type int or float
        """
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise TypeError("Vector components must be of type float")
        self.__components = [*args]

    @property 
    def components(self) -> list[int | float]:
        """
        The vector components
        """
        return self.__components

    def set_components(self, *args: int | float) -> None:
        """
        Set a new set of components for the vector 

        Parameters 
        ----------
        *args: int | float
        """
        self.__components = Vector(*args).components

    @property
    def dimensions(self) -> int:
        """
        The vector dimensions, or the length of the components list
        """
        return len(self.__components)
    
    def __repr__(self) -> str:
        """
        Representation

        Return the string of the form `Vector(*components)`
        """
        return f"Vector{tuple(self.__components)}"

    def __add__(self, other):
        """
        Addition

        Perform vectors addition 

        Parameters
        ----------
        self: Vector
            The first vector
        other: Vector 
            The other vector 

        Raises
        ------
        TypeError
            If the other operand is not a vector 
        exception.DimensionsError
            If the other vector not having the same dimensions as `self`
        """
        if not isinstance(other, Vector):
            return NotImplemented
        if self.dimensions != other.dimensions:
            raise DimensionsError("Operator `+` required two vectors with the same dimensions")
        return Vector(*utilities.array_add(self.components, other.components))

    def __sub__(self, other):
        """
        Subtraction

        Perform vectors subtraction

        Parameters
        ----------
        self: Vector
            The first vector
        other: Vector 
            The other vector 

        Raises
        ------
        TypeError
            If the other operand is not a vector 
        exception.DimensionsError
            If the other vector not having the same dimensions as `self`
        """
        if not isinstance(other, Vector):
            return NotImplemented
        if self.dimensions != other.dimensions:
            raise DimensionsError("Operator `-` required two vectors with the same dimensions")
        return Vector(*utilities.array_sub(self.components, other.components))
    
    def __mul__(self, other: int | float):
        """
        Scalar multiplication

        Perform vector scalar multiplication.
        IMPORTANT: the vector should be the first operand

        Parameters
        ----------
        self: Vector
            The first vector
        other: int | float
            The scalar

        Raises
        ------
        TypeError
            If the other is not a scalar
        """
        if not isinstance(other, (int, float)):
            raise TypeError("Vector multiplication using `*` is for scalar only, if you want vectors multiplication, use Vector.dot(v1, v2) or Vector.cross(v1, v2)")
        return Vector(*utilities.array_scalar_mul(self.components, other))

    def __truediv__(self, other: int | float):
        """
        Scalar true division

        Perform vector scalar true division
        IMPORTANT: the vector should be the first operand

        Parameters
        ----------
        self: Vector
            The first vector
        other: int | float
            The scalar

        Raises
        ------
        TypeError
            If the other is not a scalar
        """
        if not isinstance(other, (int, float)):
            raise TypeError("Vector true division using `/` is for scalar only, if you want vectors multiplication, use Vector.dot(v1, v2) or Vector.cross(v1, v2)")
        return Vector(*utilities.array_scalar_truediv(self.components, other))
    
    def __floordiv__(self, other: int | float):
        """
        Scalar floor division

        Perform vector scalar floor division
        IMPORTANT: the vector should be the first operand

        Parameters
        ----------
        self: Vector
            The first vector
        other: int | float
            The scalar

        Raises
        ------
        TypeError
            If the other is not a scalar
        """
        if not isinstance(other, (int, float)):
            
            raise TypeError("Vector floor division using `//` is for scalar only, if you want vectors multiplication, use Vector.dot(v1, v2) or Vector.cross(v1, v2)")
        return Vector(*utilities.array_floor_div(self.components, other))   

    def __eq__(self, other) -> bool:
        """
        Equal statement

        The equality of vectors 

        Parameters
        ----------
        self: Vector 
            The first vector 
        other: Vector
            The second vector

        Return 
        ------
        True if two vectors components are the same 
        else it will return False. If the other is not `Vector` type, automatically return False
        """
        if not isinstance(other, Vector):
            return False
        return self.components == other.components

    def __ne__(self, other) -> bool:
        """
        Not equal statement

        The non-equality of vectors 

        Parameters
        ----------
        self: Vector 
            The first vector 
        other: Vector
            The second vector

        Return 
        ------
        True if two vectors components are not the same 
        else it will return False. If the other is not `Vector` type, automatically return True
        """
        if not isinstance(other, Vector):
            return True
        return self.components != other.components

    def round(self, decimal_places: int = 0) -> None:
        """
        Rounding vectors

        Round the components to a given decimal_places
        Directly change the original vector 

        Parameters
        ----------
        self: Vector 
            The vector 
        decimal_places: int 
            The result decimal places
        
        Return
        ------
        Return None, only change the original vector
        """
        self.__components = [round(c, decimal_places) 
                            for c in self.__components]
    
    def rounded(self, decimal_places: int = 0):
        """
        The rounded vector

        Round and return the rounded vector components
        Not directly change the original vector 

        Parameters
        ----------
        self: Vector 
            The vector
        decimal_places: int 
            The result decimal places

        Return
        ------
        The rounded version of the vector
        """
        return Vector(*[round(c, decimal_places) 
                        for c in self.components])

    def __round__(self, decimal_places: int = 0):
        """
        Round function

        Work for round() built-in function
        The same as rounded
        """
        return self.rounded(decimal_places)

    @property
    def magnitude(self) -> float:
        """
        The vector magnitude
        """
        return sum([c**2 for c in self.components])**0.5

    @staticmethod
    def dot(v1, v2) -> float:
        """
        Vector dot product 
        
        Return the dot product of two vectors as a scalar.

        Parameters
        ----------
        v1: Vector 
            The first vector
        v2: Vector
            The second vector 

        Return 
        ------
        Return the dot product between the two input vector 

        Raises
        ------
        TypeError
            If either of the input is not a vector, TypeError will be raise 
        exceptions.DimensionsError
            If the two inputs dimensions are not the same, DimensionsError will be raise
        """
        if not isinstance(v1, Vector) or not isinstance(v2, Vector):
            raise TypeError("Dot product only accept two vectors as arguements")
        if v1.dimensions != v2.dimensions:
            raise DimensionsError("Dot product required 2 Vectors with the same dimensions")
        return sum(
            utilities.array_mul(v1.components, v2.components)
        )

    @staticmethod
    def get_angle(v1, v2, rad: bool=True) -> float:
        """
        Get angle 

        Get the angle between the two input vectors.
        
        Parameters
        ----------
        v1: Vector
            The first vector 
        v2: Vector 
            The second vectir
        rad: bool (default True)
            Output in radian form or not 

        Return
        ------
        The angle between the two vectors. If rad = True, return the angle in radian, otherwise return the angle in degree.
        IMPORTANT: This method only return angles in the range of the arccos function, specifically [0, pi] radian or [0, 180] degrees, if the angle is larger, the smaller angle will be taken, or you can also say the absolute value of the smallest co-terminal to that angle will be taken

        Raises
        ------
        TypeError
            If the two inputs are not vectors
        DimensionsError
            If the vectors are not in the same dimensions
        ZeroDivisionError
            If any of the vectors magnitude is 0
        """
        if v1.dimensions != v2.dimensions:
            raise DimensionsError("Not supported angle between two vectors with different dimensions")
        if not isinstance(v1, Vector) or not isinstance(v2, Vector):
            raise TypeError("get_angle() accept two vectors only")
        if v1.magnitude == 0 or v2.magnitude == 0:
            raise ZeroDivisionError("Cannot get angle between two vectors if one of them have 0 magnitude")
        angle_as_rad = np.arccos(Vector.dot(v1,v2)/(v1.magnitude*v2.magnitude))
        if rad is True:
           return angle_as_rad
        return angle_as_rad*(180/np.pi)

    @staticmethod
    def cross(v1, v2):
        """
        Cross product 

        The vectors cross product 

        Parameters
        ----------
        v1: Vector
            The first vector 
        v2: Vector
            The second vector

        Return
        ------
        The two vectors cross product. The direction of the resulting vector is depends on the order, so be careful

        Raises
        ------
        TypeError
            If the two inputs are not vectors
        DimensionsError
            Cross product only support 3D vectors for now, so dimensions other than 3 will raise DimensionsError
        """
        if not isinstance(v1, Vector) or not isinstance(v2, Vector):
            raise TypeError("Cross product only accept two vectors as arguements")
        if v1.dimensions != 3 or v2.dimensions != 3:
            raise DimensionsError("Only supported dot product for 3-dimensional vectors")
        x1, y1, z1 = v1.components
        x2, y2, z2 = v2.components
        return Vector(y1*z2 - z1*y2, z1*x2 - x1*z2, x1*y2 - y1*x2)

    def resize(self, dimensions: int) -> None:
        """
        Resize vector

        This method will resize the vector, in other words, force the vector into any dimensions you want, it does not maintain any properties, all it is doing is truncate or add 0s to the vectors, provide the ability to do cross product between 2D vectors for example, without create new 3D vectors with new components 
        """
        if not isinstance(dimensions, int):
            raise TypeError("Dimensions should be of type `int`")
        if self.dimensions > dimensions:
            self.__components = self.__components[:dimensions]
        else:
            complement = dimensions - self.dimensions
            self.__components = self.__components + [0]*complement
