"""
This module contains classes and functions to represent and operate on points
and objects in N-dimensional space.
"""

from dataclasses import dataclass

@dataclass(frozen=True, eq=True)
class Location2D:
    """
    Represents a point location on a two-dimensional plane. Instances of this
    dataclass will be immutable, and can be safely hashed and added to
    collections like dicts (as keys) and sets.
    """
    x: int
    y: int
