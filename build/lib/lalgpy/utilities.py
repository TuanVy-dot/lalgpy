"""
Additional utilities
"""

from typing import Any, Sequence


def array_add(arr1: Sequence[Any], arr2: Sequence[Any]) -> list[Any]:
    """
    Arrays addition

    Add every corresponding elements of the input arrays together, produce one single output list, work for elements types that support addition operation. If the length are not the same, it will stop when one of the input arrays end

    Parameters
    ----------
    arr1: Sequence 
        Any sequence that is iterable
    arr2: Sequence 
        Any sequence that is iterable

    Return 
    ------
    Return a single list with every corresponding sums as output
    """
    return list(c1 + c2 for c1, c2 in zip(arr1, arr2))

def array_sub(arr1: Sequence[Any], arr2: Sequence[Any]) -> list[Any]:
    """
    Arrays subtraction

    Subtract every corresponding elements of the input arrays together, produce one single output list, work for elements types that support subtraction operation. If the length are not the same, it will stop when one of the input arrays end

    Parameters
    ----------
    arr1: Sequence 
        Any sequence that is iterable
    arr2: Sequence 
        Any sequence that is iterable

    Return 
    ------
    Return a single list with every corresponding differences as output
    """
    return list(c1 - c2 for c1, c2 in zip(arr1, arr2))

def array_scalar_mul(arr: Sequence[Any], scalar: int | float) -> list[Any]:
    """
    Array scalar multiplication
    
    Multiply every single elements of the input array by a scalar, work for elements types that support multiplication operation.

    Parameters
    ----------
    arr: Sequence
        Any sequence that is iterable
    scalar: int
        Factor

    Return
    ------
    Return a list with every corresponding products as output
    """
    return list(c*scalar for c in arr)

def array_scalar_truediv(arr: Sequence[Any], scalar: int | float) -> list[Any]:
    """
    Array scalar true division
    
    Truely divide every single elements of the input array by a scalar, work for elements types that support division operation.

    Parameters
    ----------
    arr: Sequence
        Any sequence that is iterable
    scalar: int
        Divisor

    Return
    ------
    Return a list with every corresponding quotient as output
    """
    return list(c/scalar for c in arr)

def array_floor_div(arr: Sequence[Any], scalar: int | float) -> list[Any]:
    """
    Array scalar floor division
    
    Floor divide every single elements of the input array by a scalar, work for elements types that support floor division operation.

    Parameters
    ----------
    arr: Sequence
        Any sequence that is iterable
    scalar: int
        Divisor

    Return
    ------
    Return a list with every corresponding quotient as output
    """
    return list(c//scalar for c in arr)

def array_mul(arr1: Sequence[Any], arr2: Sequence[Any]) -> list[Any]:
    """
    Arrays corresponding multiplication

    Multiply every corresponding elements of the input arrays together, produce one single output list, work for elements types that support multiplication operation. If the length are not the same, it will stop when one of the input arrays end

    Parameters
    ----------
    arr1: Sequence
        Any sequence that is iterable
    arr2: Sequence
        Any sequence that is iterable

    Return
    ------
    Return a list with every corresponding products as output
    """
    return list(c1*c2 for c1, c2 in zip(arr1, arr2))

def array_truediv(arr1: Sequence[Any], arr2: Sequence[Any]) -> list[Any]:
    """
    Arrays corresponding true division

    Truely divide every corresponding elements of the input arrays together, produce one single output list, work for elements types that support true division operation. If the length are not the same, it will stop when one of the input arrays end.
    The second array should not have zeros elements

    Parameters
    ----------
    arr1: Sequence
        Any sequence that is iterable
    arr2: Sequence
        Any sequence that is iterable

    Return
    ------
    Return a list with every corresponding quotient as output
    """
    return list(c1/c2 for c1, c2 in zip(arr1, arr2))

def array_floordiv(arr1: Sequence[Any], arr2: Sequence[Any]) -> list[Any]:
    """
    Arrays corresponding floor division

    Floor divide every corresponding elements of the input arrays together, produce one single output list, work for elements types that support floor division operation. If the length are not the same, it will stop when one of the input arrays end.
    The second array should not have zeros elements

    Parameters
    ----------
    arr1: Sequence
        Any sequence that is iterable
    arr2: Sequence
        Any sequence that is iterable

    Return
    ------
    Return a list with every corresponding quotient as output
    """
    return list(c1//c2 for c1, c2 in zip(arr1, arr2))
