
"""
Mathematical object `Matrix`
"""

from .utilities import *
from .exceptions import *
from .vectors import *

class Matrix:
    """
    `Matrix` is a mathematical object that can be seen as a two-dimensional array, where you need two indices to get any of its elements.
    -- New features will come soon --
    Supported operations: addition, subtraction, multiplication
    IMPORTANT: For multiplication, `Matrix` should be the first operand, the multiplication operator support scalar, vector and matrix!
    
    Supported statements: 
        Equality(==): True if the components are the same else False
        Non-equality(): True if the components are different else False
        If the two sides are not the same type, it will return True or False depends on the nature of the statement. No inequalities supported
    Representation:
        Formatted as `Matrix(*components)`

    Attributes
    ----------
    __components: list[list[int | float]]
        The matrix components, each elements represent a row. Not directly changeable, if you want to change the components, see `set_components()` method

    Properties
    ----------
    components(self) -> list[list[int | float]]
        Get the matrix components as a list contain each rows
    dimensions(self) -> tuple
        Get the Matrix dimensions, as a tuple in the form (rows, cols)
    
    Methods
    -------
    set_components(self, *args: list[int | float])
        Set a new set of components for the matrix

    """
    def __init__(self, *args: list[int | float]) -> None:
        """
        Initialize the matrix

        Parameters
        ----------
        *args: list[int | float] 
            Lists represent a row, every list should have the same length

        Raises
        ------
        TypeError
            For invalid types
        DimensionsError
            If the input lists are not the same length
        """
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
        """
        The matrix components
        """
        return self.__components
    
    def set_components(self, *args: list[int | float]) -> None:
        """
        Set a new set of components for the matrix
 
        Parameters
        ----------
        *args: list[int | float] 
            Lists represent a row, every list should have the same length

        Raises
        ------
        TypeError
            For invalid types
        DimensionsError
            If the input lists are not the same length
        """
        self.__components = Matrix(*args).components
    
    @property
    def dimensions(self) -> tuple:
        """
        Get the dimensions of a matrix, or the numbers of rows and columns.
        Return a tuple in the form (rows, cols)
        """
        return (len(self.__components), len(self.__components[0]))

    def __repr__(self) -> str:
        """
        Representation

        form: 
            `Matrix(*components)`
        """
        return f"Matrix{tuple(self.__components)}"

    def __add__(self, other):
        """
        Addition

        Perform matrix additon, add every corresponding elements of the matrices

        Parameters
        ----------
        self: Matrix
            The first Matrix
        other: Matrix
            The second Matrix

        Raises
        ------
        TypeError
            If the other input is not a matrix
        DimensionsError
            If the inputs matrix are not having the same dimensions
        """
        if not isinstance(other, Matrix):
            return NotImplemented
        if self.dimensions != other.dimensions:
            raise DimensionsError("Operand `+` required two matrices with the same dimensions")
        return Matrix(*[utilities.array_add(c1, c2) 
                        for c1, c2 in zip(self.components, other.components)])

    def __sub__(self, other):
        """
        Subtraction

        Perform matrix subtraction, add every corresponding elements of the matrices

        Parameters
        ----------
        self: Matrix
            The first Matrix
        other: Matrix
            The second Matrix

        Raises
        ------
        TypeError
            If the other input is not a matrix
        DimensionsError
            If the inputs matrix are not having the same dimensions
        """
        if not isinstance(other, Matrix):
            return NotImplemented
        if self.dimensions != other.dimensions:
            raise DimensionsError("Operand `+` required two matrices with the same dimensions")
        return Matrix(*[utilities.array_sub(c1, c2) 
                        for c1, c2 in zip(self.components, other.components)])
    
    def __mul__(self, other):
        """
        Multiplication 

        Perform matrix multiplication with scalar, vector and another matrix

        Parameters
        ----------
        self: Matrix
            The first matrix
        other: int | float | Vector | Matrix
            The second operand, can be scalar, vector or matrix

        Return
        ------
        Scalar: If it was a scalar multiplication, return a matrix
        Vector: If it was a vector multiplication, return a vector
        Matrix: If it was a matrix multiplication, return a matrix

        Raises
        ------
        TypeError
            If the operand is not supported
        DimensionsError
            If the second matrix or vector are not compatible for multiplication with the first one
        """
        if isinstance(other, (int, float)):
            return Matrix(*[utilities.array_scalar_mul(c, other) for c in self.components])
        if isinstance(other, Matrix):
            Arows, Acols = self.dimensions
            Brows, Bcols = other.dimensions
            if Acols != Brows:
                raise DimensionsError("Incompatible matrices for multiplication, expected matrix in the form m×n to b multiply by n×p")
            result = [[0]*Bcols for _ in range(Arows)]
            for j in range(Arows):
                for i in range(Bcols):
                    result[j][i] = sum([self.components[j][k]*other.components[k][i]
                                        for k in range(Acols)])
            return Matrix(*result)
        if isinstance(other, Vector):
            Arows, Acols = self.dimensions
            if Acols != other.dimensions:
                raise DimensionsError("Incompatible matrix-vector for multiplication, expected matrix in the form m×n to be multiply by n×1 vector")
            result = [0]*Arows
            for i in range(Arows):
                for j in range(Acols):
                    result[i] += self.components[i][j]*other.components[j]
            return Vector(*result)
        return NotImplemented
    
    def __eq__(self, other):
        """
        Equal statement

        The equality of vectors 

        Parameters
        ----------
        self: Matrix
        other: Any

        Return 
        ------
        True if two matrices components are the same 
        else it will return False. If the other is not `Matrix` type, automatically return False
        """
        if not isinstance(other, Matrix):
            return False 
        return self.components == other.components

    def __ne__(self, other):
        """
        Not equal statement

        The non-equality of vectors 

        Parameters
        ----------
        self: Matrix
        other: Any

        Return 
        ------
        True if two matrices components are not the same 
        else it will return False. If the other is not `Matrix` type, automatically return True
        """
        if not isinstance(other, Matrix):
            return True
        return self.components != other.components 
